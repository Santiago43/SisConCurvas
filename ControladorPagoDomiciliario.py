import time
from dao.PagoDomiciliarioDao import PagoDomiciliarioDao,PagoDomiciliario
from dao.UsuariosDao import UsuariosDao
from dao.RolesDao import RolesDao
def crearPago(data,response_object,usuario):
    """
    Función que permite crear pagos de domiciliario

    Parámetros:
    
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - usuario: que es el usuario que crea el pago

    Retorna el response_object modificado
    """
    domiciliario_ID=data.get('domiciliario_ID')
    estado=data.get('estado')
    monto=data.get('monto')
    dao=PagoDomiciliarioDao()
    pagoDomiciliario=PagoDomiciliario(None,estado,monto,None,domiciliario_ID,usuario.usuario_ID)
    usuarioDao=UsuariosDao()
    usuarioAPagar=usuarioDao.consultarUsuarioPorID(domiciliario_ID)
    if usuarioAPagar is not None:
        rolDao=RolesDao()
        rol=rolDao.consultarRol(usuarioAPagar.rol_ID)
        if(rol.nombre=="Domiciliario"):
            if(dao.crearPago(pagoDomiciliario)):
                response_object['mensaje']="pago creado"
            else:
                response_object['tipo']="error"
                response_object['mensaje']="Error al crear el pago del domiciliario"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Ese usuario no es un domiciliario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe ese usuario"
    return response_object
def consultarPagos(response_object):
    """
    Función que permite consultar todos los pagos de domiciliario

    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    dao=PagoDomiciliarioDao()
    pagos=dao.consultarPagos()
    pagosDict=list()
    for pago in pagos:
        pago.fecha=pago.fecha.strftime('%Y-%m-%d')
        pagosDict.append(pago.__dict__)

    response_object['pagos']=pagosDict
    return response_object

def actualizarPago(data,response_object,usuario,pago_domiciliario_ID):
    """
    Función que permite crear pagos de domiciliario

    Parámetros:
    
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - usuario: que es el usuario que actualiza el pago
    - pago_domiciliario_ID: que es el id del pago de domiciliario que se actualizará

    Retorna el response_object modificado
    """
    estado=data.get('estado')
    monto=data.get('monto')
    dao=PagoDomiciliarioDao()
    pagoDomiciliario=dao.consultarPago(pago_domiciliario_ID)
    if(pagoDomiciliario is not None):
        if estado is not None:
            pagoDomiciliario.estado=estado
        if monto is not None:
            pagoDomiciliario.monto=monto
        pagoDomiciliario.financiero_ID=usuario.usuario_ID
        if(dao.actualizarPago(pagoDomiciliario)):
            response_object['mensaje']="pago actualizado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar el pago del domiciliario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe ese pago"
    return response_object


def eliminarPago(response_object,pago_domiciliario_ID):
    """
    Función que permite crear pagos de domiciliario

    Parámetros:
    
    - response_object: que es una referencia a la respuesta del servidor
    - usuario: que es el usuario que actualiza el pago
    - pago_domiciliario_ID: que es el id del pago de domiciliario que se actualizará

    Retorna el response_object modificado
    """
    dao=PagoDomiciliarioDao()
    pagoDomiciliario=dao.consultarPago(pago_domiciliario_ID)
    if(pagoDomiciliario is not None):
        if(dao.eliminarPago(pagoDomiciliario)):
            response_object['mensaje']="pago eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar el pago del domiciliario"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe ese pago"
    return response_object