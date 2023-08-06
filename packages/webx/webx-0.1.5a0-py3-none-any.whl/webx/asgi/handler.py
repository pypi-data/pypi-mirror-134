import os
import importlib

import rich

from webx.asgi.core import ASGIEngine
from webx.config.settings import settings
from webx.views.models import _RegisteredView


class WebxHandler:
    """
    A class that links most of the framework together.
    """
    def __init__(self, *, settings_loc: str):
        self.hook_settings(settings_loc, environ=True)

        settings._recreate()
        self.settings = settings

        _main_routes = settings.get("ROUTING_FILE")
        self._main_routes = importlib.import_module(_main_routes)

        self._registered_main_routes = getattr(
            self._main_routes,
            "routes",
            []
        )
        
        self.asgi_engine = ASGIEngine()

        for view in self._registered_main_routes:
            self.asgi_engine.add_view(view)

        # Templating
        templating_settings = settings.get("TEMPLATING")
        engine_loc = templating_settings["engine_module"]
        engine_spec = templating_settings["engine_spec"]
        engine = importlib.import_module(engine_loc)
        engine = getattr(engine, engine_spec)
        self.templating_engine = engine

        # Monitoring
        monitor_settings = settings.get("WEBX_MONITORING")
        enabled = monitor_settings.get("enabled", False)
        password = monitor_settings.get("password")
        
        if not password:
            raise ValueError("Invalid password for webx monitor.")

        if enabled:
            # for a minor startup speed increase, only import the view IF we need it.
            from webx.monitoring.view import webx_monitor_stats
            
            view = _RegisteredView(
                webx_monitor_stats,
                "/webx-monitor",
                name="webx-monitor",
                view_type="http"
            )
            self.asgi_engine.add_view(view)

            rich.print(
                (
                    f"[bold cyan]WebX Monitor[/bold cyan] successfully setup. "
                    f"Password: [bold orange3]{password}[/bold orange3]\n"
                    "[bold slate_blue1]Route:[/bold slate_blue1] /webx-monitor"
                )
            )

        # Setup HTTPClient backends
        httpclient_settings = settings.get("HTTP_CLIENT_BACKEND")
        backend_loc = httpclient_settings["backend"]
        backend_module = importlib.import_module(backend_loc)
        backend = backend_module.BACKEND
        backend.register()

        # Adding the handler to the state
        self.settings.state["webx_handler"] = self


    def hook_settings(self, module_str: str, *, environ: bool = False):
        if environ is True:
            os.environ["WEBX_CUSTOM_SETTINGS"] = module_str
        # 'import' the settings file, to environment variable creation
        try:
            module = importlib.import_module(module_str)
            settings.settings_module = module
            try:
                self.settings.settings_module = module
            except AttributeError:
                pass
        except Exception:
            raise ValueError("Invalid settings module")
