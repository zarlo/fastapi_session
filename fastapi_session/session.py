from .session_interface import SessionInterface

class Session(dict):
    def __init__(self, session_backend: SessionInterface):
        self.session_backend = session_backend
    
    def __setitem__(self, key, item):
        self.session_backend.set(key, item)

    def __getitem__(self, key):
        return self.session_backend.get(key)

    def __len__(self):
        return self.session_backend.length()

    def __delitem__(self, key):
        self.session_backend.delete(key)

    def get(self, key, default=None):
        try:
            return self.session_backend.get(key)
        except:
            return default

    def clear(self):
        return self.session_backend.clear()

    def has_key(self, key: str):
        return self.session_backend.has_key(key)

    def keys(self):
        return self.session_backend.keys()

    def values(self):
        return self.session_backend.values()

    def __contains__(self, item):
        return self.session_backend.contains()
    