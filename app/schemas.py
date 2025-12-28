from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    name: str = Field(
        ...,
        #impede nomes vazios ou invalidos
        min_length=3,
        max_length=100,
        description="Nome do usuário (mínimo 3 caracteres)"
    )
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
