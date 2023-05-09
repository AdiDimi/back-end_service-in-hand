from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# define origins
origins = ["*"]

app = FastAPI(debug=True)

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)
#     app.mongodb = app.mongodb_client[DB_NAME]



# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()

from requestTypes.web.api import api
