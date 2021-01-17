from dao.DireccionDao import DireccionDao
from dao.OrdenVentaDao import OrdenDao
from dao.UsuariosDao import UsuariosDao
from dao.EmpaqueDao import EmpaqueDao
from dao.models import Empaque

def crearEmpaque(data,response_object):
    """
    Función que permite crear un empaque
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    ordenVenta_ID=data.get('ordenVenta_ID')
    usuario_ID=data.get('usuario_ID')
    numero_prendas=data.get('numero_prendas')
    estado=data.get('estado')
    observaciones=data.get('observaciones')
    motivo_ID=data.get('motivo_ID')
    dao=EmpaqueDao()
    empaque = Empaque(None,ordenVenta_ID,motivo_ID,usuario_ID,numero_prendas,estado,observaciones)
    if dao.crearEmpaque(empaque):
        response_object['mensaje']='empaque creado'
    else:
        response_object['tipo']='error'
        response_object['mensaje']='Error al crear empaque'
    return response_object

def consultarEmpaques(response_object):
    """
    Función que permite consultar todos los Empaques. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = EmpaqueDao()
    empaques=dao.consultarEmpaques()
    empaquesDict=list()
    for empaque in empaques:
        empaquesDict.append(empaque.__dict__)
    response_object['empaques']=empaquesDict
    return response_object

def actualizarEmpaque(data,response_object,empaque_ID):
    """
    Función que permite editar un empaque a partir de su ID. 
 
    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - empaque_ID: que es el ID del empaque

    Retorna el response_object modificado
    """
    dao = EmpaqueDao()
    categoria = dao.consultarCategoria(empaque_ID)
    if categoria is not None:
        Nombre=data.get('nombre')
        if Nombre is not None:
            categoria.nombre=Nombre
        Padre_categoria_ID=data.get('Padre_categoria_ID')
        if Padre_categoria_ID is not None:
            categoria.Padre_categoria_ID=Padre_categoria_ID
        if dao.actualizarcategoria(categoria):
            response_object['mensaje']="Categoría actualizada"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar cliente"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una categoría con ese ID"
    return response_object

def eliminarEmpaque(response_object, empaque_ID):
    """
    Función que permite eliminar los datos de un empaque a partir de su ID.
    Primero realiza la consulta del empaque para posteriormente eliminarlo.

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    - empaque_ID: que es el número de teléfono del cliente
    
    Retorna el response_object modificado
    """
    dao = EmpaqueDao()
    empaque = dao.consultarEmpaque(empaque_ID)
    if empaque is not None:
        if dao.eliminarEmpaque(categoria):
            response_object['mensaje']="Empaque eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar categoria"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un empaque con ese número telefónico"
    return response_object