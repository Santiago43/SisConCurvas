import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
class RolesDao(dao):
    def crearRol(self,rol):
        sql= "insert into rol (Nombre) values (%s);"
        cnx=super().connectDB()
        cursor=cnx.cursor()
        cursor.execute(sql,(rol.nombre))
        return True