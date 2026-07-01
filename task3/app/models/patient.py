from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    condition = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    risk_score = Column(Integer)
    creation_time = Column(DateTime, default=datetime.now)