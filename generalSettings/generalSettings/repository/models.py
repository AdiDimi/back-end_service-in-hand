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


class CreateHoursPerDayModel(MongoBaseModel):
    hoursPerDay: HoursPerDayModel


class CreateBreakHoursModel(MongoBaseModel):
    # units:List[UnitModel]
    breakHours: conlist(DayHoursModel, min_items=1)

    def dict(self):
        return {
            "breakHours": [breakHour.dict() for breakHour in self.breakHours],
        }


class GetGeneralSettingModel(CreateBreakHoursModel, CreateHoursPerDayModel):
    lineDuration: int = Field(...)

    # baseUnitID: int = 1
    def dict(self):
        return {
            "lineDuration": self.lineDuration,
        }


class GetGeneralSettingsModel(MongoBaseModel):
    generalSettings: GetGeneralSettingModel

    def dict(self):
        return {
            "generalSettings": self.generalSettings.dict(),
        }
