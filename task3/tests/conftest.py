# Present so pytest adds this project directory to sys.path, which lets the
# tests import the application package with `from app.main import app`
# regardless of how pytest is invoked.

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_session

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    app.dependency_overrides[get_session] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_get_session():
    from app.database import get_session
    gen = get_session()
    db = next(gen)
    assert db is not None
    try:
        next(gen)
    except StopIteration:
        pass