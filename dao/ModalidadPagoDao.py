import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Modalidad_pago
class ModalidadPagoDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las modalidades de pago en general
    """
    def consultarModalidades(self):
        """
        Método que permite hacer la consulta de todos los modalidades
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= 'select * from Modalidad_pago;'
            cursor.execute(sql)
            results=cursor.fetchall()
            modalidades=list()
            for result in results:
                modalidad=Modalidad_pago(result[0],result[1])
                modalidades.append(modalidad)
            super().cerrarConexion(cursor,cnx)
            return modalidades
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarModalidad(self,id):
        """
        Método que permite hacer la consulta de una modalidad de pago por su ID
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= 'select * from Modalidad_pago where Modalidad_pago_ID=%s;'
            cursor.execute(sql,(id,))
            result=cursor.fetchone()
            modalidad=None
            if result is not None:
                modalidad=Modalidad_pago(result[0],result[1])
            super().cerrarConexion(cursor,cnx)
            return modalidad
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e