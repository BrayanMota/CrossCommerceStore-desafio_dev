from extract.api import extract_router
from transform.api import transform_router 
from load.api import load_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(extract_router)
app.include_router(transform_router)
app.include_router(load_router)