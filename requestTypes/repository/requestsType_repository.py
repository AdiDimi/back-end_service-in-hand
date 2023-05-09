

from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.repository.models import GetRequestsTypesModel
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)

client =  AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)

database = client[DB_NAME]

requestTypes_collection = database.get_collection("requestTypes")

async def get_request_types()->GetRequestsTypesModel:
    respnse = await requestTypes_collection.find().to_list(1000)
    if respnse is not None:
            return respnse
    raise RequestTypeNotFoundError('Requests where not found')
