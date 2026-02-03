import psutil

def get_ram_max():
    mem = psutil.virtual_memory()
    return mem.total

def get_ram_usage():
    mem = psutil.virtual_memory()
    return mem.free