from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.database.models import GetRequestsTypesModel
from requestTypes.web.app import app

DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)
DB_COLLECTION = config("DB_COLLECTION", cast=str)

@app.on_event("startup")
async def startup_db_client():
    app.client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)
    app.database = app.client[DB_NAME]
    app.dbCollection = app.database.get_collection(DB_COLLECTION)

@app.on_event("shutdown")
async def shutdown_db_client():
    app.client.close()

async def get()->GetRequestsTypesModel:
    respnse = await app.dbCollection.find().to_list(1000)
    if respnse is not None:
            return respnse
    raise RequestTypeNotFoundError('Requests where not found')

