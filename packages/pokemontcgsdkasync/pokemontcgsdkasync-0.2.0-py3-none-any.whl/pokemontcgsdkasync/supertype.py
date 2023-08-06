from pokemontcgsdkasync.query import ArrayQuery
from pokemontcgsdkasync.querybuilder import QueryBuilder


class Supertype:
    RESOURCE = 'supertypes'

    @staticmethod
    def all() -> ArrayQuery:
        return QueryBuilder(Supertype).array()
