import json
from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from MovimentacaoDados import MovimentacaoDados
from Models import PessoaInput
from Models import ItemDetails
from Models import PessoaModel

dadosAPI = FastAPI() # Instância da API de dados

@dadosAPI.get("/") # Link
def home(): # Função que vai rodar
     return "Trabalhando com dados.."

# Cria a Pessoa e já vincula a uma lista vazia
@dadosAPI.post("/postPessoa/") 
def addPessoa(nome: PessoaInput):
     pessoa = MovimentacaoDados.addPessoa(nome)
     lista = MovimentacaoDados.criaLista()
     pessoa.setLista(lista)
     return pessoa

# Adiciona itens na lista e vincula a Pessoa
@dadosAPI.post("/postItem/")
async def addItem(pessoa: PessoaModel, itens: List[ItemDetails]):
    for item_details in itens:
        item = MovimentacaoDados.addItem(item_details.descricao, item_details.qtd, item_details.preco)
        pessoa.lista.listaItens.append(item)
    return pessoa

# Gravação de dados no formato JSON
@dadosAPI.post("/gravaPessoa/") # Link
def gravaPessoa(pessoa: PessoaModel): # Função que vai rodar
     MovimentacaoDados.gravar(pessoa)
     return pessoa


