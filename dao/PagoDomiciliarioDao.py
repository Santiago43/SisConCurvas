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
            args=[pago.monto,pago.domiciliario_ID,pago.financiero_ID,pago.estado]
            cursor.callproc("insertarPagoDomiciliario",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarPago(self,id):
        """
        Método que permite hacer la consulta de un pago mediante su id
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= '''select pd.*,dp.Usuario_ID as Domiciliario_ID,fp.Usuario_ID as Financiero_ID from Pago_domiciliario as pd
            inner join Domiciliario_tiene_Pago as dp on dp.Pago_domiciliario_ID=pd.Pago_domiciliario_ID
            inner join Financiero_hace_pago as fp on pd.Pago_domiciliario_ID=fp.Pago_domiciliario_ID
            where pd.Pago_domiciliario_ID=%s;'''
            cursor.execute(sql,(id,))
            result=cursor.fetchone()
            pago=None
            if result is not None:
                pago=PagoDomiciliario(result[0],result[1],result[2],result[3],result[4],result[5])
            super().cerrarConexion(cursor,cnx)
            return pago
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def actualizarPago(self,pago):
        """
        Método que permite actualizar un pago
        Parámetros:
        - pago : que es el pago que se actualizará
        """
        try:
            sql = '''update Pago_domiciliario as pd set
            pd.Estado=%s,
            pd.Monto=%s,
            pd.fecha_pago=cast(sysdate() as date)
            where pd.Pago_domiciliario_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(pago.estado,pago.monto,pago.pagoDomiciliario_ID)
            cursor.execute(sql,args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:            
            super().cerrarConexion(cursor,cnx)
            raise e
    def eliminarPago(self,pago):
        """
        Método que permite actualizar un pago
        Parámetros:
        - pago : que es el pago que se actualizará
        """
        try:
            sql = '''update Pago_domiciliario as pd set
            pd.Estado=%s,
            pd.Monto=%s,
            pd.fecha_pago=cast(sysdate() as date)
            where pd.Pago_domiciliario_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(pago.estado,pago.monto,pago.pagoDomiciliario_ID)
            cursor.execute(sql,args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:            
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarPagos(self):
        """
        Método que permite hacer la consulta de todos los pagos
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= '''select pd.*,dp.Usuario_ID as Domiciliario_ID,fp.Usuario_ID as Financiero_ID from Pago_domiciliario as pd
            inner join Domiciliario_tiene_Pago as dp on dp.Pago_domiciliario_ID=pd.Pago_domiciliario_ID
            inner join Financiero_hace_pago as fp on pd.Pago_domiciliario_ID=fp.Pago_domiciliario_ID;'''
            cursor.execute(sql)
            results=cursor.fetchall()
            pagos=list()
            for result in results:
                pago=PagoDomiciliario(result[0],result[1],result[2],result[3],result[4],result[5])
                pagos.append(pago)
            super().cerrarConexion(cursor,cnx)
            return pagos
        except Exception as e:            
            super().cerrarConexion(cursor,cnx)
            raise e