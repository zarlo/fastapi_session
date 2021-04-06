import asyncio

from .session_interface import SessionInterface

class Session(dict):
    def __init__(self, session_backend: SessionInterface):
        self.session_backend = session_backend
    
    async def __setitem__(self, key, item):
        if asyncio.iscoroutine(self.session_backend.set):
            await self.session_backend.set(key, item)
        else:
            self.session_backend.set(key, item)

    async def __getitem__(self, key):
        if asyncio.iscoroutine(self.session_backend.get):
            return await self.session_backend.get(key)
        else:
            return self.session_backend.get(key)

    async def __len__(self):
        if asyncio.iscoroutine(self.session_backend.length):
            return await self.session_backend.length()
        else:
            return self.session_backend.length()

    async def __delitem__(self, key):
        if asyncio.iscoroutine(self.session_backend.delete):
            await self.session_backend.delete(key)
        else:
            self.session_backend.delete(key)

    async def get(self, key, default=None):
        data = None
        if asyncio.iscoroutine(self.session_backend.get):
            data = await self.session_backend.get(key)
        else:
            data = self.session_backend.get(key)
        if data is None:
            return default
        return data

    async def clear(self):
        if asyncio.iscoroutine(self.session_backend.clear):
            return await self.session_backend.clear()
        else:
            return self.session_backend.clear()

    async def has_key(self, key: str):
        if asyncio.iscoroutine(self.session_backend.has_key):
            return await self.session_backend.has_key(key)
        else:
            return self.session_backend.has_key(key)

    async def keys(self):
        if asyncio.iscoroutine(self.session_backend.keys):
            return await self.session_backend.keys()
        else:
            return self.session_backend.keys()

    async def values(self):
        if asyncio.iscoroutine(self.session_backend.values):
            return await self.session_backend.values()
        else:
            return self.session_backend.values()

    async def __contains__(self, item):
        if asyncio.iscoroutine(self.session_backend.contains):
            return await self.session_backend.contains()
        else:
            return self.session_backend.contains()
    