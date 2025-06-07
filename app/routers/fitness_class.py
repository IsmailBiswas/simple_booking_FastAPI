from fastapi import APIRouter, Query
from typing import Annotated
from app.database import DBSessionDep
from app.models import fitness_class
from sqlmodel import select

router = APIRouter()

# get all available classes
@router.get("/classes/", tags=["classes"], response_model=list[fitness_class.FitnessClassPublic])
async def read_fitnessclass(session: DBSessionDep, offset: int = 0,
  limit: Annotated[int, Query(le=100)] = 100):
    classes = session.exec(select(fitness_class.FitnessClass).offset(offset).limit(limit)).all()
    return classes

# adds new class
@router.post("/classes/", tags=["write_classess"], response_model=fitness_class.FitnessClassPublic)
async def write_fitnessclass(new_class: fitness_class.FitnessClassCreate , session: DBSessionDep):
    db_fitness_class = fitness_class.FitnessClass.model_validate(new_class)
    session.add(db_fitness_class)
    session.commit()
    session.refresh(db_fitness_class)
    return db_fitness_class

# get all booking by an email
@router.get("/booking/", tags=["booking"])
async def read_booking():
    return [{"username": "Rick"}, {"username": "Morty"}]

# book a class
@router.post("/book/", tags=["book"])
async def write_book():
    return [{"username": "Rick"}, {"username": "Morty"}]
