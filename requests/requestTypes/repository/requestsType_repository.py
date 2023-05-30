# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.repository.models import GetRequestsTypesModel


class requestTypesRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_request_types(self) -> GetRequestsTypesModel:
        cursor = self.dbCollection.find()
        respnse = await cursor.to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")
