from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

<<<<<<< HEAD
from app.database import get_db
from app import models
from app.core.security import hash_password
from app.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica se email já existe
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
=======
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post(
    "/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verifica se o email já existe
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

>>>>>>> parent of 1c1b981 (correção de bugs e Autenticação JWT)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )

<<<<<<< HEAD
    # Cria usuário no banco
    db_user = models.User(
        email=user.email,
=======
    new_user = models.User(
>>>>>>> parent of 1c1b981 (correção de bugs e Autenticação JWT)
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

<<<<<<< HEAD
    # Retorna diretamente o objeto, FastAPI converte para UserResponse
    return db_user
=======
    return new_user
>>>>>>> parent of 1c1b981 (correção de bugs e Autenticação JWT)
