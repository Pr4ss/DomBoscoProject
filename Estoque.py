import requests
#import bd

client_id = 6879509485276765
client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
redirect_uri = "https://localhost:3000/"
access_token = "APP_USR-6879509485276765-080916-4627ac8e652cbf9a510adf19235daba5-323433124"

def estoque_atualizado_ML(ID_Produto):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_produto = resposta.json()
        estoque_ML = dados_produto.get("initial_quantity", "Não disponível")
        print(f"Estoque atualizado: {estoque}")
    else:
        print(f"Não foi possível obter o estoque do produto ID {ID_Produto}")

def nome_atualizado_ML(ID_Produto):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_produto = resposta.json()
         nome_ML = dados_produto.get("title", "Não disponível")
        print(f"Nome atualizado: {nome_ML}")
    else:
        print(f"Não foi possível obter o título {ID_Produto}")

def estoque_total(ID_Vendedor):
    url = f'https://api.mercadolibre.com/sites/$MLB/search?seller_id=${ID_Vendedor}'
    headers = {'Authorization': f'Bearer {access_token}'}
    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        dados_vendedor = resposta.json()
        print(dados_vendedor)
    else:
        print(f'Não foi possível obter os itens do vendedor {ID_Vendedor}')
        print(resposta.status_code)

def atualizar_estoque(ID_Produto, novo_estoque):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "available_quantity": novo_estoque
    }

    resposta = requests.put(url, headers=headers, json=data)

    if resposta.status_code == 200:
        print(f"Estoque do produto atualizado para {novo_estoque}")
    else:
        print(f"Não foi possível atualizar o estoque do produto: {ID_Produto}")
        print(resposta.status_code)

def atualizar_status_ML(ID_Produto, Status):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "status":novo_status
    }

    resposta = requests.put(url, headers=headers, json=data)

    if resposta.status_code == 200:
        print(f"Status do produto atualizado para {novo_status}")
    else:
        print(f"Não foi possível atualizar o status do produto")
        print(resposta.status_code)


#ID_Produto = input("ID do produto: ")
#novo_estoque = int(input("Novo estoque: "))
#novo_status = input("Novo status: ")
#ID_Vendedor = input("ID do vendedor: ")

estoque_atualizado_ML(ID_Produto)
nome_atualizado_ML(ID_Produto)
atualizar_status_ML(ID_Produto, Status)

#estoque_ML
#nome_ML
