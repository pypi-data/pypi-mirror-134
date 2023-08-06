from pokemontcgsdkasync.query import ArrayQuery
from pokemontcgsdkasync.querybuilder import QueryBuilder


class Subtype:
    RESOURCE = 'subtypes'

    @staticmethod
    def all() -> ArrayQuery:
        return QueryBuilder(Subtype).array()
