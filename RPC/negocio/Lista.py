import uuid
from datetime import datetime

# Classe Lista contento id, lista de itens, data de criação, valor total e quantidade total + métodos de remoção e adição

class Lista:
    
    def __init__(self, id=None, listaItens=None, dataCriacao=None, valorTotal=0.0, qtdTotalItens=0):
        self.id = id if id else uuid.uuid4()
        self.listaItens = listaItens if listaItens else []
        self.dataCriacao = dataCriacao if dataCriacao else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.valorTotal = valorTotal
        self.qtdTotalItens = qtdTotalItens

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getListaItens(self):
        return self.listaItens

    def setListaItens(self, listaItens):
        self.listaItens = listaItens

    def getDataCriacao(self):
        return self.dataCriacao

    def setDataCriacao(self, dataCriacao):
        self.dataCriacao = dataCriacao

    def getValorTotal(self):
        return self.valorTotal

    def setValorTotal(self, valorTotal):
        self.valorTotal = valorTotal

    def getQtdTotalItens(self):
        return self.qtdTotalItens

    def setQtdTotalItens(self, qtdTotalItens):
        self.qtdTotalItens = qtdTotalItens

    def add(self, item):
        for existeItem in self.listaItens:
            if existeItem.getId() == item.getId():
                return False
        self.listaItens.append(item)
        return True

    def remove(self, uuidItem):
        for item in self.listaItens:
            if str(item.getId()) == uuidItem:
                self.listaItens.remove(item)
                return True
        return False