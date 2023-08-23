from decouple import config

DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)
DB_COLLECTION = config("DB_COLLECTION", cast=str)




