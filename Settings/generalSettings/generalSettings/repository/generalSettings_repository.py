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
