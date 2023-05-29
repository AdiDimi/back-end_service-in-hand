from bson import ObjectId
from pydantic import BaseModel, Field, conlist
from typing import List


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


class CreateWeekOpeningsModel(MongoBaseModel):
    weekOpenings: List[GetWeekOpeningModel]

    def dict(self):
        return {
            "weekOpenings": [week.dict() for week in self.weekOpenings],
        }


class GetWeekOpeningUnitModel(CreateWeekOpeningsModel):
    codUnit: int = Field(...)

    def dict(self):
        return {
            "codUnit": self.codUnit,
        }


class CreateWeekOpeningUnitsModels(MongoBaseModel):
    unitWeekOpenings: List[GetWeekOpeningUnitModel]

    def dict(self):
        return {
            "unitWeekOpenings": [unitWeek.dict() for unitWeek in self.unitWeekOpenings],
        }
