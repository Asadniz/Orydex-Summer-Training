from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=8)
    model_config = {
        "json_schema_extra":{
            "example":{
                "username": "asadniz",
                "password": "12345678"
            }
        }
    }


class UserLogin(BaseModel):
    username: str
    password: str
    model_config = {
        "json_schema_extra":{
            "example":{
                "username": "asadniz",
                "password": "12345678"
            }
        }
    }


class UserRead(BaseModel):
    id: int
    username: str
    model_config = {
        "json_schema_extra":{
            "example":{
                "username": "asadniz"
            }
        }
    }


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    model_config = {
        "json_schema_extra":{
            "example":{
                "access_token": "this is a secret key token"
            }
        }
    }
