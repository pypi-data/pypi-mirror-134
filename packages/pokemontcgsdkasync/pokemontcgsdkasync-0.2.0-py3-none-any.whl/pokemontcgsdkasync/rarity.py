from pokemontcgsdkasync.query import ArrayQuery
from pokemontcgsdkasync.querybuilder import QueryBuilder


class Rarity:
    RESOURCE = 'rarities'

    @staticmethod
    def all() -> ArrayQuery:
        return QueryBuilder(Rarity).array()
