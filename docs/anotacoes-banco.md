**Criando Banco de dados gesta-pequenos-negocios:**

1º
 - Crio um ambiente virtual e depois ativo: python -m venv venv -> .\venv\Scripts\Activate.ps1

- Instalo as bibliotecas: pip install sqlalchemy sqlmodel psycopg2-binary python-dotenv
# OBS: Não atualzei o requirements.txt com pip freeze > requirements.txt, o arquivo ainda não está na branch principal.

2º 
- Criei a pasta .env/ na raiz do projeto e adicionei a string de conexão do projeto do Supabase
# OBS: o banco postgres já existe pronto no Supabase. Quando rodar Base.metadata.create_all(bind=engine) no main.py, o SQLAlchemy vai criar a tabela produtos dentro desse banco automaticamente.

3º 
- Crio dentro da pasta backend/ o arquivo database.py/ que vai ler e se conectar com o banco de dados

4º 
- Dentro da pasta backend/, adiciono o arquivo models.py para preencher a tabela, define o nome da tabela, cria o campo id.

5º 
- Dentro da pasta backend/, o arquivo schemas.py para criar um produto e receber uma resposta 

6º 
- Criei a pasta routers/ dentro de backend/ e dentro dela crie produtos.py/ permite organizar as rotas em arquivos separados

7º 
- Editei o arquivo backend/main.py para incluir importa as rotas de produtos, cria todas as tabelas no bancoautomaticamente (se não existirem) e registrar as rotas de produtos.
# OBS: tive que adicionar um arquivo __init__.py/ na pasta routers/ para importar os produtos para o arquivo main.py/

8º 
- Ativo o uvicorn main_app --reload para testar as funções POST /produtos/ criar produtos (que está funcionando)e a função GET /produtos/ listar produtos (que está funcionando também)