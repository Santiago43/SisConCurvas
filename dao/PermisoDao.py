import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Permiso
class PermisoDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los permisos en general
    """
    def consultarPermiso(self,permiso_ID):
        """
        Método que permite hacer la consulta de un permiso mediante su ID
        Parámetros:
        - permiso_ID : que es el id del permiso que se consultará 
        """
        try:
            sql= 'select * from Permiso where Permiso_ID='+str(permiso_ID)+';'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result=cursor.fetchone()
            permiso =None
            if result is not None:
                permiso=Permiso(result[0],result[1])
            super().cerrarConexion(cursor,cnx)
            return permiso
        except Exception as e:
            raise e