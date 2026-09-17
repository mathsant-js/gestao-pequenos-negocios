from fastapi import FastAPI
from database import engine, Base
from routers import produtos  # importa as rotas de produtos

# Cria todas as tabelas no banco automaticamente (se não existirem)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestão de Pequenos Negócios",
    description="API para gerenciamento de estoque",
    version="1.0.0"
)

# Rota inicial (já estava aqui)
@app.get("/")
def inicio():
    return {
        "mensagem": "Servidor FastAPI funcionando!"
    }

# Registra as rotas de produtos
app.include_router(produtos.router)
