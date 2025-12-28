from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.core.security import hash_password
from app.schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica se email já existe
    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    db_user = models.User(
        email=user.email,
        name=user.name,
        password=hash_password(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "id": db_user.id,
        "email": db_user.email,
        "name": db_user.name,
    }
