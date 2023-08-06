from importlib import import_module
from typing import (
    Callable,
    Optional,
    List
)

from webx.views.models import _RegisteredView


def route(
    endpoint: str,
    view: Callable,
    /,
    name: Optional[str] = None
) -> _RegisteredView: 
    view = _RegisteredView(
        view,
        endpoint,
        name=name,
        view_type="http"
    )

    return view

def include(
    module_path: str,
    *,
    routes_var: str = "routes"
) -> List[_RegisteredView]:
    module = import_module(module_path)
    routes = getattr(module, routes_var, None)
    assert routes is not None, "No routes found."

    return routes