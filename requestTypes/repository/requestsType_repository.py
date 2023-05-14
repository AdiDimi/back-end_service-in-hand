
from requestTypes.database.database import get
from requestTypes.repository.exceptions import RequestTypeNotFoundError
from requestTypes.database.models import GetRequestsTypesModel

async def get_request_types()->GetRequestsTypesModel:
    respnse = await get()
    if respnse is not None:
            return respnse
    raise RequestTypeNotFoundError('Requests where not found')
