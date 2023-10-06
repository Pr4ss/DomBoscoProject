import requests
import json
#import bd

client_id = 6879509485276765
client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
redirect_uri = "https://localhost:3000/"
access_token = "APP_USR-6879509485276765-100616-a26391450f7e0e40156a79c8d4b12e72-323433124"

def PuxarEstoqueML(ID_Produto):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    dados_produto = resposta.json()
    EstoqueML = dados_produto["initial_quantity"]

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
    dados_produto = resposta.json()
    variations = dados_produto.get("variations")
    quant_variations = len(variations)
    print(variations)

    if resposta.status_code == 200:
        url = f"https://api.mercadolibre.com/items/{ID_Produto}/relist"
        listing_type_id = dados_produto.get("listing_type_id")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        for variation in variations:
            id = variation["id"]
            price = variation["price"]
            data = {
                "listing_type_id": listing_type_id,
                "variations": [
                    {
                        "id": id,
                        "price": price,
                        "quantity": novo_estoque
                    }
                ]
            }
            url = f"https://api.mercadolibre.com/items/{id}"
            resposta = requests.put(url, headers=headers, json=data)
            print(id)
            if resposta.status_code == 201:
                print("Produto do ID {id} foi atualizado com sucesso!")
            else:
                print(f"Erro ao criar o anúncio. Status Code: {resposta.status_code}")
                print("Mensagem de Erro:", resposta.json())
        #return ID_Produto
    else:
        print(f"Não foi possível obter os dados do produto ID {ID_Produto}")

def atualizar_estoque(ID_Produto, novo_estoque):
    url = f"https://api.mercadolibre.com/items/{ID_Produto}"
    resposta = requests.get(url)
    dados_produto = resposta.json()
    sold_quantity = dados_produto.get("sold_quantity")
    if sold_quantity == 0:
        FecharAnuncioML(ID_Produto)
        upd_NoSales_NoVariations(ID_Produto, novo_estoque)

ID_Produto = "MLB3470037325"
novo_estoque = int(27)
#novo_status = input("Novo status: ")
#ID_Vendedor = input("ID do vendedor: ")
           
#AtualizarEstoqueML_ComVariacao(ID_Produto, novo_estoque)
#AtualizarEstoqueML(ID_Produto, novo_estoque)
PuxarEstoqueML(ID_Produto)

#puxar_dados(ID_Produto)
#atualizar_estoque(ID_Produto, novo_estoque)