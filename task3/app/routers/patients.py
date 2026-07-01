from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_session
from app.models.patient import Patient
from app.models.user import User
from app.schemas.patient import PatientCreate, PatientPatch, PatientRead
from app.auth import get_current_user

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/", status_code=200)
def get_patients(active: bool | None = None,
    condition: str | None = None,
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_session)):
    
    print ("Listing all patients!")
    query = db.query(Patient)
    if active:
        if condition:
            query = db.query(Patient).filter(Patient.active == active).filter(Patient.condition == condition)        
        else:
            query = db.query(Patient).filter(Patient.active == active)
    elif condition:
        query = db.query(Patient).filter(Patient.condition == condition)
    
    return query.offset(offset).limit(limit).all()

@router.get("/{id}", status_code=200)
def get_patient_from_id(id: int, db: Session = Depends(get_session)):
    print ("Listing patient with id ", id, "!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.post("/", response_model=PatientRead, status_code=201)
def create_patient(data: PatientCreate,
                    current_user: User = Depends(get_current_user),
                    db: Session = Depends(get_session)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Please login first")
    print ("creating patient!")
    patient = Patient(**data.model_dump())
    if len(patient.name) < 1 or len(patient.name) > 120 or patient.age < 0 or patient.age > 120 or len(patient.condition) < 1 or patient.risk_score < 0 or patient.risk_score > 100:
        raise HTTPException(status_code=422, detail="Invalid data")
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.put("/{id}", response_model=PatientRead, status_code=200)
def update_patient(id: int, data: PatientCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_session)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Please login first")
    print ("fully updating data of patient id ", id, "!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found") 
    for key, value in data.model_dump().items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

@router.patch("/{id}", response_model=PatientRead, status_code=200)
def partial_update_patient(id: int,
                           data: PatientPatch,
                           current_user: User = Depends(get_current_user),
                           db: Session = Depends(get_session)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Please login first")
    print ("partially updating data of patient id ", id, "!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found") 
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

@router.delete("/{id}", status_code=204)
def delete_patient(id: int,
                   current_user: User = Depends(get_current_user),
                   db: Session = Depends(get_session)):
    if not current_user:
        raise HTTPException(status_code=403, detail="Please login first")
    print ("deleting patient from records!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
            raise HTTPException(status_code=404, detail="patient not found") 
    db.delete(patient)
    db.commit()
    return {"message": "Patient has been deleted"}
    