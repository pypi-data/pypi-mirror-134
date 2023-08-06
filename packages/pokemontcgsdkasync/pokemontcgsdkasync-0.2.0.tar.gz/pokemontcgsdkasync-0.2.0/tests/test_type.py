import unittest
from typing import List

from pokemontcgsdkasync import Type, AsyncClientContext


class TestType(unittest.IsolatedAsyncioTestCase):

    async def test_all_returns_types(self):
        async with AsyncClientContext():
            types: List[Type] = await Type.all().get()

            self.assertEqual(
                ["Colorless", "Darkness", "Dragon", "Fairy", "Fighting", "Fire", "Grass", "Lightning", "Metal",
                 "Psychic", "Water"], types)
