import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Usuario
from dao.models import Permiso
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos que maneja los usuarios y sus permisos
    """
    def crearUsuario(self,usuario):
        """
        Método que permite hacer el registro de un usuario
        Parámetros:
        - usuario : que es el usuario que se registrará 
        """
        try:
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=[usuario.primerNombre,usuario.segundoNombre,usuario.primerApellido,usuario.segundoApellido,usuario.tipoDocumento,usuario.documento,usuario.telefono,usuario.correo,usuario.rol_ID,usuario.contraseña]
            cursor.callproc("insertarUsuario",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            raise e

    def consultarUsuario(self,cedula):
        """
        Método que permite consultar un usuario mediante su cedula
        Parámetros:
        - cedula : que es el documento del usuario 
        """
        try:
            sql= 'select * from persona as p inner join usuario as u on u.Persona_ID=p.Persona_ID where Documento=%s;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(cedula))
            result = cursor.fetchone()
            usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],list())
            sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID=%s;'
            cursor.execute(sql2,(usuario.usuario_ID))
            for row in cursor:
                usuario.permisos.append(Permiso(row[0],row[1]))
            return usuario
        except Exception as e:
            raise e

    def actualizarusuario(self,usuario):
        """
        Método que permite actualizar un usuario (su nombre)
        Parámetros:
        - usuario : que es el usuario que se actualizará
        """
        try:
            sql = 'update persona as p, usuario as u set '
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
            args=(usuario.primerNombre,usuario.segundoNombre,usuario.PrimerApellido,usuario.segundoApellido,usuario.tipoDocumento,usuario.telefono,usuario.correo,usuario.documento)
            cursor.execute(sql,args)
        except Exception as e:
            raise e

    def eliminarusuario(self,usuario):
        """
        Método que permite eliminar un usuario mediante su id
        - usuario : que es el usuario que se elinará
        """
        try:
            sql="delete from Usuario where usuario_ID=%s;"
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(usuario.usuario_ID))
            return True
        except Exception as e:
            raise e

    def agregarPermiso(self, usuario, permiso):
        """
        Método que permite agregar permiso a un usuario
        - usuario : que es el usuario al que se le agregará el permiso
        - permiso : que es el permiso que se le agregará al usuario
        """
        try:
            sql='insert into Usuario_tiene_Permiso (usuario_ID,Permiso_ID) values (%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(usuario.usuario_ID,permiso.permiso_ID))
            return True
        except Exception as e:
            raise e
        
    def removerPermiso(self, usuario, permiso):
        try:
            sql='delete from Usuario_tiene_Permiso where (Usuario_ID,Permiso_ID) =(%s,%s);'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(usuario.usuario_ID,permiso.permiso_ID))
            return True
        except Exception as e:
            raise e
    def consultarUsuarios(self):
        """
        Método que permite consultar la lista de usuarios existentes
        """
        try:
            sql= 'select * from persona as p inner join usuario as u on u.Persona_ID=p.Persona_ID;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            usuarios=list()
            results = cursor.fetchall()
            for result in results:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],list())
                sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID=%s;'
                cursor.execute(sql2,(usuario.usuario_ID))
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
            return usuarios
        except Exception as e:
            raise e