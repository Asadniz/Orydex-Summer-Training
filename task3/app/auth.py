import jwt
import os
from fastapi import Depends, HTTPException
from app.models.user import User
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from app.database import get_session
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("secret_key")

algorithm = "HS256"
token_expiry_seconds = 1800

def create_access_token(username: str):
    to_encode = {"username": username}
    expire = datetime.now() + timedelta(seconds=token_expiry_seconds)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username = payload.get("username")
        if username is None:
            return None
        return username
    except jwt.PyJWTError:
        return None
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="invalid or expired token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="user not found")
    return user