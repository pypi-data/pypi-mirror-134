from jinja2 import (
    Environment,
    PackageLoader,
    select_autoescape,
    Template
)

from webx.config.settings import settings


class StandardEngine:
    """
    This class holds a Jinja2 environment within it.
    Also has the ability to re-create environments based on settings changes.
    """
    def __init__(self):
        templates_config = settings.get("TEMPLATES")
        templates_location = templates_config["templates_location"]
        enabled = templates_config["enabled"]

        self._enabled = enabled

        if not enabled:
            return None

        self._environment = Environment(
            loader=PackageLoader(templates_location),
            autoescape=select_autoescape()
        )

    def _refresh(self):
        _temp_engine = StandardEngine()
        self._environment = _temp_engine._environment
        return _temp_engine

    async def render(
        self,
        template: str,
        *,
        context: dict = {}
    ) -> str:
        if self._enabled is False:
            raise RuntimeError("The templates feature isn't enabled. Please enable it.")
        
        template: Template = self._environment.get_template(template)
        rendered = await template.render_async(**context)
        return rendered
        