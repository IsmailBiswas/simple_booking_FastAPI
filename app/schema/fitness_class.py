from sqlmodel import Field, SQLModel
from pydantic import EmailStr
import datetime

class FitnessClassBase(SQLModel):
  name: str = Field(index=True)
  class_time: datetime.datetime
  instructor: str

class FitnessClassPublic(FitnessClassBase):
  id: int
  booked_slot: int
  total_slot: int

class FitnessClassCreate(FitnessClassBase):
  total_slot: int

class FitnessClassUpdate(FitnessClassBase):
  name: str = Field(index=True)
  class_time: datetime.datetime
  instructor: str
  booked_slot: int
  total_slot: int

class BookingBase(SQLModel):
  client_name: str = Field(index=True)
  client_email: EmailStr = Field(index=True)
  class_id: int # TODO -> use slug

class BookingCreate(BookingBase):
  ...

class BookingPublic(BookingBase):
  booked_at: datetime.datetime

class BookingUpdate(BookingBase):
  ...
