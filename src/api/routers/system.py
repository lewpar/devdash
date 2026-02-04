from fastapi import APIRouter

import psutil

router = APIRouter(prefix="/system")

@router.get("/memory/usage")
def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "unit": "bytes",
        "free": memory.available,
        "used": memory.used,
        "total": memory.total
    }

@router.get("/disk/usage")
def get_disk_usage():
    disk = psutil.disk_usage("/")
    return {
        "unit": "bytes",
        "free": disk.free,
        "used": disk.used,
        "total": disk.total
    }

@router.get("/cpu/frequency")
def get_cpu_frequency():
    cpu = psutil.cpu_freq()
    return {
        "unit": "Mhz",
        "min": cpu.min,
        "max": cpu.max,
        "current": cpu.current
    }

@router.get("/cpu/usage")
def get_cpu_usage():
    cpu = psutil.cpu_percent(0.5)
    return {
        "unit": "%",
        "min": 0,
        "max": 1,
        "current": cpu
    }