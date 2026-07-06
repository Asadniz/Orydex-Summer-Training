from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.database import get_session
from app.models.patient import Patient
from app.models.user import User
from app.schemas.patient import PatientCreate, PatientPatch, PatientRead
from app.auth import get_current_user


def audit_log(patient_id: int, action: str):
    print("Auditing: Patient id ", patient_id, " action ", action)


router = APIRouter(prefix="/patients", tags=["patients"])


@router.get(
    "/",
    status_code=200,
    summary="List all patients",
    description="Returns a list of all patients. Supports filtering by active status and condition, and pagination via limit and offset. Results can be sorted by any patient field using sort=field for ascending or sort=-field for descending.",
)
def get_patients(
    active: bool | None = None,
    condition: str | None = None,
    limit: int = 100,
    offset: int = 0,
    sort: str | None = None,
    db: Session = Depends(get_session),
):

    print("Listing all patients!")
    query = db.query(Patient)

    if active is not None:
        query = query.filter(Patient.active == active)
    if condition is not None:
        query = query.filter(Patient.condition == condition)
    if sort is not None:
        if sort.startswith("-"):
            query = query.order_by(desc(getattr(Patient, sort[1:])))
        else:
            query = query.order_by(asc(getattr(Patient, sort)))

    return query.offset(offset).limit(limit).all()


@router.get(
    "/{id}",
    status_code=200,
    summary="Get patient by ID",
    description="Returns a single patient by their ID. Returns 404 if the patient does not exist.",
)
def get_patient_from_id(id: int, db: Session = Depends(get_session)):
    print("Listing patient with id ", id, "!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.post(
    "/",
    response_model=PatientRead,
    status_code=201,
    summary="Create a new patient",
    description="Creates a new patient record. Requires authentication. Returns 422 on invalid data, 401 if unauthenticated.",
)
def create_patient(
    data: PatientCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):

    print("creating patient!")
    patient = Patient(**data.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    background_tasks.add_task(audit_log, patient.id, "CREATE")
    return patient


@router.put(
    "/{id}",
    response_model=PatientRead,
    status_code=200,
    summary="Fully update a patient",
    description="Replaces all fields of an existing patient record. All fields are required. Returns 404 if the patient does not exist, 401 if unauthenticated.",
)
def update_patient(
    id: int,
    data: PatientCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):

    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    for key, value in data.model_dump().items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    background_tasks.add_task(audit_log, patient.id, "FULL UPDATE")
    return patient


@router.patch(
    "/{id}",
    response_model=PatientRead,
    status_code=200,
    summary="Partially update a patient",
    description="Updates only the provided fields of an existing patient record. Returns 404 if the patient does not exist, 401 if unauthenticated.",
)
def partial_update_patient(
    id: int,
    data: PatientPatch,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):

    print("partially updating data of patient id ", id, "!")
    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    background_tasks.add_task(audit_log, patient.id, "PARTIAL UPDATE")
    return patient


@router.delete(
    "/{id}",
    status_code=204,
    summary="Delete a patient",
    description="Permanently deletes a patient record by ID. Returns 404 if the patient does not exist, 401 if unauthenticated.",
)
def delete_patient(
    id: int,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):

    patient = db.query(Patient).filter(Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    background_tasks.add_task(audit_log, patient.id, "DELETE")
    db.delete(patient)
    db.commit()
    return {"message": "Patient has been deleted"}
