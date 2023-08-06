from webx.config.settings import settings
from webx.http.response import HTMLResponse


async def render(
    template: str,
    *,
    context: dict = {}
) -> str:
    """
    A shortcut to render templates using the templating engine stored in the settings state.
    """
    handler = settings.state.get("webx_handler")
    engine = handler.templating_engine
    output = await engine.render(template, **context)
    return HTMLResponse(output)