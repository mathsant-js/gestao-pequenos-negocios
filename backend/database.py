from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a URL do banco do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

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
