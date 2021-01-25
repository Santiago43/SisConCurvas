import mysql.connector
from mysql.connector import errorcode
class dao:
    """
    docstring
    """
    def __init__(self):
        self.user='concurva_sis'
        self.password='XTVwTewvQp2cTfC'
        self.database='concurva_sistema'
        self.host='127.0.0.1'
    def connectDB(self):
        cnx = mysql.connector.connect(user=self.user, password = self.password, database=self.database, host=self.host)
        return cnx
    def cerrarConexion(self,cursor,cnx):
        cursor.close()
        cnx.close()