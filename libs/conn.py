import psycopg2

try:
    connection = psycopg2.connect(host="localhost", dbname="sale", user="postgres", password="123456")
    conn = connection.cursor()

    print('Conectado')
except Exception as erro:
    print(f'ERRO: {erro}')
