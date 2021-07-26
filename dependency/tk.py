from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError,jwt
SECRET_KEY = "3aa3cf861837ce3e2859d502a2d77fb6bbb4d8d961b495cf8fcf23a6d4f42e1f"
#for secret key use cmd "openssl rand -hex 32"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 120


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY , algorithm=ALGORITHM)
    return encoded_jwt
