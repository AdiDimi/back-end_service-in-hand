from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional
from pydantic import BaseModel, Extra, Field
from typing import Union
from typing import Annotated


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class LogisticItemSchema(BaseModel):
    id: str
    amount: str
    remarks: str


class LogisticRequestSchema(BaseModel):
    codRequest: int
    codRequestType: Literal[1]
    HandleUnit: str
    requestDate: str
    status: str
    remarks: str
    requestItems: List[LogisticItemSchema]


class MaintenanceRequestSchema(BaseModel):
    codRequest: int
    codRequestType: Literal[4]
    HandleUnit: str
    requestDate: str
    status: str
    unitName: str
    target: str
    targetAudience1: str
    targetAudience2: str
    targetAudience3: str
    amount1: str
    amount2: str
    amount3: str
    level1: str
    level2: str
    level3: str
    telephone: str
    malfunctionDesc: str
    toolsZ: str
    optDate1: str
    optDate2: str
    optDate3: str


class QualificationRequestSchema(BaseModel):
    codRequest: int
    codRequestType: Literal[2]
    HandleUnit: str
    requestDate: str
    status: str
    contactMan: str
    telephone: str
    malfunctionDesc: str
    toolsZ: str
    optDate1: str
    optDate2: str
    optDate3: str


class UserRequestSchema(BaseModel):
    __root__: Annotated[
        Union[
            LogisticRequestSchema, MaintenanceRequestSchema, QualificationRequestSchema
        ],
        Field(discriminator="codRequestType"),
    ]


class CreateUserRequestSchema(BaseModel):
    userRequests: List[UserRequestSchema]
    # conlist(UnitSchema, min_items=1)


class GetUserRequestSchema(CreateUserRequestSchema):
    userID: int

    # class Config:
    #     extra = Extra.forbid


# class GetUserRequestsSchema(BaseModel):
#     GetRequestsToUser: GetUserRequestSchema

#     class Config:
#         extra = Extra.forbid
