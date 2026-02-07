from fastapi import APIRouter

import psutil, time

router = APIRouter(prefix="/system", tags=["System"])

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
    disk = psutil.disk_usage(path="/")
    return {
        "unit": "bytes",
        "free": disk.free,
        "used": disk.used,
        "total": disk.total
    }

@router.get("/cpu")
def get_cpu_info():
    return {
        "frequency": get_cpu_frequency(),
        "usage": get_cpu_usage(),
        "cores": get_cpu_cores()
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
    usage = psutil.cpu_percent(interval=0.5)
    return {
        "unit": "%",
        "min": 0,
        "max": 100,
        "current": usage
    }

@router.get("/cpu/cores")
def get_cpu_cores():
    cores = psutil.cpu_count()
    return {
        "count": cores
    }

@router.get("/boot")
def get_boot_time():
    boot = psutil.boot_time()
    current_time = time.time()
    return {
        "unit": "seconds",
        "value": current_time - boot
    }
