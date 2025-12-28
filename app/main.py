from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database import engine
from app import models
from app.routes import users, auth
from app.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    internal_exception_handler,
)

# Cria tabelas no banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Registro dos handlers globais
app.add_exception_handler(
    StarletteHTTPException, http_exception_handler
)
app.add_exception_handler(
    RequestValidationError, validation_exception_handler
)
app.add_exception_handler(
    Exception, internal_exception_handler
)

# Rotas
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API rodando com tratamento global de erros 🚀"}
