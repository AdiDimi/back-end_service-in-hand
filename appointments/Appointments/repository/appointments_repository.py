# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
from Appointments.repository.exceptions import RequestTypeNotFoundError
from Appointments.repository.models import GetAppointmentModel


class appointmentsRepository:
    def __init__(self, dbCollection):
        self.dbCollection = dbCollection

    async def get_appointments(self) -> GetAppointmentModel:
        cursor = self.dbCollection.find_one({"baseUnitCod": 1})
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return respnse
        raise RequestTypeNotFoundError("Requests where not found")
