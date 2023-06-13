# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from generalSettings.repository.exceptions import RequestTypeNotFoundError
from generalSettings.repository.models import GetGeneralSettingsModel


class generalSettingsRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_general_settings(self) -> GetGeneralSettingsModel:
        cursor = self.dbCollection.find()
        respnse = await cursor.to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")

    async def get_unit_general_settings(self, codUnit) -> GetGeneralSettingsModel:
        cursor = self.dbCollection.find({"codUnit": codUnit})
        respnse = await cursor.to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")

    async def update_general_settings(
        self, generalSettings: GetGeneralSettingsModel
    ) -> bool:
        cursor = self.dbCollection.update_one({"$set": {generalSettings}})
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return True
        else:
            return False
