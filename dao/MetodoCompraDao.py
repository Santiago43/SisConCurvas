import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Metodo_compra
class MetodoCompraDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las métodos de compra en general
    """
    def consultarMetodos(self):
        """
        Método que permite hacer la consulta de todos los métodos
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= 'select * from Metodo_compra;'
            cursor.execute(sql)
            results=cursor.fetchall()
            metodos=list()
            for result in results:
                metodo=Metodo_compra(result[0],result[1])
                metodos.append(metodo)
            super().cerrarConexion(cursor,cnx)
            return metodos
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarMetodo(self,id):
        """
        Método que permite hacer la consulta de una m+etodo de pago por su ID
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= 'select * from Metodo_compra where Metodo_compra_ID=%s;'
            cursor.execute(sql,(id,))
            result=cursor.fetchone()
            metodo=None
            if result is not None:
                metodo=Metodo_compra(result[0],result[1])
            super().cerrarConexion(cursor,cnx)
            return metodo
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e