from fastapi import APIRouter

router = APIRouter()


@router.get("/service_in_hand/{portal_id}")
def access_portal(portal_id: int):
    return {"message": "service_in_hand portal"}
