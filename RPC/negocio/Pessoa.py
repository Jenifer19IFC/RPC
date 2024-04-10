import uuid

#  Classe Pessoa contendo id, nome e lista

class Pessoa:

    def __init__(self, id=None, nome=None, lista=None):
        self.id = id if id else uuid.uuid4()
        self.nome = nome
        self.lista = lista

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getLista(self):
        return self.lista

    def setLista(self, lista):
        self.lista = lista
