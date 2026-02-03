from fastapi import FastAPI

import routers.system

app = FastAPI()

app.include_router(routers.system.router)