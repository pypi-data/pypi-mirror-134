from __future__ import annotations

import traceback
from typing import (
    List,
    TYPE_CHECKING,
    Coroutine,
)

from webx.http.response import BaseResponse
from webx.views.models import _RegisteredView
from webx.tooling.multidict import MultiDict

if TYPE_CHECKING:
    from webx.types.asgi import (
        Scope,
        Receive,
        Send
    )


class _LifespanEnclosure:
    def __init__(self, engine):
        self._engine = engine
    
    async def __aenter__(self):
        await self._engine.startup()
    
    async def __aexit__(self, *_):
        await self._engine.shutdown()

class ASGIEngine:
    """
    An engine class to handle ASGI
    """
    def __init__(self):
        self.views: List[_RegisteredView] = []
        self.event_handlers: MultiDict = {}
        self._enclosure = _LifespanEnclosure(self)

    async def startup(self):
        startup_handlers = self.event_handlers.get("startup", [])
        for handler in startup_handlers:
            await handler()
    
    async def shutdown(self):
        shutdown_handlers = self.event_handlers.get("shutdown", [])
        for handler in shutdown_handlers:
            try:
                await handler()
            except BaseException:
                # any error that occurs, we just ignore,
                # since we're shutting down our application
                pass
        
    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send
    ):
        print(scope)
        scopeT = scope["type"]
        assert scopeT in {"http", "websocket", "lifespan"}, "Scope type not supported"

        if scopeT == "lifespan":
            await self.handle_lifespan(scope, receive, send)
            return None

        for view in self.views:
            if view._match_scope(scope):
                args = view._extract_scope(scope)
                response = await view(*args)
                await response(scope, receive, send)
                return None

        # no view found, formulate a standard 404 response and send back.
        response = BaseResponse("Not Found", status=404)
        await response(scope, receive, send)

    async def handle_lifespan(
        self,
        _scope: Scope,
        receive: Receive,
        send: Send
    ):
        print("Lifespan called")
        started = False
        await receive()
        try:
            async with self._enclosure:
                await send({"type": "lifespan.startup.complete"})
                started = True
                await receive()
        except Exception:
            exc = traceback.format_exc()
            if started is False:
                await send({"type": "lifespan.startup.failed", "message": exc})
            else:
                await send({"type": "lifespan.shutdown.failed", "message": exc})
            raise # re-raise so the exception can be logged to STDOUT
        else:
            await send({"type": "lifespan.shutdown.complete"})

    def add_view(self, view: _RegisteredView):
        self.views.append(view)

    def add_event_handler(self, handler: Coroutine):
        name = handler.__name__
        self.event_handlers[name] = handler