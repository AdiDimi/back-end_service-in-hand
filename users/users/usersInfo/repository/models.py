from datetime import date
import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, conlist, validator
from typing import Annotated, List, Literal, Optional, Union


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


class LogisticItemModel(MongoBaseModel):
    id: str = Field(...)
    amount: str = Field(...)
    remarks: str = Field(...)

    def dict(self):
        return {
            "id": self.id,
            "remarks": self.remarks,
            "amount": self.amount,
        }


class LogisticRequestModel(MongoBaseModel):
    codRequest: int = Field(...)
    codRequestType: Literal[1]
    HandleUnit: str = Field(...)
    codUnit: Optional[int] = 0
    requestDate: date = "1900-01-01T00:00:00"
    status: str = Field(...)
    remarks: str = Field(...)
    requestItems: conlist(LogisticItemModel)

    # @validator("requestDate", pre=True)
    # def requestDate_datetime(cls, value):
    #     return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")

    def dict(self):
        return {
            "codRequest": self.codRequest,
            "codRequestType": self.codRequestType,
            "HandleUnit": self.HandleUnit,
            "codUnit": self.codUnit,
            "requestDate": self.requestDate,
            "status": self.status,
            "requestItems": [item.dict() for item in self.requestItems],
            "remarks": self.name,
        }


class MaintenanceRequestModel(MongoBaseModel):
    codRequest: int = Field(...)
    codRequestType: Literal[4]
    HandleUnit: str = Field(...)
    codUnit: Optional[int] = 0
    requestDate: date = "1900-01-01T00:00:00"
    status: str = Field(...)
    unitName: str = Field(...)
    target: str = Field(...)
    targetAudience1: str = Field(...)
    targetAudience2: str = Field(...)
    targetAudience3: str = Field(...)
    amount1: str = Field(...)
    amount2: str = Field(...)
    amount3: str = Field(...)
    level1: str = Field(...)
    level2: str = Field(...)
    level3: str = Field(...)
    telephone: str = Field(...)
    malfunctionDesc: str = Field(...)
    toolsZ: str = Field(...)
    optDate1: str = Field(...)
    optDate2: str = Field(...)
    optDate3: str = Field(...)

    # @validator("requestDate", pre=True)
    # def requestDate_datetime(cls, value):
    #     return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")

    def dict(self):
        return {
            "codRequest": self.codRequest,
            "codRequestType": self.codRequestType,
            "HandleUnit": self.HandleUnit,
            "codUnit": self.codUnit,
            "requestDate": self.requestDate,
            "status": self.status,
            "unitName": self.unitName,
            "codUnit": self.codUnit,
            "target": self.target,
            "targetAudience1": self.targetAudience1,
            "targetAudience2": self.targetAudience2,
            "targetAudience3": self.targetAudience3,
            "amount1": self.amount1,
            "amount2": self.amount2,
            "amount3": self.amount3,
            "level1": self.level1,
            "level2": self.level2,
            "level3": self.level3,
            "telephone": self.telephone,
            "malfunctionDesc": self.malfunctionDesc,
            "toolsZ": self.toolsZ,
            "optDate1": self.optDate1,
            "optDate2": self.optDate2,
            "optDate3": self.optDate3,
        }


class QualificationRequestModel(MongoBaseModel):
    codRequest: int = Field(...)
    codRequestType: Literal[2]
    HandleUnit: str = Field(...)
    codUnit: Optional[int] = 0
    requestDate: str = "1900-01-01T00:00:00"
    status: str = Field(...)
    contactMan: str = Field(...)
    telephone: str = Field(...)
    malfunctionDesc: str = Field(...)
    toolsZ: str = Field(...)
    optDate1: str = Field(...)
    optDate2: str = Field(...)
    optDate3: str = Field(...)

    # @validator("requestDate", pre=True)
    # def requestDate_datetime(cls, value):
    #     return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")

    def dict(self):
        return {
            "codRequest": self.codRequest,
            "codRequestType": self.codRequestType,
            "HandleUnit": self.HandleUnit,
            "codUnit": self.codUnit,
            "requestDate": self.requestDate,
            "status": self.status,
            "malfunctionDesc": self.malfunctionDesc,
            "contactMan": self.contactMan,
            "telephone": self.telephone,
            "toolsZ": self.toolsZ,
            "optDate1": self.optDate1,
            "optDate2": self.optDate2,
            "optDate3": self.optDate3,
        }


class UserRequestModel(BaseModel):
    __root__: Annotated[
        Union[LogisticRequestModel, MaintenanceRequestModel, QualificationRequestModel],
        Field(discriminator="codRequestType"),
    ]


class CreateUserRequestModel(MongoBaseModel):
    userRequests: conlist(UserRequestModel)

    def dict(self):
        return {
            "userRequests": [userRequest.dict() for userRequest in self.userRequests],
        }


class GeteUserRequestModel(CreateUserRequestModel):
    userID: int = Field(...)
    authGroup: int = Field(...)
    adminUnits: conlist(int) = [0]

    def dict(self):
        return {
            "userID": self.userID,
            "authGroup": self.authGroup,
            "adminUnits": [unit for unit in self.adminUnits],
        }


# class GetUserRequestsModel(MongoBaseModel):
#     GetRequestsToUser: GeteUserRequestModel

#     def dict(self):
#         return {
#             "GetRequestsToUser": self.GetRequestsToUser.dict()
#             #   [info.dict() for info in self.userInfo],
#         }
