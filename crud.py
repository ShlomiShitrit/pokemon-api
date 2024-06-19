from sqlalchemy.orm import Session

from . import models, schemas


def get_trainer(db: Session, trainer_id: int):
    return db.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(db: Session, name: str):
    return db.query(models.Trainer).filter(models.Trainer.name == name).first()


def get_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(db: Session, trainer: schemas.TrainerCreate):
    db_trainer = models.Trainer(name=trainer.name)
    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer


def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def get_pokemon_by_name(db: Session, name: str):
    return db.query(models.Pokemon).filter(models.Pokemon.name == name).first()


def get_pokemons_by_trainer(db: Session, trainer_id: int):
    return (
        db.query(models.Pokemon).filter(models.Pokemon.trainer_id == trainer_id).all()
    )


def create_trainer_pokemon(
    db: Session, pokemon: schemas.PokemonCreate, trainer_id: int
):
    db_pokemon = models.Pokemon(**pokemon.model_dump(), trainer_id=trainer_id)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


def get_moves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Move).offset(skip).limit(limit).all()


def get_move_by_title(db: Session, title: str):
    return db.query(models.Move).filter(models.Move.title == title).first()


def get_moves_by_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Move).filter(models.Move.pokemons.any(id=pokemon_id)).all()


def create_pokemon_move(db: Session, move: schemas.MoveCreate, pokemon_id: int):
    db_move = models.Move(**move.model_dump())
    db_pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()
    db_move.pokemons.append(db_pokemon)
    # db_pokemon.moves.append(db_move)
    
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move
