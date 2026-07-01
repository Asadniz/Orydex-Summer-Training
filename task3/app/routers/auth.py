from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserRead, UserLogin, Token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.user import User
from pwdlib import PasswordHash
from app.database import get_session
from app.auth import create_access_token




router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_session)):
    temp = db.query(User).filter(User.username == data.username).first()
    if temp:
        raise HTTPException(status_code=409, detail="username already in use")
    
    password_hash = PasswordHash.recommended()
    Hash_value = password_hash.hash(data.password)
    user = User(username = data.username, hashed_password=Hash_value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{id}", response_model=UserRead, status_code=200)
def get_user(id: int, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user

@router.post("/token", response_model=Token, status_code=200)
def authenticate(input_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    user_data = db.query(User).filter(User.username == input_data.username).first()
    if not user_data:
        raise HTTPException(status_code=401, detail="invalid username or password")
    if not PasswordHash.verify(input_data.password, user_data.hashed_password):
        raise HTTPException(status_code=401, detail="invalid username or password")
    
    token = create_access_token(user_data.username)
    return {"message": "login successful", "token": token, "token_type": "bearer"}