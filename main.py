from fastapi import FastAPI

from . import models
from .database import engine
from .routers import pokemons, trainers, moves


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(trainers.router)
app.include_router(pokemons.router)
app.include_router(moves.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
