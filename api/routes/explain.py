
from fastapi import APIRouter

router = APIRouter()

@router.post("/explain")
def explain():
    return {
        "status": "ok",
        "message": "DynamiCore explain endpoint active"
    }
