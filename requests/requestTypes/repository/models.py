from bson import ObjectId
from pydantic import BaseModel, Field, conlist
from typing import List

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify__schema__(cls,field_schema):
        field_schema.update(type="string")

class MongoBaseModel(BaseModel):
    id:PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    class Config: 
        json_encoders = {ObjectId: str}

class UnitModel(MongoBaseModel):
    codUnit: int = Field(...)
    name:str = Field(...)
    def dict(self):
        return {
            'codUnit': self.codUnit,
            # 'items': [item.dict() for item in self.items],
            'name': self.name,
        }
 
class CreateUnitModel(MongoBaseModel):
    # units:List[UnitModel]
    units:conlist(UnitModel, min_items=1)
    def dict(self):
        return {
            'units': [unit.dict() for unit in self.units],
        }

class GetRequestTypeModel(CreateUnitModel):
    codRequestType: int = Field(...)
    requestType: str = Field(...)
    # baseUnitID: int = 1
    def dict(self):
        return {
            'codRequestType': self.codRequestType,
            'requestType': self.requestType,
        }

class GetRequestsTypesModel(MongoBaseModel):
    requestTypes:List[GetRequestTypeModel]
    def dict(self):
        return {
            'requestTypes': [requestType.dict() for requestType in self.requestTypes],
        }