from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "rentfinder_secret"
ALGORITHM = "HS256"


def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)