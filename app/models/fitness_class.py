from sqlmodel import Field
import datetime
from app.schema.fitness_class import FitnessClassBase, BookingBase

class FitnessClass(FitnessClassBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    total_slot: int
    booked_slot: int = 0

class Booking(BookingBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    booked_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
