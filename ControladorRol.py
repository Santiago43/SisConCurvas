from dao.models import Rol
from dao.RolesDao import RolesDao
def crearRol(data,response_object):
    """
    Función que permite crear roles

    Parámetros:
    
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    nombreRol=data.get('nombreRol')
    dao=RolesDao()
    rol=Rol(None,nombreRol,[])
    if(dao.consultarRolPorNombre(nombreRol) is None):
        if(dao.crearRol(rol)):
            response_object['mensaje']="rol creado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear rol"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe un rol con ese nombre"
    return response_object

def consultarRoles(response_object):
    """
    Función que permite consultar todos los roles

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao=RolesDao()
    roles=dao.consultarRoles()
    rolesJson=list()
    for rol in roles:
        rolDict=rol.__dict__
        permisos=rol.permisos
        rolDict['permisos']=list()
        for permiso in permisos:
            permisoDict=permiso.__dict__
            rolDict['permisos'].append(permisoDict)
        rolesJson.append(rolDict)
    response_object['Roles']=rolesJson
    return response_object

def actualizarRol(data,response_object,rol_ID):
    """
    Función que permite actualizar un rol
    
    Parámetros:
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - rol_ID: que es el id del rol que se quiere actualizar

    Retorna el response_object modificado
    """
    dao=RolesDao()
    rol=dao.consultarRol(rol_ID)
    if rol is not None:
        nombre=data.get("nombre")
        if nombre is not None:
            rol.nombre=nombre
        if dao.actualizarRol(rol):
            response_object['mensaje']="Rol actualizado"
        else:
            response_object['tipo']="Error"
            response_object['mensaje']="Error al actualizar el rol"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="No existe un rol con ese ID"
    return response_object

def agregarPermisoARol(data,response_object):
    return response_object

def removerPermisoARol(response_object):
    return response_object