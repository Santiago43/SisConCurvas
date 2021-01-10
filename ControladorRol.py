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
    Parámetros
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
        print(rolDict)
    response_object['Roles']=rolesJson
    return response_object

def agregarPermisoARol(data,response_object):
    return response_object
