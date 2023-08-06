from dataclasses import dataclass
from typing import Optional

from dacite import from_dict

from pokemontcgsdkasync import SingleQuery, MultipleQuery
from pokemontcgsdkasync.legality import Legality
from pokemontcgsdkasync.querybuilder import QueryBuilder
from pokemontcgsdkasync.setimage import SetImage


@dataclass
class Set:
    RESOURCE = 'sets'

    id: str
    images: SetImage
    legalities: Legality
    name: str
    printedTotal: int
    ptcgoCode: Optional[str]
    releaseDate: str
    series: str
    total: int
    updatedAt: str

    @staticmethod
    def find(set_id) -> SingleQuery:
        return QueryBuilder(Set, Set.transform).find(set_id)

    @staticmethod
    def where(**kwargs) -> MultipleQuery:
        return QueryBuilder(Set, Set.transform).where(**kwargs)

    @staticmethod
    def all() -> MultipleQuery:
        return QueryBuilder(Set, Set.transform).all()

    @staticmethod
    def transform(response):
        response = from_dict(Set, response)
        return response
