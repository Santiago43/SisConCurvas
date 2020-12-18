import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
class RolesDao(dao):
    def crearRol(self,rol):
        """
        """
        try:
            sql= "insert into rol (Nombre) values (%s);"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(rol.nombre))
            return True
        except Exception as e:
            raise e

    def consultarRol(self,id):
        """
        """
        try:
            sql= "select * from rol where Rol_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id))
        except Exception as e:
            raise e

    def actualizarRol(self,rol):
        """

        """
        try:
            sql = 'update rol set Nombre=%s where Rol_ID = %s;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(rol.nombre,rol.id))
        except Exception as e:
            raise e

    def eliminarRol(self,rol):
        try:
            sql="delete from rol where Rol_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(rol.id))
        except Exception as e:
            raise e

    def agregarPermiso(self, rol, permiso):
        try:
            sql=''
        except Exception as e:
            raise e
        
    def removerPermiso(self, rol, permiso):
        try:
            sql=''
        except Exception as e:
            raise e