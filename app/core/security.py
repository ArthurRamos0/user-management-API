from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import hashlib

SECRET_KEY = "super-secret-key"  # mover para env depois
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# 🔐 HASH DE SENHA (blindado contra limite de 72 bytes)
def hash_password(password: str) -> str:
    # Converte para bytes e normaliza o tamanho
    password_bytes = password.encode("utf-8")
    password_sha = hashlib.sha256(password_bytes).hexdigest()

    # bcrypt recebe sempre um tamanho fixo
    return pwd_context.hash(password_sha)


# 🔎 VERIFICAÇÃO DE SENHA
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    password_sha = hashlib.sha256(
        plain_password.encode("utf-8")
    ).hexdigest()

    return pwd_context.verify(password_sha, hashed_password)


# 🎟️ CRIAÇÃO DE TOKEN JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
