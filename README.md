🚀 User Management API

API REST desenvolvida com FastAPI para gerenciamento de usuários, aplicando boas práticas de backend, validações, tratamento global de erros e arquitetura organizada.

📌 Funcionalidades

✅ Criar usuário

✅ Listar usuários

✅ Buscar usuário por ID

✅ Validação de dados (nome, e-mail, etc.)

✅ Tratamento global de erros (400, 404, 500)

✅ Documentação automática com Swagger

🛠️ Tecnologias Utilizadas

Python 3.10+

FastAPI

Uvicorn

Pydantic

SQLite

SQLAlchemy

📂 Estrutura do Projeto
user-management-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── exceptions.py
│   └── routes/
│       └── users.py
│
├── venv/
├── requirements.txt
└── README.md

▶️ Como Executar o Projeto

1️⃣ Clonar o repositório
git clone https://github.com/ArthurRamos0/user-management-API.git

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar a aplicação
uvicorn app.main:app --reload

📖 Documentação da API

Após iniciar o projeto, acesse:

Swagger UI:
👉 http://127.0.0.1:8000/docs

Redoc:
👉 http://127.0.0.1:8000/redoc

🚨 Tratamento Global de Erros

A aplicação possui tratamento centralizado para:

400 – Erro de validação

404 – Recurso não encontrado

500 – Erro interno do servidor

Exemplo de resposta:

{
  "detail": "Erro interno no servidor"
}

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

Consolidar conhecimentos em FastAPI

Aplicar boas práticas de backend

Criar um projeto realista para portfólio júnior

📌 Próximos Passos (Roadmap)

🔐 Autenticação com JWT

🧪 Testes automatizados

🐳 Dockerização

📊 Paginação e filtros

👤 Autor

Arthur Ramos
Estudante de Análise e Desenvolvimento de Sistemas
Foco em Backend com Python

🔗 LinkedIn: https://www.linkedin.com/in/arthurramosdev/
🔗 GitHub: https://github.com/ArthurRamos0

