# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from usersInfo.repository.exceptions import RequestTypeNotFoundError
from usersInfo.repository.models import GetUserRequestsModel


class usersRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_user_info(self) -> GetUserRequestsModel:
        cursor = self.dbCollection.find()
        respnse = await cursor.to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")
