import uuid

# Classe Item contendo ID, Descrição, Qtd e Preço

class Item:

    def __init__(self, id=None, descricao=None, qtd=0, preco=0.0): 
        self.id = id if id else uuid.uuid4()
        self.descricao = descricao
        self.qtd = qtd
        self.preco = preco

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getQtd(self):
        return self.qtd

    def setQtd(self, qtd):
        self.qtd = qtd

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
