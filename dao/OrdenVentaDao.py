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
            (Origen_ID,Modalidad_pago_ID,Metodo_compra_ID,Direccion_id,Cliente_ID,Usuario_ID,Estado,Fecha_venta,Precio,Nota,Fecha_entrega,Tipo_venta,Descuento)
            values
            (%s,%s,%s,%s,%s,%s,%s,cast(sysdate() as DATE),%s,%s,%s,%s,%s);
            '''
            cursor.execute(sql,(orden.origen_ID,orden.modalidadad_pago_ID,orden.metodo_compra_ID,orden.direccion_ID,orden.cliente_ID,orden.usuario_ID,orden.estado,orden.precio,orden.nota,orden.fecha_entrega,orden.tipo_venta,orden.descuento))
            for productoEnOrden in orden.productos:
                sql2=''' insert into Orden_venta_tiene_producto 
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
            sql='''select * from Orden_venta where Orden_venta_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id))
            result = cursor.fetchone()
            ordenVenta=OrdenVenta(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14],[])
            sql2= '''select i.*, oc.cantidad from Inventario as i
            inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
            inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
            where o.Orden_venta_ID=%s;'''
            cursor.execute(sql2,(id))
            result2= cursor.fetchall()
            for row in result2:
                productoEnOrden=ProductoEnOrden(Inventario(row[0],row[1],row[2],row[3],row[4],row[5],[]),row[6])
                sql3='''select c.* from Categoria as c
                inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
                where ic.Inventario_Referencia_Producto_ID=%s;'''
                cursor.execute(sql3,(productoEnOrden.producto.referenciaProducto))
                for row in cursor:
                    productoEnOrden.producto.categorias.append(Categoria(row[0],row[1],row[2]))  
                ordenVenta.productos.append(productoEnOrden)
            super().cerrarConexion(cursor,cnx)
            return ordenVenta
        except Exception as e:
            raise e

    def actualizarProducto(self,producto):
        """
        Método que permite actualizar un producto (su nombre)
        Parámetros:
        - producto : que es el producto que se actualizará
        """
        try:
            sql = '''update Inventario
            set Descripcion=%s,
            Url_imagen=%s,
            Stock=%s,
            Precio_costo=%s,
            Precio_venta=%s
            where Referencia_Producto_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.descripcion,producto.urlImagen,producto.precioCosto,producto.precioVenta,producto.referenciaProducto))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def eliminarproducto(self,producto):
        """
        Método que permite eliminar un producto mediante su id
        - producto : que es el producto que se elinará
        """
        try:
            sql="delete from Producto where producto_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.referenciaProducto))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def agregarCategoria(self, producto, categoria):
        """
        Método que permite agregar categoria a un producto
        - producto : que es el producto al que se le agregará el categoria
        - categoria: que es el categoria que se le agregará al producto
        """
        try:
            sql='insert into Inventario_tiene_Categoria (Referencia_producto_ID,categoria_ID) values (%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.referenciaProducto,categoria.id))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def removerCategoria(self, producto, categoria):
        try:
            sql='delete from Inventario_tiene_Categoria where (Referencia_producto_ID,categoria_ID) values (%s,%s)'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.referenciaProducto,categoria.id))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e