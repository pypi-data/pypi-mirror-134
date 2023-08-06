import requests

import webx.httpclient
from webx.httpclient.backends.base import BaseBackend


class SyncHTTPClientBackend(BaseBackend):
    def __init__(self):
        self.__session = requests.Session()

    def request(
        self,
        method: str,
        url: str,
        *args,
        **kwargs
    ) -> requests.Response:
        resp = self.__session.request(method, url, *args, **kwargs)
        return resp

    def close(self):
        self.__session.close()
    
    @classmethod
    def register(cls, *args, **kwargs):
        backend = cls(*args, **kwargs)
        setattr(webx.httpclient, "backend", backend)
        return backend

BACKEND = SyncHTTPClientBackend
        