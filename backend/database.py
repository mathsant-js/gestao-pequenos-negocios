from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

# Carrega o .env da raiz do projeto, independentemente da pasta atual.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Pega a URL do banco do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL nao foi definida. Copie .env.example para .env e "
        "preencha a URL de conexao do banco."
    )

# Cria o "motor" de conexão com o banco
engine = create_engine(DATABASE_URL)

# Fabrica de sessões — cada requisição terá sua própria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para todos os nossos modelos (tabelas)
Base = declarative_base()

# Função geradora de sessão para injeção de dependência no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
