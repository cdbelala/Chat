from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..controllers.auth_controller import register
from services.logging_service import LoggingService
from dotenv import load_dotenv
import os
load_dotenv()

router = APIRouter()

# admin credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "My_pass563")


# Define Pydantic model for the login data
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    if request.username == ADMIN_USERNAME and request.password == ADMIN_PASSWORD:
        # Return success message or token
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


#class SignUpRequest(BaseModel):
    email: str
    password: str

#class TokenRequest(BaseModel):
    idToken: str

# Sign-up endpoint
#@router.post("/signup")
#async def signup(request: SignUpRequest):
    return register(request.email, request.password)