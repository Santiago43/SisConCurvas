import mysql.connector
from mysql.connector import errorcode

from dao.dao import dao
from dao.models import Categoria, Distribucion, Inventario, ProductoEnOrden


class DistribucionDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las distribuciones de las órdenes de venta
    """
    def crearDistribucion(self,distribucion):
        """
        Método que permite hacer el registro de una distribucion
        Parámetros:
        - distribucion : que es la distribucion asociada a un despacho existente  
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql='''insert into Distribucion(Usuario_ID,Despacho_ID,Estado,Motivo_ID,Venta_neta,Costo_distribucion)
            values(%s,%s,%s,%s,%s,%s);'''
            args=(distribucion.usuario_ID,distribucion.despacho_ID,distribucion.estado,distribucion.motivo_ID,distribucion.ventaNeta,distribucion.costoDistribucion)
            cursor.execute(sql,args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def consultarDistribucion(self,id):
        """
        Método que permite consultar una distribución mediante su ID

        Parámetros:
        - id : que es el ID de la distribución 
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Distribucion where Distribucion_ID=%s;"
            cursor.execute(sql,(id,))
            distribucion=None
            result = cursor.fetchone()
            if result is not None:
                distribucion=Distribucion(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list())
                sql2='''select p.*,dp.cantidad from Inventario as p
                inner join Distribucion_tiene_prendas_Devueltas as dp on dp.Inventario_Referencia_Producto_ID=p.Referencia_Producto_ID
                inner join Distribucion as d on d.Distribucion_ID=dp.Distribucion_ID
                where d.Distribucion_ID=%s;'''
                cursor.execute(sql2,(distribucion.distribucion_ID,))
                result2=cursor.fetchall()
                for row in result2:
                    productoEnDistribucion=ProductoEnOrden(Inventario(row[0],row[1],row[2],row[3],row[4],row[5],list()),row[6])
                    sql3='''select c.* from Categoria as c
                    inner join Inventario_tiene_Categoria as ic on ic.Categoria_ID=c.Categoria_ID
                    where ic.Inventario_Referencia_Producto_ID=%s;'''
                    cursor.execute(sql3,(productoEnDistribucion.producto.referenciaProducto,))
                    result3=cursor.fetchall()
                    for rowcat in result3:
                        productoEnDistribucion.producto.categorias.append(Categoria(rowcat[0],rowcat[1],rowcat[2]))   
                    distribucion.productos.append(productoEnDistribucion)
            super().cerrarConexion(cursor,cnx)
            return distribucion
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def actualizarDistribucion(self,distribucion):
        """
        Método que permite actualizar una distribución
        Parámetros:
        - distribucion : que es la distribución que se actualizará
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql = '''update Distribucion set
            Usuario_ID=%s,
            Estado=%s,
            Venta_neta=%s,
            Motivo_ID=%s,
            Costo_distribucion=%s
            where Distribucion_ID=%s;'''
            cursor.execute(sql,(distribucion.usuario_ID,distribucion.estado,distribucion.ventaNeta,distribucion.motivo_ID,distribucion.costoDistribucion,distribucion.distribucion_ID))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def eliminarDistribucion(self,distribucion):
        """
        Método que permite eliminar un producto mediante su id.

        Parámetros:
        - distribucion : que es la distribución que se eliminará
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="delete from Distribucion where Distribucion_ID=%s;"    
            cursor.execute(sql,(distribucion.distribucion_ID,))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def agregarProductoDevuelto(self,distribucion, productoDevuelto):
        """
        Método que permite agregar categoria a un producto
        - productoDevuelto : que es el producto al que se le agregará a la devolución de una distribución
        - distribucion: que es la distribución a la que que se le agregará al producto devuelto y su cantidad
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql='''insert into Distribucion_tiene_prendas_Devueltas(Distribucion_ID,Inventario_Referencia_Producto_ID,cantidad)
            values (%s,%s,%s);'''
            cursor.execute(sql,(distribucion.distribucion_ID,productoDevuelto.producto.referenciaProducto,productoDevuelto.cantidad))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
        
    def removerProductoDevuelto(self,distribucion, productoDevuelto):
        """
        Método que permite retirar un producto devuelto de una distribución
        - distribucion: que es la distribución a la que que se le agregará al producto devuelto y su cantidad
        - productoDevuelto : que es el producto al que se le agregará a la devolución de una distribución
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql='delete from Distribucion_tiene_prendas_Devueltas where (Distribucion_ID,Inventario_Referencia_producto_ID)=(%s,%s);'
            cursor.execute(sql,(distribucion.distribucion_ID, productoDevuelto.producto.referenciaProducto))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarDistribuciones(self):
        """
        Método que permite consultar la lista de distribuciones
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= "select * from Distribucion;"
            cursor.execute(sql)
            distribuciones=list()
            results = cursor.fetchall()
            for result in results:
                distribucion=Distribucion(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list())
                sql2='''select p.*,dp.cantidad from Inventario as p
                inner join Distribucion_tiene_prendas_Devueltas as dp on dp.Inventario_Referencia_Producto_ID=p.Referencia_Producto_ID
                inner join Distribucion as d on d.Distribucion_ID=dp.Distribucion_ID
                where d.Distribucion_ID=%s;'''
                cursor.execute(sql2,(distribucion.distribucion_ID,))
                result2=cursor.fetchall()
                for row in result2:
                    productoEnDistribucion=ProductoEnOrden(Inventario(row[0],row[1],row[2],row[3],row[4],row[5],list()),row[6])
                    sql3='''select c.* from Categoria as c
                    inner join Inventario_tiene_Categoria as ic on ic.Categoria_ID=c.Categoria_ID
                    where ic.Inventario_Referencia_Producto_ID=%s;'''
                    cursor.execute(sql3,(productoEnDistribucion.producto.referenciaProducto,))
                    result3=cursor.fetchall()
                    for rowcat in result3:
                        productoEnDistribucion.producto.categorias.append(Categoria(rowcat[0],rowcat[1],rowcat[2]))   
                    distribucion.productos.append(productoEnDistribucion)
                distribuciones.append(distribucion)
            super().cerrarConexion(cursor,cnx)
            return distribuciones
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
