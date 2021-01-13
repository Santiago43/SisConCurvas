import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Cliente
from dao.models import Direccion

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

    def consultarCliente(self,telefono):
        """
        Método que permite consultar un cliente mediante su telefono
        Parámetros:
        - telefono : que es el teléfono del cliente 
        """
        try:
            sql= '''select p.*,tipo_cliente,c.Cliente_ID from Persona as p 
            inner join Cliente as c 
            on c.Persona_ID=p.Persona_ID
            where p.Telefono="'''+str(telefono)+'''";'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            cliente = Cliente(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8])
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
            sql = '''update Persona as p, Cliente as c
            set p.Primer_nombre=%s, 
            p.Segundo_nombre=%s, 
            p.Primer_apellido=%s, 
            p.Segundo_apellido=%s,
            p.Telefono=%s,
            p.correo=%s,
            c.tipo_cliente=%s
            where p.Telefono=%s and p.Persona_ID=c.Persona_ID;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(cliente.primerNombre,cliente.segundoNombre,cliente.PrimerApellido,cliente.segundoApellido,cliente.telefono,cliente.correo,cliente.tipoCliente)
            cursor.execute(sql,args)
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
            cursor.execute(sql,(cliente.cliente_ID))
            return True
        except Exception as e:
            raise e
    def consultarClientes(self):
        """
        Método que permite consultar un cliente mediante su telefono
        Parámetros:
        - telefono : que es el teléfono del cliente 
        """
        try:
            sql= '''select p.*,tipo_cliente,c.Cliente_ID from Persona as p 
            inner join Cliente as c 
            on c.Persona_ID=p.Persona_ID;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            clientes=list()
            for result in results:
                cliente = Cliente(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8])
                sql2='''select d.* from Direccion as d
                inner join Persona_tiene_Direccion as pd on d.Direccion_id
                inner join Persona as p on p.Persona_ID=pd.Persona_ID
                where p.Telefono="'''+str(cliente.telefono)+'''";'''
                cursor.execute(sql2)
                for row in cursor:
                    direccion=Direccion(row[0],row[1],row[2],row[3],row[4])
                    cliente.direcciones.append(direccion)
                clientes.append(cliente)
            return clientes
        except Exception as e:
            raise e