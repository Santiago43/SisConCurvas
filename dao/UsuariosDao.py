import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Usuario
from dao.models import Permiso
from dao.models import Direccion
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
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            args=[usuario.primerNombre,usuario.segundoNombre,usuario.primerApellido,usuario.segundoApellido,usuario.tipoDocumento,usuario.documento,usuario.telefono,usuario.correo,usuario.rol_ID,usuario.contraseña,usuario.urlImagen,usuario.token]
            cursor.callproc("insertarUsuario",args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cnx,cursor)
            raise e

    def consultarUsuario(self,documento):
        """
        Método que permite consultar un usuario mediante su documento
        Parámetros:
        - documento : que es el documento del usuario 
        """
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token
            from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID where u.Documento='''+str(documento)+''';'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            usuario=None
            if result is not None:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
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
            sql = 'update Persona as p, Usuario as u set '
            sql+='p.Primer_nombre=%s, '
            sql+='p.Segundo_nombre=%s, '
            sql+='p.Primer_apellido=%s, '
            sql+='p.Segundo_apellido=%s, '
            sql+='p.Tipo_documento=%s, '
            sql+='p.Telefono=%s, '
            sql+='p.correo=%s, '
            sql+='u.Rol_ID=%s, '
            sql+='u.estado=%s'
            sql+='where p.Documento=%s and p.Persona_ID=u.Persona_ID;'
            cnx=super().connectDB()
            cursor=cnx.cursor()
            args=(usuario.primerNombre,usuario.segundoNombre,usuario.PrimerApellido,usuario.segundoApellido,usuario.tipoDocumento,usuario.telefono,usuario.correo,usuario.estado,usuario.documento)
            cursor.execute(sql,args)
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
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
            cursor.execute(sql,(usuario.usuario_ID,))
            return True
        except Exception as e:
            raise e

    def agregarPermiso(self, usuario, permiso):
        """
        Método que permite agregar permiso a un usuario
        - usuario : que es el usuario al que se le agregará el permiso
        - permiso : que es el permiso que se le agregará al usuario
        """
        for perm in usuario.permisos:
                if perm.permiso_ID==permiso.permiso_ID:
                    return False
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql='insert into Usuario_tiene_Permiso (usuario_ID,Permiso_ID) values (%s,%s);'
            cursor.execute(sql,(usuario.usuario_ID,permiso.permiso_ID))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def removerPermiso(self, usuario, permiso):
        if len(usuario.permisos)==0:
            return False
        contador=0
        for perm in usuario.permisos:
            if perm.permiso_ID!=permiso.permiso_ID:
                contador+=1
        if contador==len(usuario.permisos):
            return False
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql='delete from Usuario_tiene_Permiso where (Usuario_ID,Permiso_ID) =(%s,%s);'
            cursor.execute(sql,(usuario.usuario_ID,permiso.permiso_ID))
            cnx.commit()
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarUsuarios(self):
        """
        Método que permite consultar la lista de usuarios existentes
        """
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token
            from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            usuarios=list()
            results = cursor.fetchall()
            for result in results:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from Usuario_tiene_Permiso as up inner join Usuario as u on u.usuario_ID=up.usuario_ID inner join Permiso as p on p.Permiso_ID=up.Permiso_ID where u.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
                sql3='''select d.* from Direccion as d
                inner join Persona_tiene_Direccion as pd on d.Direccion_id
                inner join Persona as p on p.Persona_ID=pd.Persona_ID
                inner join Usuario as u on u.Persona_ID=p.Persona_ID
                where u.Documento='''+str(usuario.documento)+''';'''
                cursor.execute(sql3)
                for row in cursor:
                    direccion = Direccion(row[0],row[1],row[2],row[3],row[4])
                    usuario.direcciones.append(direccion)
                usuarios.append(usuario)
            super().cerrarConexion(cursor,cnx)
            return usuarios
        except Exception as e:
            raise e
    def agregarDireccion(self,usuario,direccion):
        """
        Método que permite agregar una dirección a un usuario
        - usuario: que es el usuario al que se le agregará la dirección
        - dirección: que es la dirección que se le agregará al usuario
        """
        try:
            sql= ''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            super().cerrarConexion(cursor,cnx)
            return True
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarUsuarioPorCredenciales(self,correo,contraseña):
        """
        Método que permite consultar un usuario mediante su correo y contraseña
        Parámetros:
        - correo: que es el correo del usuario
        - contraseña: que es la contraseña del usuario  
        """
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token from Usuario as u
            inner join Persona as p on p.Persona_ID=u.Persona_ID
            where p.Correo = %s and u.Contraseña=sha(%s);'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(correo,contraseña))
            result = cursor.fetchone()
            usuario=None
            if result is not None:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from Usuario_tiene_Permiso as rp inner join Usuario as r on r.Usuario_ID=rp.Usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
            super().cerrarConexion(cursor,cnx)
            return usuario
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarUsuarioPorToken(self,token):
        """
        Método que permite consultar un usuario mediante su token
        Parámetros:
        - token : que es el token del usuario 
        """
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token
            from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID where u.token=%s;'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql,(token,))
            result = cursor.fetchone()
            usuario=None
            if result is not None:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
            super().cerrarConexion(cursor,cnx)
            return usuario
        except Exception as e:
            super().cerrarConexion(cursor,cnx)
            raise e
    def consultarUsuarioPorTelefono(self,telefono):
        """
        Método que permite consultar un usuario mediante su token
        Parámetros:
        - telefono : que es el token del usuario 
        """
        cnx=super().connectDB()
        cursor=cnx.cursor()
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token
            from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID where p.telefono=%s;''' 
            cursor.execute(sql,(telefono,))
            result = cursor.fetchone()
            usuario=None
            if result is not None:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
            super().cerrarConexion(cnx,cursor)
            return usuario
        except Exception as e:
            super().cerrarConexion(cnx,cursor)
            raise e
    def consultarUsuarioPorID(self,id):
        """
        Método que permite consultar un usuario mediante su documento
        Parámetros:
        - documento : que es el documento del usuario 
        """
        try:
            sql= '''select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token
            from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID where u.usuario_ID='''+str(id)+''';'''
            cnx=super().connectDB()
            cursor=cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            usuario=None
            if result is not None:
                usuario = Usuario(result[0],result[1],result[2],result[3],result[4],result[5],result[6],list(),result[7],result[8],result[9],list(),result[10],result[11],result[12],result[13],result[14])
                sql2='select p.* from usuario_tiene_permiso as rp inner join usuario as r on r.usuario_ID=rp.usuario_ID inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.usuario_ID='+str(usuario.usuario_ID)+';'
                cursor.execute(sql2)
                for row in cursor:
                    usuario.permisos.append(Permiso(row[0],row[1]))
            return usuario
        except Exception as e:
            raise e