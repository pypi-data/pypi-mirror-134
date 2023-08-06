from typing import Optional

import aiohttp

import webx.httpclient
from webx.httpclient.backends.base import BaseBackend


class AsyncHTTPClientBackend(BaseBackend):
    """
    The async httpclient backend for webx. As of now,
    ClientSessions are created on the first http request,
    since aiohttp dislikes creating client-sessions outside of
    an async context.
    """
    def __init__(self):
        self.__session: Optional[aiohttp.ClientSession] = None

    async def request(
        self,
        method: str,
        url: str,
        **kwargs
    ) -> aiohttp.ClientSession:
        resp = await self.__session.request(method, url, **kwargs)
        return resp

    async def close(self):
        if self.__session is not None:
            if self.__session.closed is not True:
                try:
                    await self.__session.close()
                except Exception:
                    # ignore any closing errors
                    pass

    @classmethod
    def register(cls, *args, **kwargs):
        backend = cls(*args, **kwargs)
        setattr(webx.httpclient, "backend", backend)
        return backend

BACKEND = AsyncHTTPClientBackend