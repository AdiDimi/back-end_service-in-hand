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


class GetAppointmentsModel(MongoBaseModel):
    appoitments: List[GetAppointmentModel]

    def dict(self):
        return {
            "appoitments": [appointment.dict() for appointment in self.appoitments],
        }