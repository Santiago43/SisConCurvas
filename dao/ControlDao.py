import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Control_rol, Control_venta, Control_inventario

class ControlDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los controles
    """
    def crearControlRol(self,controlRol):
        """
        Método que permite hacer el registro de un control de rol
        
        Parámetros:
        - controlRol : que es el control que se registrará 
        """
        try:
            sql= 'insert into Control_Rol(Rol_ID,Usuario_ID,Fecha_modificacion,Tipo,Detalle) values (%s,%s,sysdate(),%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(controlRol.rol_ID,controlRol.usuario_ID,controlRol.tipo,controlRol.detalle))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def crearControlVenta(self,controlVenta):
        """
        Método que permite hacer el registro de un control de una venta
        
        Parámetros:
        - controlVenta : que es el control que se registrará 
        """
        try:
            sql= 'insert into Control_venta(Usuario_ID,Orden_venta_ID,Fecha_modificacion,Cambio) values (%s,%s,sysdate(),%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(controlVenta.usuario_ID,controlVenta.orden_venta_ID,controlVenta.cambio))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def crearControlInventario(self,controlInventario):
        """
        Método que permite hacer el registro de un control de una venta
        
        Parámetros:
        - controlVenta : que es el control que se registrará 
        """
        try:
            sql= 'insert into Control_Inventario(Usuario_ID,Inventario_Referencia_Producto_ID,Fecha,Inventario_inicial,Detalle,Numero_prendas,Tipo) values (%s,%s,sysdate(),%s,%s,%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(controlInventario.usuario_ID,controlInventario.referenciaProducto,controlInventario.inventario_inicial,controlInventario.detalle,controlInventario.numero_prendas,controlInventario.tipo))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def consultarControlesRol(self):
        """
        Método que permite consultar todos los controles de la tabla de roles
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Control_Rol;"    
            cursor.execute(sql)
            results = cursor.fetchall()
            controles=list()
            for result in results:
                controlRol = Control_rol(result[0],result[1],result[2],result[3],result[4],result[5])
                controles.append(controlRol)
            super().cerrarConexion(cursor,cnx)
            return controles
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarControlesInventario(self):
        """
        Método que permite consultar todos los controles de la tabla de Inventario
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Control_Inventario;"    
            cursor.execute(sql)
            results = cursor.fetchall()
            controles=list()
            for result in results:
                controlInventario = Control_inventario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
                controles.append(controlInventario)
            super().cerrarConexion(cursor,cnx)
            return controles
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarControlesVenta(self):
        """
        Método que permite consultar todos los controles de la tabla de Inventario
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Control_venta;"    
            cursor.execute(sql)
            results = cursor.fetchall()
            controles=list()
            for result in results:
                controlVenta = Control_venta(result[0],result[1],result[2],result[3],result[4])
                controles.append(controlVenta)
            super().cerrarConexion(cursor,cnx)
            return controles
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e