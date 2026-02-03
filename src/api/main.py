from fastapi import FastAPI

import routers.memory

app = FastAPI()

app.include_router(routers.memory.router)