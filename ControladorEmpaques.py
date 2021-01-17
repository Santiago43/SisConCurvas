from dao.DireccionDao import DireccionDao
from dao.OrdenVentaDao import OrdenDao
from dao.UsuariosDao import UsuariosDao
from dao.EmpaqueDao import EmpaqueDao
from dao.models import Empaque
def crearEmpaque(data,response_object):
    """
    Función que permite crear órdenes
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    ordenVenta_ID=data.get('ordenVenta_ID')
    motivo_ID=data.get('motivo_ID')
    usuario_ID=data.get('usuario_ID')
    numero_prendas=data.get('numero_prendas')
    estado=data.get('estado')
    observaciones=data.get('observaciones')
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
