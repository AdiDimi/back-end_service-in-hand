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

from requestTypes.web.api import api
