"""
Module for the fastapi setup.
"""

from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError, ValidationException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

# from fastapi.staticfiles import StaticFiles
from src.config.core import core_settings
from src.middlewares.exceptions import validation_request_exception_handler
from src.routers import router


app = FastAPI(root_path="/trackfit_api")

#  Setup CORS Middleware

# app.mount("/media", StaticFiles(directory=statics), name="media")

# TODO: for production, remove the origins=["*"] and add the correct origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=core_settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(exc_class_or_status_code=RequestValidationError, handler=validation_request_exception_handler)

app.include_router(
    router=router
)

@app.get("/")
def home():
    return {"Status": "Ok"}
