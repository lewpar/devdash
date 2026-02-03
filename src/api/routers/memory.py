from fastapi import APIRouter

import psutil

router = APIRouter(prefix="/system")

@router.get("/memory")
def get_memory():
    memory = psutil.virtual_memory()
    return {
        "free": memory.available,
        "used": memory.used,
        "total": memory.total
    }