from dao.models import Usuario
from dao.UsuariosDao import UsuariosDao
from dao.DireccionDao import DireccionDao
from dao.RolesDao import RolesDao
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
    usuario=Usuario(None,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo,None,contraseña,rol_ID,None,None,urlImagen,True)
    dao = UsuariosDao()
    direccionDao=DireccionDao()
    if(dao.consultarUsuario(documento) is None):
        if(dao.crearUsuario(usuario)):
            for direccionDict in direcciones:
                direccionDao.consultarDireccion(direccionDict['idDireccion'])
            response_object['mensaje']="usuario creado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear usuario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe un usuario con ese documento o con ese correo"
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
        usuariosJson.append(usuarioDict)
    response_object['usuarios']=usuariosJson
    return response_object

def login(data,response_object):
    dao = UsuariosDao()
    correo = data.get('correo')
    contraseña=data.get('contraseña')
    usuario=dao.consultarUsuarioPorCredenciales(correo,contraseña)
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