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
            sql= 'insert into Control_Rol(Rol_ID,Usuario_ID,Fecha_modificacion,Tipo,Detalle) values (%s,%s,sysdate(),%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(controlRol.rol_ID,controlRol.usuario_ID,controlRol.tipo,controlRol.detalle))
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
            cursor.execute(sql,(controlInventario.usuario_ID,controlInventario.referenciaProducto,controlInventario.fecha,controlInventario.inventario_inicial,controlInventario.detalle,controlInventario.numero_prendas,controlInventario.tipo))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def consultarControles(self):
        """
        Método que permite consultar un categoria mediante su ID
        Parámetros:
        - id : que es el ID de categoria 
        """
        try:
            sql= "select * from Categoria where categoria_ID="+str(id)+";"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            categoria = Categoria(result[0],result[1],result[2])
            super().cerrarConexion(cursor,cnx)
            return categoria
        except Exception as e:
            raise e
