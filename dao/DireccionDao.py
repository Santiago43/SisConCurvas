import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Direccion

class DireccionDao(dao):
    """
    
    """
    def crearDireccion(self,direccion):
        """
        Método que permite hacer el registro de una direccion
        Parámetros:
        - direccion : que es la direccion que se registrará 
        """
        try:
            sql= "insert into Direccion (ciudad_ID, Departamento_ID, Barrio, Direccion) values (%s,%s,%s,%s);"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(direccion.ciudad_ID,direccion.departamento_ID,direccion.barrio,direccion.direccion))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarDireccion(self,id):
        """
        Método que permite consultar una Direccion mediante su id
        Parámetros:
        - id : que es el identificador de la direccion 
        """
        try:
            sql= "select * from direccion where direccion_ID = %s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id))
            result = cursor.fetchone()
            direccion = Direccion(result[0],result[1],result[2],result[3],result[4])
            return direccion
        except Exception as e:
            raise e

    def actualizarDireccion(self,direccion):
        """
        Método que permite actualizar una direccion
        Parámetros:
        - direccion : que es la direccion que se actualizará
        """
        try:
            sql = 'update Direccion set '
            sql+='Ciudad_ID="%s, '
            sql+='Departamento_ID=%s, '
            sql+='Barrio=%s, '
            sql+='Direccion=%s, '
            sql+='where Direccion_id =%s ;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(direccion.ciudad_ID,direccion.departamento_ID,direccion.barrio,direccion.direccion)
            cursor.execute(sql,)
        except Exception as e:
            raise e

    def eliminardireccion(self,direccion):
        """
        Método que permite eliminar una direccion mediante su id
        - direccion : que es la direccion que se elinará
        """
        try:
            sql="delete from Direccion where direccion_ID = %s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(direccion.direccion_id))
            return True
        except Exception as e:
            raise e