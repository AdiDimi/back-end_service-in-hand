# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
import datetime
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

    def get_daily_slots(start, end, slot, date):
        # combine start time to respective day
        dt = datetime.combine(date, datetime.strptime(start, "%H:%M").time())
        slots = [dt]
        # increment current time by slot till the end time
        while dt.time() < datetime.strptime(end, "%H:%M").time():
            dt = dt + datetime.timedelta(minutes=slot)
            slots.append(dt)
        return slots
