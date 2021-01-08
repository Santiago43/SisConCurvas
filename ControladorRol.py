from dao.models import Rol
def crearRol(dao,data,response_object):
    nombreRol=data.get('nombreRol')
        
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
def consultarRoles(dao, response_object):
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