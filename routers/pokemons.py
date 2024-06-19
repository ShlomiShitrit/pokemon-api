from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/pokemons",
    tags=["pokemons"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pokemons = crud.get_pokemons(db, skip=skip, limit=limit)
    return pokemons


@router.get("/{pokemon_name}", response_model=schemas.Pokemon)
def read_pokemon(pokemon_name: str, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_name(db, name=pokemon_name)
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return db_pokemon


@router.post("/{pokemon_id}/moves/", response_model=schemas.Move)
def create_move_for_pokemon(
    pokemon_id: int, move: schemas.MoveCreate, db: Session = Depends(get_db)
):
    return crud.create_pokemon_move(db, move=move, pokemon_id=pokemon_id)
