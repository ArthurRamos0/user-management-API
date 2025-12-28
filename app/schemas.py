from pydantic import BaseModel, EmailStr, Field, ConfigDict

# Base usado para UserCreate e UserResponse
class UserBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nome do usuário (mínimo 3 caracteres)"
    )
    email: EmailStr

# Para criação de usuário
class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=72,  # 👈 IMPORTANTE
        description="Senha do usuário (máx 72 caracteres)"
    )


# Para resposta ao cliente
class UserResponse(UserBase):
    id: int

    # Configuração Pydantic v2
    model_config = ConfigDict(from_attributes=True)
