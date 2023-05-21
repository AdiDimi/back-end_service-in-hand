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

class UnitSchema(BaseModel):
    codUnit: int
    name:str
 
class CreateUnitSchema(BaseModel):
    units:List[UnitSchema]
    # conlist(UnitSchema, min_items=1)

class GetRequestTypeSchema(CreateUnitSchema):
    codRequestType: int
    requestType: str
    # baseUnitID: int = 1

class GetRequestsTypesSchema(BaseModel):
    requestTypes:List[GetRequestTypeSchema]
    class Config:
         extra = Extra.forbid   
