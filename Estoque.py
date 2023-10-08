import requests
import json
#import bd

client_id = 6879509485276765
client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
redirect_uri = "https://localhost:3000/"
access_token = "APP_USR-6879509485276765-100812-fa64bc013100d27aecf8d18a777f913c-323433124"

def PuxarEstoqueML(ID_Produto):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    dados_produto = resposta.json()
    EstoqueML = dados_produto["initial_quantity"]
    variations = dados_produto.get("variations")
    return EstoqueML

def AtualizarEstoqueML(ID_Produto, novo_estoque):
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
        print(f"Erro ao Atualizar o estoque. Status Code: {resposta.status_code}")
        print("Mensagem de Erro:", resposta.json())

def AtualizarEstoqueML_ComVariacao(ID_Produto, novo_estoque):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print(f"Não foi possível obter os dados do produto ID {ID_Produto}")
        return
    
    dados_produto = resposta.json()
    variations = dados_produto.get("variations")
    
    if not variations:
        print("Não há variações para atualizar.")
        return

    listing_type_id = dados_produto.get("listing_type_id")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    updated_variations = []
    
    for variation in variations:
        id = variation["id"]
        price = variation["price"]
        updated_variation = {
            "available_quantity": novo_estoque,
            "id": id
        }
        updated_variations.append(updated_variation)
    
    data = {
        "variations": updated_variations
    }

    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.put(url, headers=headers, json=data)

    if resposta.status_code == 200 or resposta.status_code == 201:
        print(f"Estoque de todas as variações atualizado com sucesso!")
    else:
        print(f"Erro ao atualizar o estoque. Status Code: {resposta.status_code}")
        print("Mensagem de Erro:", resposta.json())

def atualizar_estoque(ID_Produto, novo_estoque):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    dados_produto = resposta.json()
    variations = dados_produto.get("variations")
    if not variations:
        AtualizarEstoqueML(ID_Produto, novo_estoque)
    else:
        AtualizarEstoqueML_ComVariacao(ID_Produto, novo_estoque)

# Martelo: MLB3470037325 
# Relógios: MLB4102962668

ID_Produto = "MLB3470037325"
novo_estoque = 13
#ID_Vendedor = input("ID do vendedor: ")
           
#AtualizarEstoqueML_ComVariacao(ID_Produto, novo_estoque)
#AtualizarEstoqueML(ID_Produto, novo_estoque)
#PuxarEstoqueML(ID_Produto)

atualizar_estoque(ID_Produto, novo_estoque)