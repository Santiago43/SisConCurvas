import secrets

from dao.models import Usuario
from dao.UsuariosDao import UsuariosDao
from dao.DireccionDao import DireccionDao
from dao.RolesDao import RolesDao
from dao.PermisoDao import PermisoDao
def crearUsuario(data,response_object):
    """
    Función que permite crear usuarios
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    primerNombre=data.get('primerNombre')
    segundoNombre=data.get('segundoNombre')
    primerApellido=data.get('primerApellido')
    segundoApellido=data.get('segundoApellido')
    tipoDocumento=data.get('tipoDocumento')
    documento=data.get('documento')
    telefono=data.get('telefono')
    correo=data.get('correo')
    direcciones=data.get('direcciones')
    rol_ID=data.get('rol_ID')
    contraseña=data.get('contraseña')
    urlImagen=data.get('urlImagen')
    nombreUsuario=data.get('usuario')
    token = secrets.token_urlsafe(100)
    usuario=Usuario(None,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,list(),rol_ID,contraseña,None,list(),urlImagen,tipoDocumento,documento,True,token,nombreUsuario)
    dao = UsuariosDao()
    direccionDao=DireccionDao()
    if(dao.consultarUsuario(documento) is None or dao.consultarUsuarioPorTelefono(telefono) is None):
        if(dao.crearUsuario(usuario)):
            #for direccionDict in direcciones:
            #    direccionDao.consultarDireccion(direccionDict['idDireccion'])
            response_object['mensaje']="usuario creado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear usuario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe un usuario con ese documento, con ese correo o con ese teléfono"
    return response_object

def consultarUsuarios(response_object):
    """
    Función que permite consultar todos los usuarios. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = UsuariosDao()
    rolesDao=RolesDao()
    usuarios=dao.consultarUsuarios()
    usuariosJson=list()
    for usuario in usuarios:
        usuarioDict=usuario.__dict__
        permisos=usuario.permisos
        usuarioDict['permisos']=list()
        for permiso in permisos:
            permisoDict=permiso.__dict__
            usuarioDict['permisos'].append(permisoDict)
        rolUsuario=rolesDao.consultarRol(usuarioDict['rol_ID'])
        rolDict=rolUsuario.__dict__
        permisos=rolUsuario.permisos
        rolDict['permisos']=list()
        for permiso in permisos:
            permisoDict=permiso.__dict__
            rolDict['permisos'].append(permisoDict)
        usuarioDict['rol']=rolDict
        direccionesDict= list()
        for direccion in usuario.direcciones:
            direccionesDict.append(direccion.__dict__)
        usuarioDict['direcciones']=direccionesDict
        usuarioDict.pop('contraseña')
        usuarioDict.pop('rol_ID')
        usuarioDict.pop('token')
        usuariosJson.append(usuarioDict)
    response_object['usuarios']=usuariosJson
    return response_object

def login(data,response_object):
    dao = UsuariosDao()
    nombreUsuario = data.get('usuario')
    contraseña=data.get('contraseña')
    usuario=dao.consultarUsuarioPorCredenciales(nombreUsuario,contraseña)
    if (usuario is not None):
        usuarioDict=usuario.__dict__
        rolesDao=RolesDao()
        rol=rolesDao.consultarRol(usuarioDict['rol_ID'])
        rolDict=rol.__dict__
        permisosUsuario=usuario.permisos
        permisosUsuarioDict=list()
        for permiso in permisosUsuario:
            permisoDict=permiso.__dict__
            permisosUsuarioDict.append(permisoDict)
        permisosRolDict=list()
        permisosRol=rol.permisos
        for permiso in permisosRol:
            permisoDict=permiso.__dict__
            permisosRolDict.append(permisoDict)
        rolDict['permisos']=permisosRolDict
        usuarioDict['rol']=rolDict
        usuarioDict['permisos']=permisosUsuarioDict
        usuarioDict.pop('contraseña')
        usuarioDict.pop('rol_ID')
        response_object['usuario']=usuarioDict
    else:
        response_object['tipo']='error'
        response_object['mensaje']='Usuario o contraseña incorrectos'
    return response_object

