from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/moves",
    tags=["moves"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Move])
def read_moves(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    moves = crud.get_moves(db, skip=skip, limit=limit)
    return moves


@router.get("/{move_title}", response_model=schemas.Move)
def read_move(move_title: int, db: Session = Depends(get_db)):
    db_move = crud.get_move_by_title(db, title=move_title)
    if db_move is None:
        raise HTTPException(status_code=404, detail="Move not found")
    return db_move
