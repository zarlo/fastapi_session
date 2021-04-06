import time, os

import pickle

from .session_interface import BackendInterface, SessionInterface

class FileSystemBackend(BackendInterface):
    def __init__(self, session_key: str, data_path: str):
        self.session_key = session_key
        self.data_path = data_path
    
    def get_session(self, key: str) -> SessionInterface:
        return FileSystemInterface(key, self.data_path)

    def cleanup(self) -> None:
        now = time.time()

        for f in os.listdir(self.data_path):
            if os.stat(f).st_mtime < now - 7 * 86400:
                if os.path.isfile(f):
                    os.remove(os.path.join(self.data_path, f))
    
class FileSystemInterface(SessionInterface):
    
    def __init__(self, session_key: str, data_path: str):
        self.session_key = session_key
        self.data_path = '{0}/{1}'.format(data_path, session_key)
        with open(self.data_path,'rb') as fp:
            self._data = pickle.load(fp)
    
    def save(self):
        with open(self.data_path,'wb') as fp:
            self._data = pickle.dump(self._data, fp)
        
    def get(self, key: str):
        return self._data[key]
    
    def set(self, key: str, value: object):
        self._data[key] = value
        self.save()
    
    def clear(self):
        self._data = {}
        self.save()

    def has_key(self, key: str) -> bool:
        return self._data.has_key(key)

    def keys(self):
        return self._data.keys()

    def values(self):
        return  self._data.values()
    
    def delete(self, key: str):
        del self._data[key]
        self.save()
    
    def contains(self, item: object) -> bool:
        return  self._data.contains(item)
    
    def length(self) -> int:
        return None