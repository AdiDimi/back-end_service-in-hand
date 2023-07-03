from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, conlist, validator
from typing import List

from Appointments.web.api.schemas import StatusEnum


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify__schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


class AppointmentModel(MongoBaseModel):
    codRequest: str = Field(...)
    HandleUnit: str = Field(...)
    codRequestType: int = Field(...)
    codUnit: int = Field(...)
    requestDate: str = Field(...)
    requestItems: List[str] = []
    status: str = Field(...)
    registeredToID: str = Field(...)
    remarks: str = Field(...)

    # @validator("requestDate")
    # def date_requested_datetime(cls, value):
    #     return datetime.strftime(value, "%m/%d/%Y, %H:%M:%S")

    def dict(self):
        return {
            "codRequest": self.codRequest,
            "HandleUnit": self.HandleUnit,
            "codRequestType": self.codRequestType,
            "codUnit": self.codUnit,
            "requestDate": self.requestDate,
            "status": self.status,
            "registeredToID": self.registeredToID,
            "remarks": self.remarks,
        }


class CreateAppointmentModel(MongoBaseModel):
    # units:List[UnitModel]
    openRequests: conlist(AppointmentModel)

    # , min_items=1)
    def dict(self):
        return {
            "openRequests": [appointment.dict() for appointment in self.openRequests],
        }


class GetAppointmentModel(CreateAppointmentModel):
    baseUnitCod: int = Field(...)

    def dict(self):
        return {
            "baseUnitCod": self.baseUnitCod,
        }


class EventModel(MongoBaseModel):
    id: str = Field(...)
    title: str = Field(...)
    date: str = Field(...)
    fromHour: str = Field(...)
    toHour: str = Field(...)
    isAllDay: bool = Field(...)

    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "fromHour": self.fromHour,
            "toHour": self.toHour,
            "isAllDay": self.isAllDay,
        }


class CreateEventModel(MongoBaseModel):
    # units:List[UnitModel]
    events: conlist(EventModel, min_items=1)

    def dict(self):
        return {
            "units": [event.dict() for event in self.events],
        }


class GetWeekOpeningModel(CreateEventModel):
    weekStartDate: str = Field(...)

    def dict(self):
        return {
            "weekStartDate": self.weekStartDate,
        }


class DayHoursModel(MongoBaseModel):
    fromHour: str = Field(...)
    toHour: str = Field(...)

    def dict(self):
        return {
            "fromHour": self.fromHour,
            "toHour": self.toHour,
        }


class HoursPerDayModel(MongoBaseModel):
    sunday: DayHoursModel = Field(...)
    monday: DayHoursModel = Field(...)
    tuesday: DayHoursModel = Field(...)
    wednesday: DayHoursModel = Field(...)
    thursday: DayHoursModel = Field(...)

    def dict(self):
        return {
            "sunday": self.sunday.dict(),
            "monday": self.monday.dict(),
            "tuesday": self.tuesday.dict(),
            "wednesday": self.wednesday.dict(),
            "thursday": self.thursday.dict(),
        }


# class CreateHoursPerDayModel(MongoBaseModel):
#     hoursPerDay: HoursPerDayModel

#     def dict(self):
#         return {
#             "hoursPerDay": self.hoursPerDay.dict(),
#         }


class CreateBreakHoursModel(MongoBaseModel):
    # units:List[UnitModel]
    breakHours: conlist(DayHoursModel)

    def dict(self):
        return {
            "breakHours": [breakHour.dict() for breakHour in self.breakHours],
        }


class GetGeneralSettingModel(CreateBreakHoursModel):
    codUnit: int = Field(...)
    lineDuration: int = Field(...)
    hoursPerDay: HoursPerDayModel = {}

    # baseUnitID: int = 1
    def dict(self):
        return {
            "codUnit": self.codUnit,
            "lineDuration": self.lineDuration,
            "hoursPerDay": self.hoursPerDay.dict(),
        }


class GetGeneralSettingsModel(MongoBaseModel):
    generalSettings: List[GetGeneralSettingModel]

    def dict(self):
        return {
            "generalSettings": [
                generalSetting.dict() for generalSetting in self.generalSettings
            ],
        }


# class GetAppointmentsModel(MongoBaseModel):
#     appoitments: GetAppointmentModel

#     def dict(self):
#         return {
#             "GetAllAppointments": self.appoitments.dict()
#             #   [appointment.dict() for appointment in self.appoitments],
#         }
