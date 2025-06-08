from fastapi import APIRouter, Query, HTTPException
from typing import Annotated
from pydantic import EmailStr
from app.database import DBSessionDep
from app.models import fitness_class as fitness_class_model
from app.schema import fitness_class as fitness_class_schema
from sqlmodel import select

router = APIRouter()

# get all available classes
@router.get("/classes/", tags=["classes"], response_model=list[fitness_class_schema.FitnessClassPublic])
async def read_fitnessclass(session: DBSessionDep, offset: int = 0,
  limit: Annotated[int, Query(le=100)] = 100):
    classes = session.exec(select(fitness_class_model.FitnessClass).offset(offset).limit(limit)).all()
    return classes

# adds new class
@router.post("/classes/", tags=["write_classess"], response_model=fitness_class_schema.FitnessClassPublic)
async def write_fitnessclass(new_class: fitness_class_schema.FitnessClassCreate , session: DBSessionDep):
    db_fitness_class = fitness_class_model.FitnessClass.model_validate(new_class)
    session.add(db_fitness_class)
    session.commit()
    session.refresh(db_fitness_class)
    return db_fitness_class


# get all booking by an email
@router.get("/booking/", tags=["booking"], response_model=list[fitness_class_schema.BookingPublic])
async def read_booking(client_email: EmailStr,
  session: DBSessionDep,
  offset: int = 0,
  limit: Annotated[int, Query(le=100)] = 100):
    db_booking = session.exec(
      select(fitness_class_model.Booking).where(fitness_class_model.Booking.client_email == client_email).offset(offset).limit(limit)
    ).all()
    return db_booking

# book a class
@router.post("/book/", tags=["book"], response_model=fitness_class_schema.BookingPublic)
async def write_book(book: fitness_class_schema.BookingCreate, session: DBSessionDep):
  with session.begin_nested():
    db_booking = fitness_class_model.Booking.model_validate(book)
    # Lock the row for update
    req_class = session.exec(
      select(fitness_class_model.FitnessClass).where(fitness_class_model.FitnessClass.id == db_booking.class_id)
      .with_for_update()
    ).first()

    if not req_class:
      raise HTTPException(status_code=404, detail="Class not found")

    if req_class.booked_slot >= req_class.total_slot:
      raise HTTPException(status_code=409, detail="No more slot is available")

    req_class.booked_slot += 1
    session.add(req_class)
    session.add(db_booking)
    return db_booking
