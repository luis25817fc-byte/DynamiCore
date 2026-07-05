from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    nums = data.get("system", [])
    return {
        "status": "ok",
        "sum": sum(nums),
        "avg": sum(nums)/len(nums) if nums else 0
    }
