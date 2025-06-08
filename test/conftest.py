import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel import StaticPool
from app.database import get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session

    app.dependency_overrides[get_session] = get_session_override  
    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear() 
