import json
import httpx
import asyncio
from negocio.GeradorUUID import GeradorUUID

gerador = GeradorUUID()

# Boas-vindas
print('Seja bem-vindo (a)!\n'
    'Processo de utilização do sistema:\n'
    '- Cadastrar usuário único\n- Criar lista de compras\n- Visualizar lista de compras\n- Calcular valor total da lista\n\n')

# Cria Pessoa e já vincular a uma lista vazia 
nome = input("Digite seu nome: ")

# Requisição para criar Pessoa, retornando a mesma 
async def post_pessoa(nome):
    url = "http://localhost:8000/postPessoa/"
    data = {"nome": nome}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())
        return response.json()
    
pessoa = asyncio.run(post_pessoa(nome))

idPessoa = pessoa['id']
nome = pessoa['nome']['nome']
lista = pessoa['lista'] 
#  ------------------------------------------------ ------------------------

# Adição de itens na lista
print('\n# Adicionando itens na lista...\n')

itens = []

while True: # Solicitação de dados ao usuário
    descricao = input("Digite a descrição: ")
    qtd = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    
    item = {
        "id": str(gerador.gerarUUID()),
        "descricao": descricao,
        "qtd": qtd,
        "preco": preco
    }
    itens.append(item)
    
    continuar = input("1 - Continuar\n2 - Parar\nDigite sua escolha: ")
    
    if continuar == '2':
        break

# Requisição à API de dados para adicionar item.
# Função retorna a Pessoa com os itens na lista
async def postItem(pessoa, itens):
    url = "http://localhost:8000/postItem/"
    payload = {
        "pessoa": {
            "id": pessoa['id'],
            "nome": {"nome": pessoa['nome']['nome']},
            "lista": {
                "id": pessoa['lista']['id'],
                "listaItens": [],
                "dataCriacao": pessoa['lista']['dataCriacao'],
                "valorTotal": pessoa['lista']['valorTotal'],
                "qtdTotalItens": pessoa['lista']['qtdTotalItens']
            }
        },
        "itens": itens
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()

pessoa = asyncio.run(postItem(pessoa, itens))
# print(pessoa)

def listarTudo(pessoa):
    print(f"\n ----------- LISTAGEM --------------")
    print(f"ID da Pessoa: {pessoa['id']}")
    print(f"Nome: {pessoa['nome']['nome']}")
    print("\nLista de Compras:")
    print(f"ID da Lista: {pessoa['lista']['id']}")
    print(f"Data de Criação: {pessoa['lista']['dataCriacao']}")
    print(f"Valor Total: {pessoa['lista']['valorTotal']}")
    print(f"Quantidade Total de Itens: {pessoa['lista']['qtdTotalItens']}")
    print("\nItens:")
    print(f"- Descrição -> Quantidade -> Preço")
    for item in pessoa['lista']['listaItens']:
        print(f"- {item['descricao']} -> {item['qtd']} -> {item['preco']} R$")

    print(f" ----------- [FIM LISTAGEM] --------------")

listarTudo(pessoa)

# Requisição de cálculos para a API de negócios - soma total e quantidade total de itens na lista
# Retorna a pessoa os atributos atualizados
async def fazerCalculos(pessoa):
    url = "http://localhost:8001/calculos/"
    # Ajustando o payload para corresponder ao esperado pelo servidor
    payload = {
        "id": pessoa['id'],
        "nome": {"nome": pessoa['nome']['nome']},
        "lista": {
            "id": pessoa['lista']['id'],
            "listaItens": pessoa['lista']['listaItens'],
            "dataCriacao": pessoa['lista']['dataCriacao'],
            "valorTotal": pessoa['lista']['valorTotal'],
            "qtdTotalItens": pessoa['lista']['qtdTotalItens']
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()

pessoa = asyncio.run(fazerCalculos(pessoa))

# Passa como parâemtro a versão final da Pessoa e grava os dados no JSON
async def gravaPessoa(pessoa):
    url = "http://localhost:8000/gravaPessoa/"
    payload = {  # Ajustado o payload para corresponder ao esperado pelo servidor - PessoaModel
        "id": pessoa['id'],
        "nome": {"nome": pessoa['nome']['nome']},
        "lista": {
            "id": pessoa['lista']['id'],
            "listaItens": pessoa['lista']['listaItens'],
            "dataCriacao": pessoa['lista']['dataCriacao'],
            "valorTotal": pessoa['lista']['valorTotal'],
            "qtdTotalItens": pessoa['lista']['qtdTotalItens']
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()

pessoa = asyncio.run(gravaPessoa(pessoa))
print('\nGRAVADO -->>>', pessoa)