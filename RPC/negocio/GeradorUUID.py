import uuid

class GeradorUUID:
    
    # Gera id para os Objetos
    @staticmethod
    def gerarUUID():
        return uuid.uuid4()
