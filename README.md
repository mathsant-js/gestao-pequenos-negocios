# 🏪 Gestão do Negócio — Backend API

API RESTful desenvolvida com **FastAPI** e **PostgreSQL** para gerenciamento de estoque e inventário.

## 🛠️ Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy / SQLModel
- Pytest

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Configurar o Ambiente Virtual
Bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

3. Instalar Dependências
Bash
pip install -r requirements.txt
4. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com as credenciais do seu banco:

Snippet de código
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco

5. Iniciar a API
Bash
uvicorn backend.main:app --reload
Acesse a documentação interativa em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

🧪 Executando os Testes Automatizados
Para rodar as suítes de teste com Pytest:

Bash
pytest