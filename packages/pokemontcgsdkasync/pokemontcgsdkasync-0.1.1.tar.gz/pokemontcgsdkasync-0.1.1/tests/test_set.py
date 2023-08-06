import unittest
from typing import List

from pokemontcgsdkasync import Set, AsyncClientContext


class TestSet(unittest.IsolatedAsyncioTestCase):

    async def test_find_returns_set(self):
        async with AsyncClientContext():
            card_set: Set = await Set.find('xy11')
            self.assertEqual('xy11', card_set.id)
            self.assertEqual('Steam Siege', card_set.name)
            self.assertEqual('XY', card_set.series)
            self.assertEqual(114, card_set.printedTotal)
            self.assertEqual(116, card_set.total)
            self.assertEqual('STS', card_set.ptcgoCode)
            self.assertEqual("2016/08/03", card_set.releaseDate)

    async def test_where_filters_on_name(self):
        async with AsyncClientContext():
            sets: List[Set] = await Set.where(q='name:steam')

            self.assertEqual(1, len(sets))
            self.assertEqual('xy11', sets[0].id)

    async def test_all_returns_all_sets(self):
        async with AsyncClientContext():
            sets: List[Set] = await Set.all()

            self.assertGreater(len(sets), 70)
