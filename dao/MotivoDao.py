import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Motivo
class MotivoDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los motivos en general
    """
    def consultarMotivos(self):
        """
        Método que permite hacer la consulta de todos los motivos (de venta, no empaque, no despacho, no distribución)
        """
        try:
            sql= 'select * from Motivo;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results=cursor.fetchall()
            motivos=list()
            for result in results:
                motivo=Motivo(result[0],result[1],result[2])
                motivos.append(motivo)
            super().cerrarConexion(cursor,cnx)
            return motivos
        except Exception as e:
            raise e