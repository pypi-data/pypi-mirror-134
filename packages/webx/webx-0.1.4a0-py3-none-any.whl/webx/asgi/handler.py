import os
import importlib

from webx.asgi.core import ASGIEngine
from webx.config.settings import settings
from webx.templating.engine import StandardEngine


class WebxHandler:
    """
    A class that links most of the framework together.
    """
    def __init__(self, *, settings_loc: str):
        settings._recreate()

        self.hook_settings(settings_loc, environ=True)
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
        engine_loc = templating_settings["engine"]
        engine = importlib.import_module(engine_loc)
        self.templating_engine = engine

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
