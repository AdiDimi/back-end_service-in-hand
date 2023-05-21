import logging
from fastapi import Request

logger = logging.getLogger("uvicorn.access")


def call_api_gateway(request: Request):
    portal_id = request.path_params["portal_id"]
    print(request.path_params)
    if portal_id == str(1):
        raise RedirectRequestTypesServiceException()
    elif portal_id == str(2):
        raise RedirectAppointmentsServiceException()
    elif portal_id == str(3):
        raise RedirectUsersServiceException()


class RedirectRequestTypesServiceException(Exception):
    pass


class RedirectAppointmentsServiceException(Exception):
    pass


class RedirectUsersServiceException(Exception):
    pass
