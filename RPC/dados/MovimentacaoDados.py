from datetime import datetime
import json

from fastapi.encoders import jsonable_encoder
from negocio.Pessoa import Pessoa
from negocio.GeradorUUID import GeradorUUID
from negocio.Lista import Lista
from negocio.Item import Item

class MovimentacaoDados:

    gerador = GeradorUUID()

    # Cria uma Pessoa e a retorna
    @staticmethod
    def addPessoa(nome):
        pessoa = Pessoa(id=MovimentacaoDados.gerador.gerarUUID(), nome=nome, lista=None)
        return pessoa
    
    # Cria uma lista e a retorna
    @staticmethod
    def criaLista():
        lista = Lista(id=MovimentacaoDados.gerador.gerarUUID(), dataCriacao=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return lista
    
    # Cria item e o retorna 
    @staticmethod
    def addItem(descricao, qtd, preco):
        item = Item(id=MovimentacaoDados.gerador.gerarUUID(),descricao=descricao, qtd=qtd, preco=preco)
        return item
    
    # @staticmethod
    # def removeItem(lista, id):
    #     lista.remove(id)
    #     novaLista = lista
    #     return novaLista

    # Remoção não funcional
    @staticmethod
    def removeItem(lista, des):
        lista.remove(des)
        novaLista = lista
        return novaLista
    
    # Grava dados - Pessoa
    @staticmethod
    def gravar(pessoa):
         # Converte o objeto Pydantic em um dicionário e serializa para JSON
        pessoa_dict = jsonable_encoder(pessoa)
        pessoa_json = json.dumps(pessoa_dict, indent=4)

        with open('pessoa.json', 'w') as file:
            file.write(pessoa_json)
        
