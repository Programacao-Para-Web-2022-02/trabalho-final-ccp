
import mysql.connector

cnx = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='db')
print("Conectado=", cnx.is_connected())
print("Conjunto de caracteres=", cnx.charset)

cnx.close()






import mysql.connector


class SQL:

    def __init__(self   ):
       self.cnx = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='db')


    def executar(self, comando, parametros):
       cs = self.cnx.cursor(buffered=True)
       cs.execute(comando, parametros)
       self.cnx.commit()
       cs.close()
       return True

    def consultar(self, comando, parametros = []):
       cs = self.cnx.cursor()
       cs.execute(comando, parametros)
       return cs

    def __del__(self):
       self.cnx.close()


