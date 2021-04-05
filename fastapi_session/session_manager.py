import inspect
import random
import string
from typing import Callable, Awaitable, Union

from fastapi import Request, Cookie, Response
from .session_interface import BackendInterface

class SessionManager:

    def __init__(self, backend: BackendInterface = None):
        self._backend = backend
        self._session_id_callback = None
        self._cookie_name = None
    
    def use_cookie(self, cookie_name: str = "session"):
        """
        This is just a basic session id that use's a cookie
        """
        self._cookie_name = cookie_name
        self.session_id(self._cookie)
        
    def init_cookie(self, response: Response, id: str = None):
        if id is None:
            id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
            
        response.set_cookie(self._cookie_name, id)
            
    def _cookie(self, request: Request) -> str:
        return request.cookies.get(self._cookie_name, None)
        
    
    def session_id(self, callback: Union[Callable, Awaitable]) -> Union[Callable, Awaitable]:
        """
        This sets the callback to retrieve the session id.
        The function should take an unique identifier
        and return the id as a string.

        Basic usage::

            >>> from fastapi import FastAPI
            >>> from fastapi_session import SessionManager

            >>> app = FastAPI()

            >>> manager = SessionManager(backend)

            >>> manager.session_id(get_id)

            >>> # this is the preferred way
            >>> @manager.session_id
            >>> def get_id(request: Request):
            ...     # get session id logic here

        :param Callable or Awaitable callback: The callback which returns the user
        :return: The callback
        """
        self._session_id_callback = callback
        return callback
    
    async def __call__(self, request: Request):
        
        if self._session_id_callback is None:
            raise Exception(
                "Missing session_id_callback callback"
            )

        if inspect.iscoroutinefunction(self._session_id_callback):
            _session_id = await self._session_id_callback(request)
        else:
            _session_id = self._session_id_callback(request)

        return self._backend.get_session(_session_id)
