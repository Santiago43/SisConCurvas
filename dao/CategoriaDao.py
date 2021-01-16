import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Categoria
class CategoriaDao(dao):
    """
    Clase de objeto de acceso a datos que maneja las categorías
    """
    def crearCategoria(self,categoria):
        """
        Método que permite hacer el registro de una categoría
        Parámetros:
        - categoria : que es el categoria que se registrará 
        """
        try:
            sql= 'insert into Categoria(Nombre,Padre_categoria_ID) values (%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(categoria.nombre,categoria.idPadre))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e
        
    def consultarCategoria(self,id):
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

    def actualizarcategoria(self,categoria):
        """
        Método que permite actualizar un categoria (su nombre)
        Parámetros:
        - categoria : que es el categoria que se actualizará
        """
        try:
            sql = 'update Categoria set Nombre=%s, Padre_categoria_ID=%s where categoria_ID = %s;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(categoria.nombre,categoria.idPadre,categoria.id))
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def eliminarcategoria(self,categoria):
        """
        Método que permite eliminar un categoria mediante su id
        - categoria : que es el categoria que se elinará
        """
        try:
            sql="delete from Categoria where categoria_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(categoria.id,))
            cursor.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarCategorias(self):
        """
        Método que permite consultar las categorias
        """
        try:
            categorias = list()
            sql= "select * from Categoria;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                categoria = Categoria(i[0],i[1],i[2])
                categorias.append(categoria)
            super().cerrarConexion(cursor,cnx)
            return categorias
        except Exception as e:
            raise e
    def consultarCategoriaPorNombre(self,nombre):
        """
        Método que permite consultar un categoria mediante su nombre
        Parámetros:
        - nombre : que es el nombre de categoria 
        """
        try:
            sql= 'select * from Categoria where Nombre="'+str(nombre)+'";'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            categoria = Categoria(result[0],result[1],result[2])
            super().cerrarConexion(cursor,cnx)
            return categoria
        except Exception as e:
            raise e