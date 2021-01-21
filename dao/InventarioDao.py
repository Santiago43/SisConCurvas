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
        - producto : que es el producto que se agregará al inventario 
        """
        try:
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(producto.referenciaProducto,producto.descripcion,producto.urlImagen,producto.stock,producto.precioCosto,producto.precioVenta,producto.precioMayorista)
            sql='''insert into Inventario(Referencia_Producto_ID,Descripcion,Url_imagen,Stock,Precio_costo,Precio_venta,Precio_mayorista)
            values(%s,%s,%s,%s,%s,%s,%s);'''
            cursor.execute(sql,args)
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
            sql= "select * from Inventario where Referencia_Producto_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id,))
            result = cursor.fetchone()
            producto=None
            if result is not None:
                producto = Inventario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list())
                sql2='''select c.* from Categoria as c
                inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
                where ic.Inventario_Referencia_Producto_ID=%s;'''
                cursor.execute(sql2,(id,))
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
            Precio_venta=%s,
            Precio_mayorista=%s
            where Referencia_Producto_ID=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.descripcion,producto.urlImagen,producto.stock,producto.precioCosto,producto.precioVenta,producto.precioMayorista,producto.referenciaProducto))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def eliminarproducto(self,producto):
        """
        Método que permite eliminar un producto mediante su id
        - producto : que es el producto que se elinará
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql="delete from Inventario where producto_ID='"+str(producto.referenciaProducto)+"';"
            
            cursor.execute(sql)
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e

    def agregarCategoria(self, producto, categoria):
        """
        Método que permite agregar categoría a un producto
        - producto : que es el producto al que se le agregará la categoría
        - categoria: que es el categoria que se le agregará al producto
        """
        try:
            sql='insert into Inventario_tiene_Categoria (Inventario_Referencia_producto_ID,categoria_ID) values (%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(producto.referenciaProducto,categoria.id))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def removerCategoria(self, producto, categoria):
        """
        Método que permite eliminar categoría de un producto
        - producto : que es el producto al que se le removerá la categoría
        - categoria: que es el categoría que se le removerá al producto
        """
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

    def consultarProductos(self):
        """
        Método que permite consultar la lista de productos existentes 
        """
        try:
            sql= "select * from Inventario;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results=cursor.fetchall()
            productos=[]
            for result in results:
                producto = Inventario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list())
                productos.append(producto)
            for producto in productos:
                sql2='''select c.* from Categoria as c
                inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
                where ic.Inventario_Referencia_Producto_ID="'''+producto.referenciaProducto+'''";'''
                cursor.execute(sql2)
                for row in cursor:
                    producto.categorias.append(Categoria(row[0],row[1],row[2]))           
            super().cerrarConexion(cursor,cnx)
            return productos
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e