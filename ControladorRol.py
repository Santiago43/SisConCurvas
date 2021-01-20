from dao.models import Rol,Control_rol
from dao.RolesDao import RolesDao
from dao.PermisoDao import PermisoDao
from dao.ControlDao import ControlDao

def crearRol(data,response_object,usuario):
    """
    Función que permite crear roles

    Parámetros:
    
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - usuario: que es el usuario que crea el rol

    Retorna el response_object modificado
    """
    nombreRol=data.get('nombre')
    dao=RolesDao()
    rol=Rol(None,nombreRol,[])
    if(dao.consultarRolPorNombre(nombreRol) is None):
        if(dao.crearRol(rol)):
            response_object['mensaje']="rol creado"
            rol=dao.consultarRolPorNombre(nombreRol)
            texto="El usuario "+usuario.primerNombre+" "+usuario.primerApellido+" creó el rol '"+nombreRol+"'"
            control=Control_rol(None,rol.idRol,usuario.usuario_ID,None,1,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
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

def actualizarRol(data,response_object,rol_ID,editor):
    """
    Función que permite actualizar un rol
    
    Parámetros:
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - rol_ID: que es el id del rol que se quiere actualizar
    - editor: Usuario que realiza la acción

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
            rol=dao.consultarRolPorNombre(nombre)
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" modificó el rol '"+nombre+"'"
            control=Control_rol(None,rol.idRol,editor.usuario_ID,None,2,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="Error"
            response_object['mensaje']="Error al actualizar el rol"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="No existe un rol con ese ID"
    return response_object

def eliminarRol(response_object,rol_ID,editor):
    """
    Función que permite eliminar un rol
    
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    - rol_ID: que es el id del rol que se quiere actualizar
    - editor: Usuario que realiza la acción

    Retorna el response_object modificado
    """
    dao=RolesDao()
    rol=dao.consultarRol(rol_ID)
    nombreRol = rol.nombre
    if rol is not None:
        if dao.eliminarRol(rol):
            response_object['mensaje']="Rol eliminado"
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" eliminó el rol '"+nombreRol+"'"
            control=Control_rol(None,rol_ID,editor.usuario_ID,None,3,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="Error"
            response_object['mensaje']="Error al eliminar el rol"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="No existe un rol con ese ID"
    return response_object

def agregarPermisoARol(response_object,rol_ID,permiso_ID,editor):
    """
    Función que permite agregar un permiso a un rol

    Parámetros:
    - response_object: referencia a la respuesta del servidor
    - rol_ID: Id del rol al que se quiere agregar el permiso
    - permiso_ID: Permiso que se desee agregar
    - editor: Usuario que realiza la acción

    Retorna el response_object modificado
    """
    permisoDao=PermisoDao()
    rolDao=RolesDao()
    permiso = permisoDao.consultarPermiso(permiso_ID)
    rol=rolDao.consultarRol(rol_ID)
    if permiso and rol is not None:
        if rolDao.agregarPermiso(rol,permiso):
            response_object['mensaje']="Permiso '"+permiso.nombre+"' agregado al rol "+rol.nombre
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" agregó el permiso '"+permiso.nombre+"' al rol '"+rol.nombre+"'"
            control=Control_rol(None,rol.idRol,editor.usuario_ID,None,1,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al asignar permiso"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe ese permiso o ese rol"
    return response_object

def removerPermisoARol(response_object,rol_ID,permiso_ID, editor):
    """
    Función que permite remover un permiso a un rol

    Parámetros:
    - response_object: referencia a la respuesta del servidor
    - rol_ID: Id del rol al que se quiere eliminar el permiso
    - permiso_ID: Permiso que se desee remover
    - editor: Usuario que realiza la acción

    Retorna el response_object modificado
    """
    permisoDao=PermisoDao()
    rolDao=RolesDao()
    permiso = permisoDao.consultarPermiso(permiso_ID)
    rol=rolDao.consultarRol(rol_ID)
    if permiso and rol is not None:
        if rolDao.removerPermiso(rol,permiso):
            response_object['mensaje']="Permiso '"+permiso.nombre+"' removido del rol "+rol.nombre
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" removió el permiso '"+permiso.nombre+"' del rol '"+rol.nombre+"'"
            control=Control_rol(None,rol.idRol,editor.usuario_ID,None,3,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al asignar permiso. Probablemente ya tenga este permiso."
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe ese permiso o ese rol"
    return response_object