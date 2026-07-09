"""Test fixtures for MSP Dashboard API."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.app import Base, get_db, app


@pytest.fixture
def db_session():
    """Create a fresh in-memory SQLite database for each test."""
    engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    import os
    os.remove("./test.db")