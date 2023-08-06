import unittest
from typing import List

from pokemontcgsdkasync import Subtype, AsyncClientContext


class TestSubtype(unittest.IsolatedAsyncioTestCase):

    async def test_all_returns_subtypes(self):
        async with AsyncClientContext():
            subtypes: List[Subtype] = await Subtype.all().get()

            self.assertTrue(len(subtypes) > 15)
            self.assertTrue('MEGA' in subtypes)
