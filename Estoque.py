import requests
import json
#import bd

client_id = 6879509485276765
client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
redirect_uri = "https://localhost:3000/"
access_token = "APP_USR-6879509485276765-100514-88337319187d9e5083560e2360d8e0f0-323433124"

def atualizar(ID_Produto, novo_estoque):
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

def FecharAnuncioML(ID_Produto):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "status": "closed"
    }

    resposta = requests.put(url, headers=headers, json=data)

    if resposta.status_code == 200:
        print(f"Produco fechado com sucesso para permitir o reanúncio com o novo estoque.")
    else:
        print(f"Não foi possível atualizar o status do produto")
        print(resposta.status_code)

def atual_soldQuantity0(ID_Produto, novo_estoque):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    dados_produto = resposta.json()

    if resposta.status_code == 200:
        url = f"https://api.mercadolibre.com/items/{ID_Produto}/relist"
        listing_type_id = dados_produto.get("listing_type_id")
        price = dados_produto.get("price")

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "price": price,
            "quantity": novo_estoque,
            "listing_type_id": listing_type_id
        }

        resposta = requests.post(url, headers=headers, json=data)
        ID_Produto = resposta.json()
        ID_Produto = ID_Produto['id']
        return ID_Produto
    else:
        print(f"Não foi possível obter os dados do produto ID {ID_Produto}")

ID_Produto = "MLB3468877753"
novo_estoque = int(22)
#novo_status = input("Novo status: ")
#ID_Vendedor = input("ID do vendedor: ")

#atualizar_status_ML(ID_Produto, novo_status)
#atual(ID_Produto, novo_estoque)
#atual_soldQuantity0(ID_Produto)

url = f"https://api.mercadolibre.com/items/{ID_Produto}"
resposta = requests.get(url)
dados_produto = resposta.json()
sold_quantity = dados_produto.get("sold_quantity")

def atualizar_estoque(ID_Produto, novo_estoque):
    if sold_quantity == 0:
        FecharAnuncioML(ID_Produto)
        atual_soldQuantity0(ID_Produto, novo_estoque)
        print("Estoque atualizado com sucesso!")

atualizar_estoque(ID_Produto, novo_estoque)