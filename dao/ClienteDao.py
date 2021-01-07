import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Cliente

class ClienteDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los clientes y sus permisos
    """
    def crearcliente(self,cliente):
        """
        Método que permite hacer el registro de un cliente
        Parámetros:
        - cliente : que es el cliente que se registrará 
        """
        try:
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=[cliente.primerNombre,cliente.segundoNombre,cliente.primerApellido,cliente.segundoApellido,cliente.tipoDocumento,cliente.documento,cliente.telefono,cliente.correo,cliente.tipoCliente]
            cursor.callproc("insertarCliente",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarcliente(self,cedula):
        """
        Método que permite consultar un cliente mediante su cedula
        Parámetros:
        - cedula : que es la cédula de cliente 
        """
        try:
            sql= 'select * from Persona as p inner join Cliente as c on c.Persona_ID=p.Persona_ID where Documento=%s;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(cedula))
            result = cursor.fetchone()
            cliente = Cliente(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10])
            return cliente
        except Exception as e:
            raise e

    def actualizarcliente(self,cliente):
        """
        Método que permite actualizar un cliente (su nombre)
        Parámetros:
        - cliente : que es el cliente que se actualizará
        """
        try:
            sql = 'update Persona as p, Cliente as u set '
            sql+='p.Primer_nombre="%s, '
            sql+='p.Segundo_nombre=%s, '
            sql+='p.Primer_apellido=%s, '
            sql+='p.Segundo_apellido=%s, '
            sql+='p.Tipo_documento=%s, '
            sql+='p.Telefono=%s, '
            sql+='where p.Documento=%s and p.Persona_ID=u.Persona_ID;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(cliente.primerNombre,cliente.segundoNombre,cliente.PrimerApellido,cliente.segundoApellido,cliente.tipoDocumento,cliente.telefono,cliente.correo)
            cursor.execute(sql,)
        except Exception as e:
            raise e

    def eliminarcliente(self,cliente):
        """
        Método que permite eliminar un cliente mediante su id
        - cliente : que es el cliente que se elinará
        """
        try:
            sql="delete from cliente where cliente_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(cliente.idcliente))
            return True
        except Exception as e:
            raise e
