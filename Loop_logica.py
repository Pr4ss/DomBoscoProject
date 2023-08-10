import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='cshpco98_viquetti',
                                  database='cshpco98_estoque',
                                  password = 'Bananaverde333@',
                                  host = 'cshp.com.br')


def desconectarbanco(): 
  cnx.close()
  

def consulta():

  cursor = cnx.cursor()

  consulta_id = "SELECT `id_banco`, `quantidade`FROM `estoque`" #consulta os valores do banco de dados para bater com os que vem da API do ML
  

  cursor.execute(consulta_id)

  # Buscar todos os dados no banco de ados
  produtos_bd = cursor.fetchall()
  print(produtos_bd)
  # Exemplo de dados do estoque por enquanto está os valores de exemplo em uma lista, mas serão os dados coletados da API do ML.
  estoque = [
      {"nome": "martelo", "quantidade":50,"id": 1},
      {"nome": "Touca", "quantidade": 50,'id': 3}
      # ...
  ]

  # Loop for para comparar e atualizar quantidades
  for produto_estoque in estoque:
      id_produto_estoque = produto_estoque["id"]
      quantidade_estoque = produto_estoque["quantidade"]
     

      # Encontrar o produto correspondente no banco de dados comparando o ID, (mais pra frente vai ter uma lógica para bater com o ID do ML)
      produto_bd = None
      for item in produtos_bd:
          if item[0] == id_produto_estoque:
              produto_bd = item
              break
      
      
      if produto_bd:
          id_banco = produto_bd[0]
          quantidade_bd = produto_bd[1]
          
          if quantidade_bd != quantidade_estoque:
              # Calcular a nova quantidade no banco de dados alterando o valor para o valor que vem do ML
              nova_quantidade = quantidade_estoque
              
              # Atualizar a quantidade no banco de dados dando um UPDATE que vai para o banco
              consulta_atualizacao = f"UPDATE `estoque` SET `quantidade` = {nova_quantidade} WHERE `id_banco` = {id_banco}"
              cursor.execute(consulta_atualizacao)
              cnx.commit()
              
              print(f"Quantidade atualizada para o produto {produto_bd} de ID: {id_banco}: {nova_quantidade}")
      else:
          print(f"Produto com ID {id_produto_estoque} não encontrado no banco de dados.")

  # Fechar o cursor e a conexão com o banco de dados


consulta()

desconectarbanco()