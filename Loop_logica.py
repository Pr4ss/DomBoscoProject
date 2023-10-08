import mysql.connector
from mysql.connector import errorcode
from Estoque import PuxarEstoqueML





cnx = mysql.connector.connect(user='cshpco98_viquetti',
                                  database='cshpco98_estoque',
                                  password = 'Bananaverde333@',
                                  host = 'cshp.com.br')


def desconectarbanco(): 
  cnx.close()
  

def consulta():

  cursor = cnx.cursor()


  consulta_id = "SELECT `id_banco`, `quantidade`, `id_mercadolivre` FROM `estoque`" #consulta os valores do banco de dados para bater com os que vem da API do ML
  dicionarios = []
  cursor.execute(consulta_id)
  produtos_bd = cursor.fetchall()

  for tupla in produtos_bd:
    novo_dicionario = {
        "id_banco": tupla[0],
        "quantidade": tupla[1],
        "id_mercadolivre": tupla[2]
    }
    dicionarios.append(novo_dicionario)
  


  for item in dicionarios:
    quantidade_bd = item["quantidade"]
    id_mercadolivre = item["id_mercadolivre"]
    id_banco = item["id_banco"]
    EstoqueML = PuxarEstoqueML(id_mercadolivre)
    PuxarEstoqueML(id_mercadolivre)
    

    if EstoqueML != quantidade_bd:
      novo_estoque = quantidade_bd - EstoqueML
      novo_estoque = abs(novo_estoque - quantidade_bd)
      consulta_atualizacao = f"UPDATE `estoque` SET `quantidade` = {novo_estoque} WHERE `id_banco` = {id_banco}"
      cursor.execute(consulta_atualizacao)
      cnx.commit()
      
    
consulta()

desconectarbanco()
