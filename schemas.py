from pydantic import BaseModel


class MoveBase(BaseModel):
    title: str
    power: int


class MoveCreate(MoveBase):
    pass


class Move(MoveBase):
    id: int

    class Config:
        orm_mode = True


class PokemonBase(BaseModel):
    name: str
    type: str


class PokemonCreate(PokemonBase):
    pass


class Pokemon(PokemonBase):
    id: int
    moves: list[Move] = []
    trainer_id: int

    class Config:
        orm_mode = True


class TrainerBase(BaseModel):
    name: str


class TrainerCreate(TrainerBase):
    pass


class Trainer(TrainerBase):
    id: int
    pokemons: list[Pokemon] = []

    class Config:
        orm_mode = True
