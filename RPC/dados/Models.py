from typing import List
from pydantic import BaseModel
import uuid

# Modelos pré-estruturados dos parâmetros

class PessoaInput(BaseModel):
    nome: str

class Item(BaseModel):
    descricao: str
    qtd: int
    preco: float

class Lista(BaseModel):
    id: uuid.UUID
    listaItens: List[Item]
    dataCriacao: str
    valorTotal: float
    qtdTotalItens: int

class PessoaModel(BaseModel):
    id: uuid.UUID
    nome: dict
    lista: Lista


class ItemDetails(BaseModel):
    id: uuid.UUID
    descricao: str
    qtd: int
    preco: float

class DescricaoItem(BaseModel):
    descricao: str
