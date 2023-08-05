import asyncio
from .responce import Response


class Request:
    def __init__(self, sender, chain):
        self._sender = sender
        self.chain = chain

    def __getattr__(self, item):
        return Request(self._sender, self.chain+[item])

    @asyncio.coroutine
    def __call__(self, **kwargs):
        method = '.'.join(self.chain)
        response = yield from self._sender.send(method, **kwargs)
        return Response(method=method, kwargs=kwargs, **response)
