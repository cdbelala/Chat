from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..controllers.auth_controller import register

router = APIRouter()

class SignUpRequest(BaseModel):
    email: str
    password: str

class TokenRequest(BaseModel):
    idToken: str

# Sign-up endpoint
@router.post("/signup")
async def signup(request: SignUpRequest):
    return register(request.email, request.password)