import os
from datetime import datetime, timedelta
from typing import Any

import jwt
from passlib.context import CryptContext

JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-key-change-me")
JWT_ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def create_token(subject: str, ttl_minutes: int = 60 * 24 * 7) -> str:
    expires = datetime.utcnow() + timedelta(minutes=ttl_minutes)
    payload = {"sub": subject, "exp": expires}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> Any:
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
