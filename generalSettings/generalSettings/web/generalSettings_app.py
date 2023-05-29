import datetime
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# import logging
from background import audit_log_error, audit_log_transaction
from handler_exceptions import GetRequestTypeNotFoundException, InvalidActionException
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as GlobalStarletteHTTPException
from fastapi.exceptions import RequestValidationError
from generalSettings.database.database import close_async_db, create_async_db

# # setup loggers
# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
# # get root logger
# logger = logging.getLogger(__name__)

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


# @app.exception_handler(GlobalStarletteHTTPException)
# def global_exception_handler(req: Request, ex: GlobalStarletteHTTPException):
#     with open("audit_log.txt", mode="a") as reqfile:
#         content = f"GlobalStarletteHTTPException - message:{str(ex.detail)} status code:{str(ex.status_code)} received at {datetime.datetime.now()} \n"
#         reqfile.writelines(content)
#     return PlainTextResponse(f"Error message:{ex}", status_code=ex.status_code)


@app.exception_handler(RequestValidationError)
def validationerror_exception_handler(req: Request, ex: RequestValidationError):
    with open("audit_log.txt", mode="a") as reqfile:
        content = f"RequestValidationError - message:{str(ex)} status code:400 received at {datetime.datetime.now()} \n"
        reqfile.writelines(content)
    return PlainTextResponse(f"Error message:{str(ex)}", status_code=400)


@app.exception_handler(GetRequestTypeNotFoundException)
def feedback_exception_handler(req: Request, ex: GetRequestTypeNotFoundException):
    with open("audit_log.txt", mode="a") as reqfile:
        content = f"GetRequestTypeNotFoundException - message:{str(ex.detail)} status code:{str(ex.status_code)} received at {datetime.datetime.now()} \n"
        reqfile.writelines(content)
    return JSONResponse(
        status_code=ex.status_code, content={"message": f"error: {ex.detail}"}
    )


@app.exception_handler(InvalidActionException)
def rating_exception_handler(req: Request, ex: InvalidActionException):
    with open("audit_log.txt", mode="a") as reqfile:
        content = f"InvalidActionException - message:{str(ex.detail)} status code:{str(ex.status_code)} received at {datetime.datetime.now()} \n"
        reqfile.writelines(content)
    return JSONResponse(
        status_code=ex.status_code, content={"message": f"error: {ex.detail}"}
    )


@app.middleware("http")
async def log_transaction_filter(request: Request, call_next):
    start_time = datetime.datetime.now()
    method_name = request.method
    qp_map = "None"
    # request.query_parasms
    pp_map = "None"
    # request.path_params
    response = await call_next(request)
    process_time = datetime.datetime.now() - start_time
    with open("request_log.txt", mode="a") as reqfile:
        content = f" method: {method_name} ,processed time:{process_time}, from start time: {start_time} received at {datetime.datetime.now()} \n"
        reqfile.writelines(content)
    response.headers["X-Time-Elapsed"] = str(process_time)
    return response


@app.on_event("startup")
async def startup_db_client():
    create_async_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    close_async_db()


from generalSettings.web.api import api
