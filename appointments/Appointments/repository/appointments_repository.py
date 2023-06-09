# from fastapi import Depends
# from requestTypes.database.database import create_db_collections
import datetime
from Appointments.repository.exceptions import RequestTypeNotFoundError
from Appointments.repository.models import AppointmentModel, GetAppointmentModel


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

    async def update_appointment(self, appointment: AppointmentModel) -> bool:
        cursor = self.dbCollection.update_one(
            {"openRequests.codRequest": appointment.codRequest},
            {"$set": {"openRequests.$.status": appointment.status}},
        )
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return True
        else:
            return False

    async def create_appointments(self, appointment: AppointmentModel) -> bool:
        cursor = self.dbCollection.update_one(
            {"openRequests.codRequest": appointment.codRequest},
            {"$set": {"openRequests.$.status": appointment.status}},
        )
        respnse = await cursor
        # .to_list(length=None)
        if respnse is not None:
            return True
        else:
            return False

    def get_daily_slots(start, end, slot, date):
        # combine start time to respective day
        dt = datetime.combine(date, datetime.strptime(start, "%H:%M").time())
        slots = [dt]
        # increment current time by slot till the end time
        while dt.time() < datetime.strptime(end, "%H:%M").time():
            dt = dt + datetime.timedelta(minutes=slot)
            slots.append(dt)
        return slots
