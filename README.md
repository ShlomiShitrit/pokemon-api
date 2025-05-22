# 🧬 Pokémon API

A simple but powerful Pokémon-themed API built with **FastAPI** and **SQLAlchemy**. This project demonstrates how to build a RESTful API that manages Pokémon, Trainers, and Moves with proper relational mappings.

---

## 🎯 Features

- 🔥 FastAPI-powered async backend
- 📦 SQLAlchemy ORM with relationships
- 🧑‍🏫 Trainers can own multiple Pokémon
- 🧠 Pokémon can have multiple moves (many-to-many)
- ⚔️ Move sharing across different Pokémon
- 🧪 REST endpoints for CRUD operations

---

## 🏗️ Models Overview

### 🐱 Pokémon
- `id`: integer
- `name`: string (unique)
- `type`: string
- `trainer_id`: foreign key to `Trainer`

Relationships:
- Many-to-one with `Trainer`
- Many-to-many with `Move`

### 🧑 Trainer
- `id`: integer
- `name`: string (unique)

Relationships:
- One-to-many with `Pokemon`

### 💥 Move
- `id`: integer
- `title`: string (unique)
- `power`: integer

Relationships:
- Many-to-many with `Pokemon`

---

## 🔁 API Endpoints
Trainers

    GET /trainers – List all trainers

    GET /trainers/{id} – Get a trainer by ID

    POST /trainers – Create a new trainer

Pokémon

    GET /pokemons – List all Pokémon

    GET /pokemons/{name} – Get Pokémon by name

    GET /pokemons/trainer/{trainer_id} – List Pokémon owned by a specific trainer

    POST /trainers/{trainer_id}/pokemons – Create a Pokémon for a trainer

Moves

    GET /moves – List all moves

    GET /moves/{title} – Get a move by title

    GET /moves/pokemon/{pokemon_id} – Get moves known by a specific Pokémon

    POST /pokemons/{pokemon_id}/moves – Add a move to a Pokémon
