from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from handler_exceptions import GetRequestTypeNotFoundException
from Appointments.database.database import create_db_collections
from fastapi.responses import JSONResponse

# from requestTypes.containers.single_container import requestTypesContainer
from Appointments.repository.exceptions import RequestTypeNotFoundError
from Appointments.repository.appointments_repository import appointmentsRepository
from Appointments.web.appointments_app import app
from Appointments.web.api.schemas import (
    AppointmentSchema,
    GetAppointmentSchema,
    GetWeekOpeningSchema,
)
import httpx

# from dependency_injector.wiring import inject, Provide
# import sys


@app.get(
    "/appointments",
    status_code=status.HTTP_200_OK,
    response_model=GetAppointmentSchema,
)
# @inject
async def get_appointments(dbCollection=Depends(create_db_collections)):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: appointmentsRepository = appointmentsRepository(dbCollection)
        respnse = await repo.get_appointments()
        if respnse is not None:
            return respnse
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


@app.put(
    "/appointments",
    status_code=status.HTTP_200_OK,
)
# @inject
async def put_appointments(
    appointment: AppointmentSchema,
    dbCollection=Depends(create_db_collections),
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: appointmentsRepository = appointmentsRepository(dbCollection)
        respnse = await repo.update_appointment(appointment)
        if respnse == True:
            return JSONResponse(
                status_code=201, content=f"Update appointment was successful"
            )
        else:
            return JSONResponse(
                status_code=500, content=f"Update appointments was unsuccessful"
            )
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"appointment was not found"
        )


@app.post(
    "/appointments/",
    status_code=status.HTTP_200_OK,
)
async def create_appointments(
    weekEvents: GetWeekOpeningSchema, dbCollection=Depends(create_db_collections)
):
    # repo:requestTypesRepository=Depends(Provide[requestTypesContainer.requestTypesService])):
    try:
        repo: appointmentsRepository = appointmentsRepository(dbCollection)
        async with httpx.AsyncClient() as client:
            respnse = await client.get("http://localhost:8005/generalSettings")
        if respnse is not None:
            weekOpenings = respnse.json()["weekOpenings"]
        return weekOpenings
    except RequestTypeNotFoundError:
        raise GetRequestTypeNotFoundException(
            status_code=404, detail=f"Requests where not found"
        )


# container = requestTypesContainer()
# container.wire(modules=[sys.modules[__name__]])
