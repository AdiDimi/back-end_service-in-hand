from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from weekOpening.database.database import create_db_collections

# from requestTypes.containers.single_container import requestTypesContainer
from weekOpening.repository.exceptions import RequestTypeNotFoundError
from weekOpening.repository.weekOpening_repository import weekOpeningRepository
from weekOpening.web.weekOpening_app import app
from weekOpening.web.api.schemas import (
    CreateWeekOpeningUnitsSchema,
)

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/weekOpenings",
    status_code=status.HTTP_200_OK,
    response_model=CreateWeekOpeningUnitsSchema,
)
# @inject
async def get_weekOpenings(dbCollection=Depends(create_db_collections)):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: weekOpeningRepository = weekOpeningRepository(dbCollection)
        respnse = await repo.get_week_opening()
        if respnse is not None:
            return {"unitWeekOpenings": respnse}
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
