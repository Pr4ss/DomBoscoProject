import requests

# Dados do seu aplicativo do Mercado Livre
client_id = 6879509485276765
client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
redirect_uri = "https://localhost:3000/"

# URL de autorização
authorization_url = f'https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'


def primeiro_token(authorization_url):
    # Redirecione o usuário para a URL de autorização para permitir o acesso
    print("Por favor, acesse a seguinte URL e permita o acesso:")
    print(authorization_url)

    # Troque o código de autorização por um token de acesso
    code = 'TG-64cbfb2baa3bd10001608932-323433124'
    token_url = 'https://api.mercadolibre.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }

    response = requests.post(token_url, data=data)

    # Verifique se a resposta é bem-sucedida e obtenha o token de acesso
    if response.status_code == 200:
        access_token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']
        responsejson = response.json()
        print(f"Token de acesso: {access_token}")
        print(f"Refresh Token: {refresh_token}")
    else:
        print("Falha na obtenção do token de acesso.")
        print(response.json())

def obter_novo_token_acesso():
    url = "https://api.mercadolibre.com/oauth/token"

    # Substitua as variáveis abaixo pelos valores corretos da sua aplicação e refresh token
    client_id = "6879509485276765"
    client_secret = "t3TezoMpOAnhJfIhXWnK7cJ2f2ryUl6o"
    refresh_token = "TG-64cbfb2baa3bd10001608932-323433124"

    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    resposta = requests.post(url, data=data, headers=headers)

    if resposta.status_code == 200:
        dados_token = resposta.json()
        token_acesso = dados_token["access_token"]
        refresh_token = dados_token["refresh_token"]
        print("Novo token de acesso obtido com sucesso:")
        print("Token de Acesso:", token_acesso)
        print("Refresh token: ", refresh_token)
    else:
        print("Não foi possível obter o novo token de acesso.")
        print("Código de status:", resposta.status_code)

obter_novo_token_acesso()
