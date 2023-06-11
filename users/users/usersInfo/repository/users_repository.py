# from requestTypes.database.database import create_db_collections
from dataclasses import asdict
import datetime
from usersInfo.repository.exceptions import RequestTypeNotFoundError
from usersInfo.repository.models import (
    CreateUserRequestModel,
    GeteUserRequestModel,
    UserRequestModel,
)


class usersRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_user_info(self) -> GeteUserRequestModel:
        cursor = self.dbCollection.find_one({"userID": 2222222})
        respnse: GeteUserRequestModel = await cursor
        # .to_list(length=None)
        if respnse is not None:
            if (GeteUserRequestModel(**respnse)).authGroup == 2:
                usrCursor = self.dbCollection.find(
                    # {
                    #     "userRequests.requestDate": {
                    #         "$gte": "2020-03-01",
                    #         "$lt": "2021-03-31",
                    #     }
                    # },
                    {"userRequests.codUnit": {"$in": respnse["adminUnits"]}},
                )
                users: list[GeteUserRequestModel] = await usrCursor.to_list(1000)
                if users is not None:
                    for user in users:
                        for request in user["userRequests"]:
                            # print(request)
                            currReq: UserRequestModel = request
                            if currReq["codUnit"] in respnse["adminUnits"]:
                                respnse["userRequests"].append(request)

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
