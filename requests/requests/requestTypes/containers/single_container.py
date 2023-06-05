from dependency_injector import containers, providers
from requestTypes.repository.requestsType_repository import requestTypesRepository

class requestTypesContainer(containers.DeclarativeContainer):
    requestTypesService =  providers.Singleton(requestTypesRepository)

# class RecipeAppContainer(containers.DeclarativeContainer):
#         requesttypescontainer = providers.Container(requestTypesContainer)