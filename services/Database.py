import pymysql
from dotenv import load_dotenv
from os import getenv


## Ainda estou pensando em como otimizar e deixar mais seguro essa conecxão com o banco
## por enquanto ele vai retornar a conecxão
def DbConnection():

    load_dotenv()

    conn = pymysql.connect(
        host=getenv("DB_HOST"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        database=getenv("DB_NAME")
    )

    return conn

    

def NoneParamsSQL(query):

    conn = DbConnection()
    cursor  = conn.cursor()
    cursor.execute(query)

    res = cursor.fetchall()

    cursor.close()
    conn.close()


    return res 

def WithParamsSQL(query, params):

    conn = DbConnection()
    cursor  = conn.cursor()
    cursor.execute(query, params)

    res = cursor.fetchall()

    cursor.close()
    conn.close()


    return res









    


