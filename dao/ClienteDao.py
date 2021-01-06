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
            args=[cliente.primerNombre,cliente.segundoNombre,cliente.primerApellido,cliente.segundoApellido,cliente.tipoDocumento,cliente.documento,cliente.telefono,cliente.correo,cliente.rol_ID,cliente.contraseña]
            cursor.callproc("insertarcliente",args)
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
            sql= 'select * from persona as p inner join cliente as u on u.Persona_ID=p.Persona_ID where Documento=1234567890;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(id))
            result = cursor.fetchone()
            cliente = cliente(result[0],result[1],None)
            sql2='select p.* from cliente_tiene_permiso as rp inner join cliente as r on r.cliente_ID=rp.cliente_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.cliente_ID=%s;'
            cursor.execute(sql2,(id))
            for row in cursor:
                cliente.permisos.append(Permiso(row[0],row[1]))
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
            sql = 'update persona as p, cliente as u set '
            sql+='p.Primer_nombre="%s, '
            sql+='p.Segundo_nombre=%s, '
            sql+='p.Primer_apellido=%s, '
            sql+='p.Segundo_apellido=%s, '
            sql+='p.Tipo_documento=%s, '
            sql+='p.Telefono=%s, '
            sql+='p.correo=%s, '
            sql+='u.Rol_ID=%s, '
            sql+='where p.Documento=%s and p.Persona_ID=u.Persona_ID;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(cliente.primerNombre,cliente.segundoNombre,cliente.PrimerApellido,cliente.segundoApellido,cliente.tipoDocumento,cliente.telefono,cliente.correo,)
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

    def agregarPermiso(self, cliente, permiso):
        """
        Método que permite agregar permiso a un cliente
        - cliente : que es el cliente al que se le agregará el permiso
        - permiso : que es el permiso que se le agregará al cliente
        """
        try:
            sql='insert into cliente_tiene_permiso (cliente_ID,Permiso_ID) values (%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(cliente.id,permiso.id))
            return True
        except Exception as e:
            raise e
        
    def removerPermiso(self, cliente, permiso):
        try:
            sql='delete from cliente_tiene_permiso where (cliente_ID,Permiso_ID) =(%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(cliente.id,permiso.id))
            return True
        except Exception as e:
            raise e