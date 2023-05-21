from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import RedirectResponse, JSONResponse
from gateway.api_router import (
    call_api_gateway,
    RedirectRequestTypesServiceException,
    RedirectAppointmentsServiceException,
    RedirectUsersServiceException,
)
from controller import service_in_hand

# from requests.requestTypes.web import requestTypes_app
# from appointments.Appointments.web import appointments_app

# from users.users.web import users_app

from loguru import logger
from uuid import uuid4

app = FastAPI()
app.include_router(
    service_in_hand.router,
    dependencies=[Depends(call_api_gateway)],
    # prefix="/service_in_hand",
)
logger.add(
    "info.log",
    format="Log: [{extra[log_id]}: {time} - {level} - {message} ",
    level="INFO",
    enqueue=True,
)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info("Request to access " + request.url.path)
        try:
            response = await call_next(request)
        except Exception as ex:
            logger.error(f"Request to " + request.url.path + " failed: {ex}")
            response = JSONResponse(content={"success": False}, status_code=500)
        finally:
            logger.info("Successfully accessed " + request.url.path)
            return response


@app.exception_handler(RedirectRequestTypesServiceException)
def exception_handler_student(
    request: Request, exc: RedirectRequestTypesServiceException
) -> Response:
    return RedirectResponse(url="http://localhost:8001/requestTypes")


@app.exception_handler(RedirectAppointmentsServiceException)
def exception_handler_faculty(
    request: Request, exc: RedirectAppointmentsServiceException
) -> Response:
    return RedirectResponse(url="http://localhost:8002/appointments")


@app.exception_handler(RedirectUsersServiceException)
def exception_handler_library(
    request: Request, exc: RedirectUsersServiceException
) -> Response:
    return RedirectResponse(url="http://localhost:8003/appointments")


# app.mount("/BackEnd_ServiceInHand/requests", requestTypes_app.app)
# app.mount("/BackEnd_ServiceInHand/appointments", appointments_app.app)
# # app.mount("/service_in_hand/users", users_app.app)
