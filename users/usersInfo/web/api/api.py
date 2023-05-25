from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from usersInfo.database.database import create_db_collections

# from requestTypes.containers.single_container import requestTypesContainer
from usersInfo.repository.exceptions import RequestTypeNotFoundError
from usersInfo.repository.users_repository import usersRepository
from usersInfo.web.users_app import app
from usersInfo.web.api.schemas import (
    GetUserRequestsSchema,
)

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=GetUserRequestsSchema,
)
# @inject
async def get_requestTypes(dbCollection=Depends(create_db_collections)):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: usersRepository = usersRepository(dbCollection)
        respnse = await repo.get_user_info()
        if respnse is not None:
            return {"userInfo": respnse}
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
