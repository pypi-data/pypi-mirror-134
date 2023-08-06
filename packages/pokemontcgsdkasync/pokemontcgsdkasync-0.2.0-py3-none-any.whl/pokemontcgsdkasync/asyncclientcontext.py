from typing import Dict

from aiohttp import ClientSession
from aiohttp.abc import HTTPException

from pokemontcgsdkasync.pokemontcgexception import PokemonTcgException


class AsyncClientContext:

    _session: ClientSession = None

    def __init__(self, api_key: str = None):
        self.api_key: str = api_key
        self.headers: Dict = {'User-Agent': 'Mozilla/5.0'}
        if api_key is not None:
            self.headers['X-Api-Key'] = api_key

    async def __aenter__(self):
        AsyncClientContext._session = ClientSession(
            base_url="https://api.pokemontcg.io",
            headers=self.headers
        )
        return self

    async def __aexit__(self, *err):
        await AsyncClientContext._session.close()
        AsyncClientContext._session = None

    @classmethod
    async def get(cls, url: str, params: Dict = None):
        """Invoke an HTTP GET request on a url
        
        Args:
            url (string): URL endpoint to request
            params (dict): Dictionary of url parameters 
        Returns:
            dict: JSON response as a dictionary
        """
        try:
            async with cls._session.get("/v2/" + url, params=params) as resp:
                return await resp.json()

        except HTTPException as err:
            raise PokemonTcgException(err.read())
