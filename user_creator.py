import requests

ACCESS_TOKEN = "APP_USR-6879509485276765-080315-1b91b9e4ea88fa8afa90d97a8243923d-323433124"

def criar_usuario_teste(site_id):
    url = "https://api.mercadolibre.com/users/test_user"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "site_id": site_id
    }

    resposta = requests.post(url, headers=headers, json=data)

    if resposta.status_code == 201:
        dados_usuario = resposta.json()
        print("Usuário de teste criado com sucesso:")
        print("ID:", dados_usuario["id"])
        print("Apelido:", dados_usuario["nickname"])
        print("Senha:", dados_usuario["password"])
        print("Status do site:", dados_usuario["site_status"])
    else:
        print("Não foi possível criar o usuário de teste.")
        print("Código de status:", resposta.status_code)

criar_usuario_teste("MLB")