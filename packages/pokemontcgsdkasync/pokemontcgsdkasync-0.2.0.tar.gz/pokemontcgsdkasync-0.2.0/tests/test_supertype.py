import unittest
from typing import List

from pokemontcgsdkasync import Supertype, AsyncClientContext


class TestSupertype(unittest.IsolatedAsyncioTestCase):

    async def test_all_returns_supertypes(self):
        async with AsyncClientContext():
            supertypes: List[Supertype] = await Supertype.all().get()

            self.assertEqual(["Energy", "Pokémon", "Trainer"], supertypes)
