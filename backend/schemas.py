from pydantic import BaseModel

# Schema para CRIAR um produto (dados que o cliente envia)
class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    quantidade_estoque: int = 0

# Schema para RESPOSTA (dados que a API retorna, incluindo o id)
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    quantidade_estoque: int

    class Config:
        from_attributes = True  # Permite converter objeto do banco em JSON
