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
    usuario=Usuario(None,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo,None,contraseña,rol_ID,None,None,urlImagen)
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
    correo = data.get_json('correo')
    contraseña=data.get_json('contraseña')
    usuario=dao.consultarUsuarioPorCredenciales(correo,contraseña)
    if (usuario is not None):
        usuarioDict=usuario.__dict__
        rolesDao=RolesDao()
        rol=rolesDao.consultarRol(usuarioDict['rol_ID'])
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