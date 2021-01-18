import mysql.connector
from mysql.connector import errorcode

from dao.dao import dao
from dao.models import Motivo, PagoDomiciliario


class PagoDomiciliarioDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los pagos de domiciliario en general
    """
    def crearPago(self,pago):
        """
        Método que permite hacer el registro de un pago
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            args=[pago.monto,pago.domiciliario_ID,pago.financiero_ID]
            cursor.callproc("insertarPagoDomiciliario",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
