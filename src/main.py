"""
Module for the fastapi setup.
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()

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

@app.get("/")
def home():
    return "Oka"
