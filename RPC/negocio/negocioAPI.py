from fastapi import FastAPI
from Calculo import Calculo
from dados.Models import PessoaModel
from dados.MovimentacaoDados import MovimentacaoDados

negocioAPI = FastAPI() # Instância da API de negócios

@negocioAPI.get("/") # Link
def home(): # Função que vai rodar
     return "Trabalhando com negócio..."

# Realiza cálculos de valor total e quantidade total de itens
@negocioAPI.post("/calculos/") # Link
def calculos(pessoa: PessoaModel): # Função que vai rodar
     somaTotal, qtdTotal = Calculo.calcular_totais(pessoa.lista.listaItens)

     # Atribuição dos cálculos à pessoa
     pessoa.lista.valorTotal = somaTotal
     pessoa.lista.qtdTotalItens = qtdTotal

     return pessoa

