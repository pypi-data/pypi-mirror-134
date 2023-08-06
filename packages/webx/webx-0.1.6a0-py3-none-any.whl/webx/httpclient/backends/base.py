class BaseBackend:
    def __init__(self):
        raise NotImplementedError

    def request(self, *args, **kwargs):
        # can be overridden to be async
        raise NotImplementedError
    
    def close(self):
        raise NotImplementedError