# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from weekOpening.repository.exceptions import RequestTypeNotFoundError
from weekOpening.repository.models import GetWeekOpeningUnitModel


class weekOpeningRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_week_opening(self) -> GetWeekOpeningUnitModel:
        cursor = self.dbCollection.find_one({"codUnit": 5})
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")
