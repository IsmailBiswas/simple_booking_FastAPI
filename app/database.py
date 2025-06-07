from typing import Annotated
from sqlmodel import create_engine, Session
from fastapi import Depends
from app.config import settings

sqlite_url = settings.database_url

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

DBSessionDep = Annotated[Session, Depends(get_session)]
