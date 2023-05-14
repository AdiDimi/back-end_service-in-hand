
from fastapi import Depends
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from requestTypes.database.database import create_db_collections
from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.repository.requestsType_repository import requestTypesRepository
from requestTypes.web.app import app
from requestTypes.web.api.schemas import (
     GetRequestsTypesSchema,
)

@app.get("/requestTypes",status_code=status.HTTP_200_OK, response_model=GetRequestsTypesSchema)
async def get_requestTypes(dbCollection=Depends(create_db_collections)):
      try:
        repo:requestTypesRepository = requestTypesRepository(dbCollection)
        respnse = await repo.get_request_types()
        if respnse is not None:
            return {"requestTypes": respnse}
      except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(status_code=404, detail=f"Requests where not found")
 