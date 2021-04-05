class SessionInterface:
    
    def __init__(self, session_key: str):
        self.session_key = session_key
    
    def get(self, key: str):
        pass
    
    def set(self, key: str, value: object):
        pass
    
    def clear(self):
        pass

    def has_key(self, key: str) -> bool:
        pass

    def keys(self):
        pass

    def values(self):
        pass
    
    def delete(self, key: str):
        pass
    
    def contains(self, item: object) -> bool:
        pass
    
    def length(self) -> int:
        pass
    
class BackendInterface:
        
    def get_session(self, key: str) -> SessionInterface:
        pass

    def cleanup(self):
        pass