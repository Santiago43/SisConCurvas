import mysql.connector
from mysql.connector import errorcode

from dao.dao import dao
from dao.models import Ciudad, Departamento, Direccion


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
            sql= "insert into Direccion (Ciudad_ID, Barrio, Direccion) values (%s,%s,%s,%s);"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(direccion.ciudad_ID,direccion.barrio,direccion.direccion))
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
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Direccion where direccion_ID = %s;"
            
            cursor.execute(sql,(id,))
            result = cursor.fetchone()
            direccion = Direccion(result[0],result[1],result[2],result[3])
            super().cerrarConexion(cursor,cnx)
            return direccion
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def consultarDirecciones(self):
        """
        Método que permite consultar todas las direcciones

        Parámetros:
        -
        """
        try:
            sql= '''select * from Direccion;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            direcciones=list()
            for result in results:
                direccion = Direccion(result[0],result[1],result[2],result[3])
                direcciones.append(direccion)
            super().cerrarConexion(cursor,cnx)
            return direcciones
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def actualizarDireccion(self,direccion):
        """
        Método que permite actualizar una direccion
        Parámetros:
        - direccion : que es la direccion que se actualizará
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql = 'update Direccion set '
            sql+='Ciudad_ID="%s, '
            sql+='Barrio=%s, '
            sql+='Direccion=%s '
            sql+='where Direccion_id =%s ;'
            
            args=(direccion.ciudad_ID,direccion.departamento_ID,direccion.barrio,direccion.direccion)
            cursor.execute(sql,args)
            super().cerrarConexion(cursor,cnx)
            return direccion
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
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
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def consultarCiudades(self):
        """
        Método que permite consultar todas las ciudades
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="select * from Ciudad;"

            cursor.execute(sql)
            ciudades=list()
            for row in cursor:
                ciudades.append(Ciudad(row[0],row[1],row[2]))
            return ciudades
            super().cerrarConexion(cursor,cnx)
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarDepartamentos(self):
        """
        Método que permite consultar todos los departamentos
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="select * from Departamento;"
            
            cursor.execute(sql)
            departamento=list()
            for row in cursor:
                departamento.append(Departamento(row[0],row[1]))
            super().cerrarConexion(cursor,cnx)
            return departamento
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarCiudad(self,ciudad_ID):
        """
        Método que permite consultar todas las ciudades
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="select * from Ciudad where Ciudad_ID=%s;"
            cursor.execute(sql,(ciudad_ID,))
            result=cursor.fetchone()
            ciudad=None
            if result is not None:
                ciudad=Ciudad(result[0],result[1],result[2])
            super().cerrarConexion(cursor,cnx)
            return ciudad
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarDepartamento(self,departamento_ID):
        """
        Método que permite consultar todas las ciudades
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="select * from Departamento; where Departamento_ID=%s;"
            cursor.execute(sql,(departamento_ID,))
            result=cursor.fetchone()
            departamento=None
            if result is not None:
                departamento=Departamento(result[0],result[1])
            super().cerrarConexion(cursor,cnx)
            return departamento
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e