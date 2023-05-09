
from fastapi import HTTPException
from starlette import status
from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.repository.requestsType_repository import get_request_types
from requestTypes.web.app import app
from requestTypes.web.api.schemas import (
     GetRequestsTypesSchema,
)

@app.get("/requestTypes",status_code=status.HTTP_200_OK, response_model=GetRequestsTypesSchema)
async def get_requestTypes():
      try:
        respnse = await get_request_types()
        if respnse is not None:
            return {"requestTypes": respnse}
      except RequestTypeNotFoundError:
        raise HTTPException(status_code=404, detail=f"Requests where not found")
 