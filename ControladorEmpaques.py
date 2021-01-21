from dao.DireccionDao import DireccionDao
from dao.OrdenVentaDao import OrdenDao
from dao.UsuariosDao import UsuariosDao
from dao.EmpaqueDao import EmpaqueDao
from dao.models import Empaque, Control_venta
from dao.ControlDao import ControlDao

def crearEmpaque(data,response_object,editor):
    """
    Función que permite crear un empaque
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - editor: Usuario que realiza la acción

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
        texto="El usuario "+editor.usuario+" hizo el empaque de la orden '"+ordenVenta_ID+"'"
        control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
        controlDao=ControlDao()
        controlDao.crearControlVenta(control)
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

def actualizarEmpaque(data,response_object,empaque_ID,editor):
    """
    Función que permite editar un empaque a partir de su ID. 
 
    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - empaque_ID: que es el ID del empaque

    Retorna el response_object modificado
    """
    dao = EmpaqueDao()
    empaque = dao.consultarEmpaque(empaque_ID)
    if empaque is not None:
        ordenVenta_ID=data.get('ordenVenta_ID')
        if ordenVenta_ID is not None:
            empaque.ordenVenta_ID=ordenVenta_ID
        usuario_ID=data.get('usuario_ID')
        if usuario_ID is not None:
            empaque.usuario_ID=usuario_ID
        numero_prendas = data.get('numero_prendas')
        if numero_prendas is not None:
            empaque.numero_prendas = numero_prendas
        estado = data.get('estado')
        if estado is not None:
            empaque.estado = estado
        observaciones = data.get('observaciones')
        if observaciones is not None:
            empaque.observaciones = observaciones
        motivo_ID = data.get('motivo_ID')
        if motivo_ID is not None:
            empaque.motivo_ID = motivo_ID
        if dao.actualizarEmpaque(empaque):
            response_object['mensaje']="Empaque actualizado"
            texto="El usuario "+editor.usuario+" hizo el actualizó el empaque de la orden '"+ordenVenta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar Empaque"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un empaque con ese ID"
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
        if dao.eliminarEmpaque(empaque):
            response_object['mensaje']="Empaque eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar empaque"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un empaque con ese número telefónico"
    return response_object