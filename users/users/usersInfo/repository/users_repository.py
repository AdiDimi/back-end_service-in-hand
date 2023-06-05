# from requestTypes.database.database import create_db_collections
from usersInfo.repository.exceptions import RequestTypeNotFoundError
from usersInfo.repository.models import GeteUserRequestModel


class usersRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_user_info(self) -> GeteUserRequestModel:
        cursor = self.dbCollection.find_one({"userID": 5102422})
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")

    async def update_user_info(self, usrInfo: GeteUserRequestModel) -> bool:
        cursor = self.dbCollection.update_one(
            {"userID": usrInfo.userID}, {"$set": {"userRequests": usrInfo.userRequests}}
        )
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return True
        else:
            return False
