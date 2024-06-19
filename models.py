from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

pokemon_move_association = Table(
    "pokemon_move",
    Base.metadata,
    Column("pokemon_id", Integer, ForeignKey("pokemons.id")),
    Column("move_id", Integer, ForeignKey("moves.id")),
)


class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    moves = relationship(
        "Move", secondary=pokemon_move_association, back_populates="pokemons"
    )
    trainers = relationship("Trainer", back_populates="pokemons")


class Move(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    power = Column(Integer, index=True)

    pokemons = relationship(
        "Pokemon", secondary=pokemon_move_association, back_populates="moves"
    )


class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    pokemons = relationship("Pokemon", back_populates="trainers")
