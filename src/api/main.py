from fastapi import FastAPI
from fastapi.middleware import cors

import routers.system

app = FastAPI()

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(cors.CORSMiddleware,
                   allow_origins=allowed_origins,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(routers.system.router)