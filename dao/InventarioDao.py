import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Inventario
from dao.models import Categoria
class InventarioDao(dao):
    """
    Clase de objeto de acceso a datos que maneja el inventario
    """
    def crearProducto(self,producto):
        """
        Método que permite hacer el registro de un producto
        Parámetros:
        - producto : que es el producto ue se agregará al inventario 
        """
        try:
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=[producto.referenciaProducto,producto.descripcion,producto.urlImagen,producto.stock,producto.precioCosto,producto.precioVenta,producto.categorias[0].idCategoria]
            cursor.callproc("insertarProducto",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarProducto(self,id):
        """
        Método que permite consultar un producto mediante su ID
        Parámetros:
        - id : que es el ID de producto 
        """
        try:
            sql= "select * from inventario where Referencia_Producto_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id))
            result = cursor.fetchone()
            producto = Inventario(result[0],result[1],result[2],result[3],result[4],result[5])
            sql2='''select c.* from categoria as c
            inner join Inventario_tiene_categoria as ic on c.Categoria_ID=ic.Categoria_ID
            where Inventario_Referencia_Producto_ID=%s;'''
            cursor.execute(sql2,(id))
            for row in cursor:
                producto.categorias.append(Categoria(row[0],row[1],row[2]))           
            super().cerrarConexion(cursor,cnx)
            return producto
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
            sql="delete from producto where producto_ID=%s;"
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
            sql='insert into Inventario_tiene_categoria (Referencia_producto_ID,categoria_ID) values (%s,%s);'
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
            sql='delete from Inventario_tiene_categoria where (Referencia_producto_ID,categoria_ID) values (%s,%s)'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.referenciaProducto,categoria.id))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e