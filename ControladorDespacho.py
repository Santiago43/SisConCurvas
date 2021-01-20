from dao.DespachoDao import DespachoDao
from dao.OrdenVentaDao import OrdenDao
from dao.models import Despacho, Control_venta
from dao.ControlDao import ControlDao

def crearDespacho(data,response_object,editor):
    """
    Función que permite crear despachos
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - editor: Usuario que realiza la acción

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
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" hizo el despacho de la orden '"+ordenVenta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
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


def actualizarDespacho(data,response_object,despacho_ID,editor):
    """
    Función que permite actualizar despachos

    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - despacho_ID: que es el id del despacho a actualizar
    
    Retorna el response_object modificado
    """
    dao = DespachoDao()
    despacho = dao.consultarDespacho(despacho_ID)
    if despacho is not None:
        ordenVenta_ID=data.get('ordenVenta_ID')
        if ordenVenta_ID is not None:
            despacho.ordenVenta_ID=ordenVenta_ID
        usuario_ID=data.get('usuario_ID')
        if usuario_ID is not None:
            despacho.usuario_ID=usuario_ID
        ruta_ID = data.get('ruta_ID')
        if ruta_ID is not None:
            despacho.ruta_ID = ruta_ID
        estado = data.get('estado')
        if estado is not None:
            despacho.estado = estado
        motivo_ID = data.get('motivo_ID')
        if motivo_ID is not None:
            despacho.motivo_ID = motivo_ID
        id_envia = data.get('id_envia')
        if id_envia is not None:
            despacho.id_envia = id_envia
        if dao.actualizarDespacho(despacho):
            response_object['mensaje']="despacho actualizado"
            texto="El usuario "+editor.primerNombre+" "+editor.primerApellido+" editó el despacho de la orden '"+despacho.ordenVenta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar despacho"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un despacho con ese ID"
    return response_object