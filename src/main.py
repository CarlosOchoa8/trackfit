"""
Module for the fastapi setup.
"""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

from src.routers import router

# app = FastAPI()
app = FastAPI(openapi_prefix="/trackfit_api")

#  Setup CORS Middleware

# app.mount("/media", StaticFiles(directory=statics), name="media")

# TODO: for production, remove the origins=["*"] and add the correct origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=router
)

@app.get("/")
def home():
    return {"Status": "Ok"}
