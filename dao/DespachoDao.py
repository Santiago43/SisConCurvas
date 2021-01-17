import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Despacho

class DespachoDao(dao):
    """

    """
    def crearDespacho(self,despacho):
        """
        Método que permite hacer el registro de un despacho
        Parámetros:
        - despacho: El despacho que se registrará
        """
        try:
            sql = "insert into Despacho(Usuario_ID,Orden_venta_ID,Ruta_ID,Estado,Fecha_despacho,Motivo_ID,Id_envia) values (%s,%s,%s,%s,%s,%s,%s);"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql, (despacho.motivo_ID, despacho.usuario_ID, despacho.orden_venta_ID, despacho.ruta_ID, despacho.estado, despacho.fecha_despacho, despacho.id_envia))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarDespacho(self,id):
        """
        Método que permite consultar un despacho mediante su ID
        Parámetros:
        - id : que es el ID del despacho 
        """
        try:
            sql= "select * from Despacho where Despacho_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id,))
            result = cursor.fetchone()
            despacho = Despacho(result[0],result[1],result[2],result[3],result[4],result[5],result[7],result[7])
            return despacho
        except Exception as e:
            raise e

    def actualizarDespacho(self,despacho):
        """
        Método que permite actualizar un despacho (su nombre)
        Parámetros:
        - despacho : que es el despacho que se actualizará
        """
        try:
            sql = '''update Despacho
            set motivo_ID=%s,
            usuario_ID=%s,
            orden_venta_ID=%s,
            ruta_ID=%s,
            estado=%s,
            fecha_despacho=%s,
            id_envia=%s
            where Despacho_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(despacho.motivo_ID, despacho.usuario_ID, despacho.orden_venta_ID, despacho.ruta_ID, despacho.estado, despacho.fecha_despacho, despacho.id_envia, despacho.Despacho_ID))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def eliminarDespacho(self,despacho):
        """
        Método que permite eliminar un producto mediante su id
        - producto : que es el producto que se elinará
        """
        try:
            sql="delete from Despacho where Despacho_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(despacho.Despacho_ID,))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarDespachos(self):
        """
        Método que permite consultar la lista de despachos
        Parámetros:
        - id : que es el ID del despacho 
        """
        try:
            sql= "select * from Despacho"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            despachos=list()
            for result in results:        
                despacho = Despacho(result[0],result[1],result[2],result[3],result[4],result[5],result[7],result[7])
                despachos.append(despacho)
            return despachos
        except Exception as e:
            raise e