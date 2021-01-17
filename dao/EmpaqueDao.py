import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Empaque
class EmpaqueDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las empaquees de las órdenes de venta
    """
    def crearEmpaque(self,empaque):
        """
        Método que permite hacer el registro de un empaque
        Parámetros:
        - empaque : que es el empaque que se registrará 
        """
        try:
            sql= "insert into Empaque (Orden_venta_ID, Motivo_ID, Usuario_ID, Numero_prendas, Estado, Observaciones) values (%s,%s,%s,%s,%s,%s);"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(empaque.ordenVenta_ID ,empaque.motivo_ID ,empaque.usuario_ID ,empaque.numero_prendas ,empaque.estado ,empaque.observaciones ))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def consultarEmpaque(self,id):
        """
        Método que permite consultar un empaque mediante su id
        Parámetros:
        - id : que es el identificador del empaque 
        """
        try:
            sql= 'select * from Empaque where Empaque_id = '+str(id)+';'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            empaque = Empaque(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
            super().cerrarConexion(cursor,cnx)
            return empaque
        except Exception as e:
            raise e
    def actualizarEmpaque(self,empaque):
        """
        Método que permite actualizar un empaque 
        Parámetros:
        - empaque : que es el empaque que se actualizará
        """
        try:
            sql = 'update Empaque set '
            sql+='Orden_venta_ID =%s, '
            sql+='Usuario_ID=%s, '
            sql+='Numero_prendas=%s, '
            sql+='Estado=%s, '
            sql+='Observaciones=%s, '
            sql+='Motivo_ID=%s, '
            sql+='where Empaque_id =%s ;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(empaque.ordenVenta_ID,empaque.usuario_ID,empaque.numero_prendas,empaque.Estado,empaque.Observaciones,empaque.Motivo_ID)
            cursor.execute(sql,args)
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def eliminarEmpaque(self,empaque):
        """
        Método que permite eliminar una direccion mediante su id
        - direccion : que es la direccion que se elinará
        """
        try:
            sql="delete from Empaque where Empaque_id = %s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(empaque.Empaque_id))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
    def consultarEmpaques(self):
        """
        Método que permite consultar todos los empaques  
        """
        try:
            sql= 'select * from Empaque;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            empaques=list()
            for result in results:
                empaque = Empaque(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
                empaques.append(empaque)
            super().cerrarConexion(cursor,cnx)
            return empaques
        except Exception as e:
            raise e
        