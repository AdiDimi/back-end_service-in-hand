from fastapi import Depends, Body
from fastapi.responses import JSONResponse
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from usersInfo.database.database import create_db_collections

# from requestTypes.containers.single_container import requestTypesContainer
from usersInfo.repository.exceptions import RequestTypeNotFoundError
from usersInfo.repository.users_repository import usersRepository
from usersInfo.web.users_app import app
from usersInfo.web.api.schemas import (
    GetUserRequestSchema,
)

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=GetUserRequestSchema,
)
# @inject
async def get_requestTypes(dbCollection=Depends(create_db_collections)):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: usersRepository = usersRepository(dbCollection)
        respnse = await repo.get_user_info()
        if respnse is not None:
            return respnse
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


@app.put(
    "/users",
    status_code=status.HTTP_200_OK,
)
# @inject
async def put_requestTypes(
    usrInfo: GetUserRequestSchema = Body(...),
    dbCollection=Depends(create_db_collections),
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: usersRepository = usersRepository(dbCollection)
        respnse = await repo.update_user_info(usrInfo)
        if respnse == True:
            return JSONResponse(status_code=201, content=f"Update user was successful")
        else:
            return JSONResponse(
                status_code=500, content=f"Update user was unsuccessful"
            )
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"user was not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
