from fastapi import APIRouter

router = APIRouter()


@router.get("/api/{portal_id}")
def access_portal(portal_id: str):
    return {"message": "service_in_hand portal"}


@router.get("/api/{portal_id}/{get_param}")
def access_portal(portal_id: str, get_param="none"):
    return {"message": "service_in_hand portal"}


@router.put("/api/{portal_id}")
def access_portal(portal_id: str):
    return {"message": "service_in_hand portal"}


@router.post("/api/{portal_id}")
def access_portal(portal_id: str):
    return {"message": "service_in_hand portal"}
