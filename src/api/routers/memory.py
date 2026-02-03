from fastapi import APIRouter
from system.diagnostic import get_ram_usage, get_ram_max, get_ram_free

router = APIRouter(prefix="/system")

class MemoryDetails:
    def __init__(self, used: int, max: int, free: int):
        self.used = used
        self.free = free
        self.max = max

@router.get("/memory")
def get_memory():
    return MemoryDetails(get_ram_usage(), get_ram_max(), get_ram_free())