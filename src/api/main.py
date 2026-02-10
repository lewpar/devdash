from fastapi import FastAPI
from fastapi.middleware import cors

from routers.system import router as system_router
from api.routers.containers import router as containers_router

app = FastAPI()

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(cors.CORSMiddleware,
                   allow_origins=allowed_origins,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(system_router)
app.include_router(containers_router)