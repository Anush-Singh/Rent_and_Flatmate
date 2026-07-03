from fastapi import APIRouter
from app.schemas.user import UserRegister, UserLogin
from app.services.auth_service import hash_password
from app.services.jwt_service import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserRegister):
    hashed = hash_password(user.password)

    return {
        "message": "User Registered",
        "user": {
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "hashed_password": hashed
        }
    }


@router.post("/login")
def login(user: UserLogin):
    token = create_token({"email": user.email})

    return {
        "message": "Login Successful",
        "token": token
    }