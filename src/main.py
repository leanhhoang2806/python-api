from fastapi import FastAPI
from src.routers.router import router


app = FastAPI()

app.include_router(router)
