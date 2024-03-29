import logging
from fastapi import Request

logger = logging.getLogger("uvicorn.access")


def call_api_gateway(request: Request):
    portal_id = request.path_params["portal_id"]
    # get_param = request.path_params["get_param"]
    print(request.path_params)
    if portal_id == str("requestTypes"):
        raise RedirectRequestTypesServiceException()
    elif portal_id == str("appointments"):
        raise RedirectAppointmentsServiceException()
    elif portal_id == str("users"):
        raise RedirectUsersServiceException()
    elif portal_id == str("weekOpening"):
        if request.path_params.get("get_param") is not None:
            raise RedirectWeekOpeningWithParamException()
        else:
            raise RedirectWeekOpeningServiceException()
    elif portal_id == str("generalSettings"):
        raise RedirectGeneralSettingsServiceException()


class RedirectRequestTypesServiceException(Exception):
    pass


class RedirectAppointmentsServiceException(Exception):
    pass


class RedirectUsersServiceException(Exception):
    pass


class RedirectWeekOpeningServiceException(Exception):
    pass


class RedirectWeekOpeningWithParamException(Exception):
    pass


class RedirectGeneralSettingsServiceException(Exception):
    pass
