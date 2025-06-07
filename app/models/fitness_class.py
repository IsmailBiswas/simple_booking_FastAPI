from sqlmodel import Field, SQLModel
import datetime

class FitnessClassBase(SQLModel):
  name: str = Field(index=True)
  class_time: datetime.datetime
  instructor: str

class FitnessClass(FitnessClassBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    total_slot: int
    available_slot: int | None = None

class FitnessClassPublic(FitnessClassBase):
  id: int
  available_slot: int | None = None

class FitnessClassCreate(FitnessClassBase):
  total_slot: int

class FitnessClassUpdate(FitnessClassBase):
  name: str = Field(index=True)
  class_time: datetime.datetime
  instructor: str
  available_slot: int | None = None
  total_slot: int

class Booking(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    client_name: str = Field(index=True)
    client_email: int | None = Field(default=None, index=True)
    booked_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
