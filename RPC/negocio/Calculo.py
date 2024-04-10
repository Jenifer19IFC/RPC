class Calculo:

    # Calcula o valor total e quantidade total de itens na lista
    @staticmethod
    def calcular_totais(lista_itens):
        valor_total = 0
        qtd_total_itens = 0

        for item in lista_itens:
            valor_total += item.preco * item.qtd
            qtd_total_itens += item.qtd

        return valor_total, qtd_total_itens
