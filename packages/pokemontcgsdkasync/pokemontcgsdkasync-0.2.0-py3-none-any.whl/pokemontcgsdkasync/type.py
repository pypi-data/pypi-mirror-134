from pokemontcgsdkasync.query import ArrayQuery
from pokemontcgsdkasync.querybuilder import QueryBuilder


class Type:
    RESOURCE = 'types'

    @staticmethod
    def all() -> ArrayQuery:
        return QueryBuilder(Type).array()
