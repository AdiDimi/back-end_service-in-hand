from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Extra, validator


class StatusEnum(Enum):
    created = "חדש"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "סגור"


class AppointmentSchema(BaseModel):
    codRequest: str
    HandleUnit: str
    codRequestType: int
    codUnit: int
    requestDate: str
    requestItems: List[str] = []
    status: str
    registeredToID: str = ""
    remarks: str = ""

    # @validator("requestDate")
    # def date_requested_datetime(cls, value):
    #     return datetime.strftime(value, "%m/%d/%Y, %H:%M:%S")


class CreateAppointmentsSchema(BaseModel):
    openRequests: List[AppointmentSchema]
    # conlist(UnitSchema, min_items=1)


class GetAppointmentSchema(CreateAppointmentsSchema):
    baseUnitCod: int
    # requestType: str
    # baseUnitID: int = 1


class EventSchema(BaseModel):
    id: str
    title: str
    date: str
    fromHour: str
    toHour: str
    isAllDay: bool


class CreateEventSchema(BaseModel):
    events: List[EventSchema]


# conlist(UnitSchema, min_items=1)


class GetWeekOpeningSchema(CreateEventSchema):
    weekStartDate: str


# class GetAppointmentsSchema(BaseModel):
#     GetAllAppointments: GetAppointmentSchema

#     class Config:
#         extra = Extra.forbid


class DayHoursSchema(BaseModel):
    fromHour: str = ""
    toHour: str = ""


class HoursPerDaySchema(BaseModel):
    sunday: DayHoursSchema
    monday: DayHoursSchema
    tuesday: DayHoursSchema
    wednesday: DayHoursSchema
    thursday: DayHoursSchema


# class CreateHoursPerDaySchema(BaseModel):
#     hoursPerDay: HoursPerDaySchema


class CreateBreakHoursSchema(BaseModel):
    # units:List[UnitModel]
    breakHours: List[DayHoursSchema]


class GetGeneralSettingSchema(CreateBreakHoursSchema):
    lineDuration: int
    hoursPerDay: HoursPerDaySchema


class GetGeneralSettingsSchema(BaseModel):
    generalSettings: List[GetGeneralSettingSchema]
