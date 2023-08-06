import unittest
from typing import List

from pokemontcgsdkasync import Card, AsyncClientContext


class TestCard(unittest.IsolatedAsyncioTestCase):

    async def test_find_returns_card(self):
        async with AsyncClientContext():
            card: Card = await Card.find('xy7-54').get()

            self.assertEqual('xy7-54', card.id)
            self.assertEqual('Gardevoir', card.name)
            self.assertEqual('Pokémon', card.supertype)
            self.assertEqual(['Stage 2'], card.subtypes)
            self.assertEqual('130', card.hp)
            self.assertEqual(['Fairy'], card.types)
            self.assertEqual('Kirlia', card.evolvesFrom)
            self.assertTrue(len(card.abilities) == 1)
            self.assertTrue(len(card.attacks) == 1)
            self.assertTrue(len(card.weaknesses) == 1)
            self.assertTrue(len(card.resistances) == 1)
            self.assertEqual(['Colorless', 'Colorless'], card.retreatCost)
            self.assertEqual(2, card.convertedRetreatCost)
            self.assertEqual('xy7', card.set.id)
            self.assertEqual('54', card.number)
            self.assertEqual('TOKIYA', card.artist)
            self.assertEqual('Rare Holo', card.rarity)
            self.assertEqual(
                'It has the power to predict the future. Its power peaks when it is protecting its Trainer.',
                card.flavorText)
            self.assertEqual([282], card.nationalPokedexNumbers)
            self.assertEqual('https://prices.pokemontcg.io/tcgplayer/xy7-54', card.tcgplayer.url)

    async def test_all_with_params_return_cards(self):
        async with AsyncClientContext():
            cards: List[Card] = await Card.where(q='supertype:pokemon subtypes:mega').get()
            self.assertTrue(len(cards) >= 70)

    async def test_all_with_page_returns_cards(self):
        async with AsyncClientContext():
            cards: List[Card] = await Card.where(page=1).get()
            self.assertEqual(250, len(cards))

    async def test_all_with_page_and_page_size_returns_card(self):
        async with AsyncClientContext():
            cards: List[Card] = await Card.where(page=1, pageSize=1).get()
            self.assertEqual(1, len(cards))

    async def test_where_generator(self):
        async with AsyncClientContext():
            c = 0
            async for card in Card.where(q='set.id:pl3', orderBy='?orderBy=number', pageSize=100).generator():
                c += 1
            assert c == 153
