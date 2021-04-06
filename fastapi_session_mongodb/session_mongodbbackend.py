from fastapi_session.session import Session
import time, os
from motor.motor_asyncio import AsyncIOMotorClient

import pickle

from fastapi_session.session_interface import BackendInterface, SessionInterface

class MongoDBBackend(BackendInterface):
    def __init__(self, session_key: str, client: AsyncIOMotorClient, collection: str = "session"):
        self.session_key = session_key
        self.client = client
        self.collection = collection
    
    def get_session(self, key: str) -> Session:
        return Session(MongoDBInterface(key, self.client, self.collection))

    def cleanup(self) -> None:
        pass
    
class MongoDBInterface(SessionInterface):
    
    def __init__(self, session_key: str, client: AsyncIOMotorClient, collection: str):
        self.session_key = session_key
        self.client = client
        self.collection = client[collection]
    
    async def save(self, data):
        await self.collection.replace_one({'_id': data._id}, data)

    async def get_hole(self):
        return await self.collection.find_one({'key': self.session_key})
    
    async def get(self, key: str):
        return await self.get_hole()[key]
    
    async def set(self, key: str, value: object):
        await self.collection.replace_one({'key': self.session_key}, { key: value })
    
    async def clear(self):
        await self.collection.find_one_and_delete({'key': self.session_key})

    async def has_key(self, key: str) -> bool:
        return key in await self.keys()

    async def keys(self):
        return await self.get_hole().keys()

    async def values(self):
        return await self.get_hole().values()
    
    async def delete(self, key: str):
        pass
        #await self.collection.delete_many({'key': self.session_key})
    
    async def contains(self, item: object) -> bool:
        return item in await self.values()
    
    async def length(self) -> int:
        return await self.collection.count_documents({})