from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

sqlite_file_name = "database.db"
sqlite_url = os.getenv("database_url")

connect_args = {"check_same_thread": False} if sqlite_url.startswith("sqlite") else {}
engine = create_engine(sqlite_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
