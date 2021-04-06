from fastapi_session.session import Session
from typing import List


class SessionInterface:
    
    def __init__(self, session_key: str):
        self.session_key = session_key
    
    def get(self, key: str) -> object:
        pass
    
    def set(self, key: str, value: object):
        pass
    
    def clear(self):
        pass

    def has_key(self, key: str) -> bool:
        pass

    def keys(self) -> List[str]:
        pass

    def values(self) -> List[object]:
        pass
    
    def delete(self, key: str):
        pass
    
    def contains(self, item: object) -> bool:
        pass
    
    def length(self) -> int:
        pass
    
class BackendInterface:
        
    def get_session(self, key: str) -> Session:
        pass

    def cleanup(self) -> None:
        pass