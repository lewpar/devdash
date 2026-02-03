from fastapi import APIRouter
from system.diagnostic import get_ram_usage, get_ram_max

router = APIRouter()

@router.get("/memory")
def get_memory():
    return get_ram_usage()