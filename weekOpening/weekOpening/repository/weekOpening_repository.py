# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from weekOpening.repository.exceptions import RequestTypeNotFoundError
from weekOpening.repository.models import CreateWeekOpeningUnitsModels


class weekOpeningRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_week_opening(self) -> CreateWeekOpeningUnitsModels:
        cursor = self.dbCollection.find()
        respnse = await cursor.to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")
