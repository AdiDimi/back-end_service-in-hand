from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Extra


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class DayHoursSchema(BaseModel):
    fromHour: str
    toHour: str


class HoursPerDaySchema(BaseModel):
    sunday: DayHoursSchema
    monday: DayHoursSchema
    tuesday: DayHoursSchema
    wednesday: DayHoursSchema
    thursday: DayHoursSchema


class CreateHoursPerDaySchema(BaseModel):
    hoursPerDay: HoursPerDaySchema


class CreateBreakHoursSchema(BaseModel):
    # units:List[UnitModel]
    breakHours: List[DayHoursSchema]


class GetGeneralSettingSchema(CreateBreakHoursSchema, CreateHoursPerDaySchema):
    lineDuration: int


class GetGeneralSettingsSchema(BaseModel):
    generalSettings: GetGeneralSettingSchema

    class Config:
        extra = Extra.forbid