def actualizarUsuario(data,response_object,documento):
    """
    Función que permite actualizar datos de un usuario.
    Parámetros:
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor.
    - documento: que es el documento del usuario a actualizar. 

    Retorna el response_object modificado
    """
    dao = UsuariosDao()
    usuario=dao.consultarUsuario(documento)
    primerNombre=data.get('primerNombre')
    segundoNombre=data.get('segundoNombre')
    primerApellido=data.get('primerApellido')
    segundoApellido=data.get('segundoApellido')
    tipoDocumento=data.get('tipoDocumento')
    documento=data.get('documento')
    telefono=data.get('telefono')
    correo=data.get('correo')
    rol_ID=data.get('rol_ID')
    #contraseña=data.get('contraseña')
    urlImagen=data.get('urlImagen')
    estado=data.get('estado')
    
    if(usuario is not None):
        if primerNombre is not None:
            usuario.primerNombre=primerNombre
        if segundoNombre is not None:
            usuario.segundoNombre=segundoNombre
        if primerApellido is not None:
            usuario.primerApellido=primerApellido
        if segundoApellido is not None:
            usuario.segundoApellido=segundoApellido
        if tipoDocumento is not None:
            usuario.tipoDocumento=tipoDocumento
        if urlImagen is not None:
            usuario.urlImagen=usuario.urlImagen
        if telefono is not None:
            usuario.telefono=telefono
        if rol_ID is not None:
            usuario.rol_ID=rol_ID
        if correo is not None:
            usuario.correo=correo
        if estado is not None:
            usuario.estado=estado
        if(dao.actualizarusuario(usuario)):
            response_object['mensaje']="usuario actualizado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar usuario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un usuario con ese documento o con ese correo"
    return response_object

def eliminarUsuario(response_object,documento):
    """
    Función que permite eliminar datos de un usuario.
    
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor.
    - documento: que es el documento del usuario a actualizar. 
    
    Retorna el response_object modificado
    """
    dao = UsuariosDao()
    usuario=dao.consultarUsuario(documento)
    if(usuario is not None):
        if(dao.eliminarusuario(usuario)):
            response_object['mensaje']="usuario eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar usuario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un usuario con ese documento o con ese correo"
    return response_object

def agregarPermisoAUsuario(response_object,documento,permiso_ID):
    permisoDao=PermisoDao()
    usuarioDao=UsuariosDao()
    permiso=permisoDao.consultarPermiso(permiso_ID)
    usuario=usuarioDao.consultarUsuario(documento)
    if permiso and usuario is not None:
        if usuarioDao.agregarPermiso(usuario,permiso):
            response_object['mensaje']="Permiso "+permiso.nombre+" agregado al usuario: "+usuario.primerNombre+" "+usuario.primerApellido
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al asignar permiso. El usuario probablemente ya tenga el permiso"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ese usuario o ese permiso no existe"
    return response_object

def removerPermisoAUsuario(response_object,documento,permiso_ID):
    permisoDao=PermisoDao()
    usuarioDao=UsuariosDao()
    permiso=permisoDao.consultarPermiso(permiso_ID)
    usuario=usuarioDao.consultarUsuario(documento)
    if permiso and usuario is not None:
        if usuarioDao.removerPermiso(usuario,permiso):
            response_object['mensaje']="Permiso "+permiso.nombre+" removido al usuario: "+usuario.primerNombre+" "+usuario.primerApellido
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al retirar permiso. Probablemente no tenga este permiso."
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ese usuario o ese permiso no existe"
    return response_object

def validarUsuario(nombrePermiso,token):
    usuarioDao=UsuariosDao()
    usuario=usuarioDao.consultarUsuarioPorToken(token)
    if usuario is None:
        return (False,None)
    else:
        rolDao=RolesDao()
        rol=rolDao.consultarRol(usuario.rol_ID)
        for permiso in usuario.permisos:
            if permiso.nombre==nombrePermiso:
                return (True,usuario)
        for permiso in rol.permisos:
            if permiso.nombre==nombrePermiso:
                return (True,usuario)
    return (False,None)
    

def validarUsuarioLogueadoPorToken(token):
    usuarioDao=UsuariosDao()
    return usuarioDao.consultarUsuarioPorToken(token) is not None

def validarUsuarioPorToken(token):
    usuarioDao = UsuariosDao()
    usuario = usuarioDao.consultarUsuarioPorToken(token) 
    usuarioDict=usuario.__dict__
    permisos=usuario.permisos
    usuarioDict['permisos']=list()
    for permiso in permisos:
        permisoDict=permiso.__dict__
        usuarioDict['permisos'].append(permisoDict)
    rolUsuario=rolesDao.consultarRol(usuarioDict['rol_ID'])
    rolDict=rolUsuario.__dict__
    permisos=rolUsuario.permisos
    rolDict['permisos']=list()
    for permiso in permisos:
        permisoDict=permiso.__dict__
        rolDict['permisos'].append(permisoDict)
    usuarioDict['rol']=rolDict
    direccionesDict= list()
    for direccion in usuario.direcciones:
        direccionesDict.append(direccion.__dict__)
    usuarioDict['direcciones']=direccionesDict
    usuarioDict.pop('contraseña')
    usuarioDict.pop('rol_ID')
    usuarioDict.pop('token')
    return usuarioDict