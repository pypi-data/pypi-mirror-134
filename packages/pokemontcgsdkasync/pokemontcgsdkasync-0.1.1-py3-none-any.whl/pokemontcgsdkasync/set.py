from dataclasses import dataclass
from typing import Optional

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
    async def find(set_id):
        return await QueryBuilder(Set).find(set_id)

    @staticmethod
    async def where(**kwargs):
        return await QueryBuilder(Set).where(**kwargs)

    @staticmethod
    async def all():
        return await QueryBuilder(Set).all()
