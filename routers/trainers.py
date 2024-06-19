from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/trainers",
    tags=["trainers"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Trainer)
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer_by_name(db, name=trainer.name)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already Exists")
    return crud.create_trainer(db=db, trainer=trainer)


@router.get("/", response_model=list[schemas.Trainer])
def read_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainers = crud.get_trainers(db, skip=skip, limit=limit)
    return trainers


@router.get("/{trainer_id}", response_model=schemas.Trainer)
def read_trainer(trainer_id: int, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer(db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@router.post("/{trainer_id}/pokemons/", response_model=schemas.Pokemon)
def create_pokemon_for_trainer(
    trainer_id: int, pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)
):
    return crud.create_trainer_pokemon(db=db, pokemon=pokemon, trainer_id=trainer_id)
