from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from weekOpening.database.database import create_db_collections

# from requestTypes.containers.single_container import requestTypesContainer
from weekOpening.repository.exceptions import RequestTypeNotFoundError
from weekOpening.repository.weekOpening_repository import weekOpeningRepository
from weekOpening.web.weekOpening_app import app
from weekOpening.web.api.schemas import (
    CreateWeekOpeningsSchema,
)

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/weekOpenings/{cod_unit}",
    status_code=status.HTTP_200_OK,
    response_model=CreateWeekOpeningsSchema,
)
# @inject
async def get_weekOpenings(
    dbCollection=Depends(create_db_collections), cod_unit: int = 5
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: weekOpeningRepository = weekOpeningRepository(dbCollection)
        respnse = await repo.get_week_opening(cod_unit)
        if respnse is not None:
            return respnse
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


@app.put(
    "/weekOpenings",
    status_code=status.HTTP_200_OK,
)
# @inject
async def put_weekOpenings(
    weekOpening: CreateWeekOpeningsSchema, dbCollection=Depends(create_db_collections)
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: weekOpeningRepository = weekOpeningRepository(dbCollection)
        respnse = await repo.update_week_opening(weekOpening)
        if respnse == True:
            return JSONResponse(
                status_code=201, content=f"weekOpening Update was successful"
            )
        else:
            return JSONResponse(
                status_code=500, content=f"weekOpening Update user was unsuccessful"
            )
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


@app.post(
    "/weekOpenings",
    status_code=status.HTTP_200_OK,
)
# @inject
async def post_weekOpenings(
    weekOpening: CreateWeekOpeningsSchema, dbCollection=Depends(create_db_collections)
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: weekOpeningRepository = weekOpeningRepository(dbCollection)
        respnse = await repo.update_week_opening(weekOpening)
        if respnse == True:
            return JSONResponse(
                status_code=201, content=f"weekOpening Update was successful"
            )
        else:
            return JSONResponse(
                status_code=500, content=f"weekOpening Update user was unsuccessful"
            )
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
