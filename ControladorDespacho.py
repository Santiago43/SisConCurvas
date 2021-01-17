from dao.DespachoDao import DespachoDao
from dao.OrdenVentaDao import OrdenDao
from dao.models import Despacho
def crearDespacho(data,response_object):
    """
    Función que permite crear despachos
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    ordenVenta_ID=data.get("ordenVenta_ID")
    usuario_ID=data.get('usuario_ID')
    motivo_ID=data.get('motivo_ID')
    ruta_ID=data.get('ruta_ID')
    estado="No despachado"
    id_envia=data.get('id_envia')
    despacho=Despacho(None,motivo_ID,usuario_ID,ordenVenta_ID,ruta_ID,estado,None,id_envia)
    dao=DespachoDao()
    ordenDao=OrdenDao()
    if ordenDao.consultarOrden(ordenVenta_ID) is not None:
        if dao.crearDespacho(despacho):
            response_object['mensaje']="Despacho creado"
        else:
            response_object['tipo']="Error"
            response_object['mensaje']="Error al crear el despacho"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="No existe esa orden de venta"
    return response_object

def consultarDespachos(response_object):
    """
    Función que permite consultar todos los despachos

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao=DespachoDao()
    despachos=dao.consultarDespachos()
    despachosDict=list()
    for despacho in despachos:
        despachoDict=despacho.__dict__
        despachosDict.append(despachoDict)
    response_object['despachos']=despachosDict
    return response_object


def actualizarDespacho(data,response_object,despacho_ID):
    """
    Función que permite consultar todos los despachos

    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - despacho_ID: que es el id del despacho a actualizar
    
    Retorna el response_object modificado
    """
    dao=DespachoDao()
    despachos=dao.consultarDespachos()
    despachosDict=list()
    for despacho in despachos:
        despachoDict=despacho.__dict__
        despachosDict.append(despachoDict)
    response_object['despachos']=despachosDict
    return response_object