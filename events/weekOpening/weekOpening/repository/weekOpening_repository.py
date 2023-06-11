# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from weekOpening.repository.exceptions import RequestTypeNotFoundError
from weekOpening.repository.models import GetWeekOpeningModel, GetWeekOpeningUnitModel


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

    async def update_week_opening(self, openingWeek: GetWeekOpeningUnitModel) -> bool:
        cursor = self.dbCollection.update_one(
            {"codUnit": openingWeek.codUnit},
            {"weekOpenings.id": openingWeek.id},
            {"$set": {"weekOpenings.$": openingWeek}},
        )
        respnse = await cursor

        if respnse is not None:
            return True
        else:
            return False

    async def insert_week_opening(self, openingWeek: GetWeekOpeningModel) -> bool:
        cursor = self.dbCollection.update(
            {"codUnit": openingWeek.codUnit},
            {"$push": {"weekOpenings": openingWeek}},
        )
        respnse = await cursor

        if respnse is not None:
            return True
        else:
            return False
        # raise RequestTypeNotFoundError("Requests where not found")
