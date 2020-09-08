import inspect

from fastapi import Request, Cookie
from .session_interface import BackendInterface

class SessionManager:

    def __init__(self, backend: BackendInterface = None):
        self._backend = backend
        self._session_id_callback = None
    
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
