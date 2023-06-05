from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from generalSettings.database.database import create_db_collections

# from requestTypes.containers.single_container import requestTypesContainer
from generalSettings.repository.exceptions import RequestTypeNotFoundError
from generalSettings.repository.generalSettings_repository import (
    generalSettingsRepository,
)
from generalSettings.web.generalSettings_app import app
from generalSettings.web.api.schemas import (
    GetGeneralSettingsSchema,
)

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/generalSettings",
    status_code=status.HTTP_200_OK,
    response_model=GetGeneralSettingsSchema,
)
# @inject
async def get_requestTypes(dbCollection=Depends(create_db_collections)):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: generalSettingsRepository = generalSettingsRepository(dbCollection)
        respnse = await repo.get_general_settings()
        if respnse is not None:
            return {"generalSettings": respnse}
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
