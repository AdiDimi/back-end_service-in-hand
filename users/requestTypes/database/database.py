from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)
DB_COLLECTION = config("DB_COLLECTION", cast=str)

def create_async_db():
 global client
 client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)

def create_db_collections():
    database = client[DB_NAME]
    dbCollection = database.get_collection(DB_COLLECTION)
    return dbCollection


def close_async_db():
     client.close()
