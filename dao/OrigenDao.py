import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Origen
class OrigenDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los orígenes en general
    """
    def consultarOrigenes(self):
        """
        Método que permite hacer la consulta de todos los orígenes (de venta, no empaque, no despacho, no distribución)
        """
        try:
            sql= 'select * from Origen;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results=cursor.fetchall()
            origenes=list()
            for result in results:
                origen=Origen(result[0],result[1])
                origenes.append(origen)
            super().cerrarConexion(cursor,cnx)
            return origenes
        except Exception as e:
            raise e