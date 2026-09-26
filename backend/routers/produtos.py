from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models, schemas

# permite organizar as rotas em arquivos separados.
router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

# POST /produtos — Cria um novo produto no banco
@router.post("/", response_model=schemas.ProdutoResponse, status_code=201)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    # Cria o objeto do modelo (ainda não salvo)
    novo_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco,
        quantidade_estoque=produto.quantidade_estoque
    )
    db.add(novo_produto)       # Prepara para salvar
    db.commit()                # Salva no banco (como um "Ctrl+S")
    db.refresh(novo_produto)   # Atualiza o objeto com dados do banco (ex: o id gerado)
    return novo_produto

# GET /produtos — Lista todos os produtos do banco
@router.get("/", response_model=list[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models.Produto).all()
    return produtos

# GET /produtos/{id} — Busca um produto específico
@router.get("/{produto_id}", response_model=schemas.ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
