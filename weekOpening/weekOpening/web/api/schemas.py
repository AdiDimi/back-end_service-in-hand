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


class CreateWeekOpeningsSchema(BaseModel):
    weekOpenings: List[GetWeekOpeningSchema]


class GetWeekOpeningUnitSchema(CreateWeekOpeningsSchema):
    codUnit: int

    class Config:
        extra = Extra.forbid


# class CreateWeekOpeningUnitsSchema(BaseModel):
#     GetAllEvents: GetWeekOpeningUnitSchema
