import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import OrdenVenta
from dao.models import ProductoEnOrden
from dao.models import Inventario
from dao.models import Categoria
class OrdenDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las órdenes de venta
    """
    def crearOrden(self,orden):
        """
        Método que permite hacer el registro de una orden
        Parámetros:
        - orden : que es la orden asociada a una orden de venta existente  
        """
        try:
            cnx=super().connectDB()
            cursor=cnx.cursor()
            sql=''' insert into Orden_venta 
            (Motivo_ID,Origen_ID,Modalidad_pago_ID,Metodo_compra_ID,Direccion_id,Cliente_ID,Usuario_ID,Estado,Fecha_venta,Nota,Fecha_entrega,Tipo_venta,Descuento)
            values
            (%s,%s,%s,%s,%s,%s,%s,sysdate(),%s,%s,%s,%s);
            '''
            cursor.execute(sql,(orden.motivo_ID,orden.origen_ID,orden.modalidadad_pago_ID,orden.metodo_compra_ID,orden.direccion_ID,orden.cliente_ID,orden.usuario_ID,orden.estado,orden.precio,orden.nota,orden.fecha_entrega,orden.tipo_venta,orden.descuento))
            for productoEnOrden in orden.productos:
                sql2=''' insert into Orden_venta_tiene_Producto 
                (Orden_venta_ID,Inventario_Referencia_Producto_ID,cantidad) 
                values (%s,%s,%s);  '''
                cursor.execute(sql2,(orden.orden_ID,productoEnOrden.producto.referenciaProducto,productoEnOrden.cantidad))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarOrden(self,id):
        """
        Método que permite consultar una orden de venta mediante su ID
        Parámetros:
        - id : que es el ID de la orden
        """
        try:
            sql='''select *,(select sum(q.Precio_venta*q.cantidad) from (select i.Precio_venta, oc.cantidad from Inventario as i
            inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
            inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
            where o.Orden_venta_ID=ov.Orden_venta_ID) as q) as precio  from Orden_venta as ov where Orden_venta_ID='''+str(id)+''';'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            ordenVenta=OrdenVenta(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],[],result[14])
            sql2= '''select i.*, oc.cantidad from Inventario as i
            inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
            inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
            where o.Orden_venta_ID='''+str(id)+''';'''
            cursor.execute(sql2)
            result2= cursor.fetchall()
            for row in result2:
                productoEnOrden=ProductoEnOrden(Inventario(row[0],row[1],row[2],row[3],row[4],row[5],[]),row[6])
                sql3='''select c.* from Categoria as c
                inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
                where ic.Inventario_Referencia_Producto_ID=%s;'''
                cursor.execute(sql3,(productoEnOrden.producto.referenciaProducto,))
                for row in cursor:
                    productoEnOrden.producto.categorias.append(Categoria(row[0],row[1],row[2]))  
                ordenVenta.productos.append(productoEnOrden)
            super().cerrarConexion(cursor,cnx)
            return ordenVenta
        except Exception as e:
            raise e

    def actualizarOrden(self,orden):
        """
        Método que permite actualizar una orden
        Parámetros:
        - orden : que es la orden que se actualizará
        """
        try:
            sql = '''update Orden_venta set
                    Motivo_ID =%s,
                    Origen_ID=%s,
                    Modalidad_pago_ID=%s,
                    Metodo_compra_ID=%s,
                    Direccion_id=%s,
                    Cliente_ID=%s,
                    Usuario_ID=%s,
                    Estado=%s,
                    Nota=%s,
                    Fecha_entrega=%s,
                    Tipo_venta=%s,
                    Descuento=%s
                    where Orden_venta_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(orden.motivo_ID,orden.origen_ID,orden.modalidad_pago_ID,orden.metodo_compra_ID,orden.direccion_ID,orden.cliente_ID,orden.usuario_ID,orden.estado,orden.nota,orden.tipo_venta,orden.descuento,orden.ordenVenta_ID))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def eliminarOrden(self,orden):
        """
        Método que permite eliminar una orden mediante su id
        - orden : que es la orden que se eliminará
        """
        try:
            sql="delete from Orden_venta where Orden_venta_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(orden.ordenVenta_ID,))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def agregarProducto(self, productoEnOrden):
        """
        Método que permite agregar un producto en una orden
        - producto : que es el producto que se agregará a la orden
        - orden: que es la orden a la que se agregará el producto
        """
        try:
            sql='''
            insert into Orden_venta_tiene_producto (Orden_venta_ID,Inventario_Referencia_Producto_ID,cantidad) 
            values (%s,%s,%s);'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(productoEnOrden.orden.ordenVenta_ID,productoEnOrden.producto.referenciaProducto))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def removerProducto(self, productoEnOrden):
        try:
            sql='''delete from Orden_venta_tiene_producto
            where (Orden_venta_ID,Inventario_Referencia_Producto_ID)=(%s,%s);'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(productoEnOrden.orden.ordenVenta_ID,productoEnOrden.producto.referenciaProducto))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
    def consultarOrdenes(self):
        """
        Método que permite consultar todas las órdenes de venta
        """
        try:
            sql='''select *,(select sum(q.Precio_venta*q.cantidad) from (select i.Precio_venta, oc.cantidad from Inventario as i
            inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
            inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
            where o.Orden_venta_ID=ov.Orden_venta_ID) as q) as precio  from Orden_venta as ov;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            ordenesVenta=list()
            for result in results:
                ordenVenta=OrdenVenta(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],[],result[14])
                sql2= '''select i.*, oc.cantidad from Inventario as i
                inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
                inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
                where o.Orden_venta_ID='''+str(ordenVenta.ordenVenta_ID)+''';'''
                cursor.execute(sql2)
                result2= cursor.fetchall()
                for row in result2:
                    productoEnOrden=ProductoEnOrden(Inventario(row[0],row[1],row[2],row[3],row[4],row[5],list()),row[6])
                    sql3='''select c.* from Categoria as c
                    inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
                    where ic.Inventario_Referencia_Producto_ID="'''+productoEnOrden.producto.referenciaProducto+'''";'''
                    cursor.execute(sql3)
                    for row in cursor:
                        productoEnOrden.producto.categorias.append(Categoria(row[0],row[1],row[2]))  
                    ordenVenta.productos.append(productoEnOrden)
                ordenesVenta.append(ordenVenta)
            super().cerrarConexion(cursor,cnx)
            return ordenesVenta
        except Exception as e:
            raise e