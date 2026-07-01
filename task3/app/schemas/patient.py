from pydantic import BaseModel, Field
from typing import Optional

class PatientCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=120)
    condition: str = Field(..., min_length=1)
    risk_score: int = Field(..., ge=0, le=100)
    active: bool = Field(default=True)

class PatientPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=0, le=120)
    condition: Optional[str] = Field(None, min_length=1)
    risk_score: Optional[int] = Field(None, ge=0, le=100)
    active: Optional[bool]

class PatientRead(BaseModel):
    id: int
    name: str
    age: int
    condition: str
    risk_score: int
    active: bool
    
    model_config = {"from_attributes": True}