from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .database import Base, engine
from .routes import users
from .exceptions import (
    http_exception_handler,
    validation_exception_handler,
    internal_exception_handler
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# 👉 REGISTRO DOS HANDLERS
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)

app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "API rodando com tratamento global de erros 🚀"}
