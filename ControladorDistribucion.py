from dao.DespachoDao import DespachoDao
from dao.DistribucionDao import DistribucionDao
from dao.models import Despacho,Distribucion,Control_venta
from dao.ControlDao import ControlDao

def crearDistribucion(data,response_object,editor):
    """
    Función que permite crear distribuciones
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - editor: Usuario que realiza la acción

    Retorna el response_object modificado
    """
    motivo_ID=data.get('motivo_ID')
    despacho_ID=data.get('despacho_ID')
    estado=data.get('estado')
    costoDistribucion=data.get('costoDistribucion')
    ventaNeta=data.get('ventaNeta')
    productos=data.get('productos')
    distribucion=Distribucion(None,editor.usuario_ID,despacho_ID,estado,motivo_ID,ventaNeta,costoDistribucion,list())
    dao=DistribucionDao()
    despachoDao=DespachoDao()
    despacho=despachoDao.consultarDespacho(despacho_ID)
    if  despacho is not None:
        if dao.crearDistribucion(distribucion):
            response_object['mensaje']="Distribución creada"
            texto="El usuario "+editor.usuario+" hizo el registro de la distribución del despacho '"+str(despacho_ID)+"'"
            control=Control_venta(None,editor.usuario_ID,despacho.orden_venta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
        else:
            response_object['tipo']="Error"
            response_object['mensaje']="Error al crear la distribución"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="No existe ese despacho"
    return response_object

def consultarDistribuciones(response_object):
    """
    Función que permite consultar todas las distribuciones

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao=DistribucionDao()
    distribuciones=dao.consultarDistribuciones()
    distribucionesDict=list()
    for distribucion in distribuciones:
        distribucionDict=distribucion.__dict__
        productosEnOrdenDict=list()
        for productoEnOrden in distribucion.productos:
            categoriasDict=list()
            for categoria in productoEnOrden.producto.categorias:
                categoriasDict.append(categoria.__dict__)
            productoEnOrdenDict=productoEnOrden.__dict__
            productoEnOrdenDict['producto']=productoEnOrdenDict['producto'].__dict__
            productoEnOrdenDict['producto'].pop('stock')
            productoEnOrdenDict['producto']['categorias']=categoriasDict
            productosEnOrdenDict.append(productoEnOrdenDict)
        distribucionDict['productos']=productosEnOrdenDict
        distribucionesDict.append(distribucionDict)
    response_object['distribuciones']=distribucionesDict
    return response_object


def actualizarDistribucion(data,response_object,distribucion_ID,editor):
    """
    Función que permite actualizar distribuciones 

    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - distribucion_ID: que es el id de la distribución a actualizar
    
    Retorna el response_object modificado
    """
    dao = DistribucionDao()
    distribucion = dao.consultarDistribucion(distribucion_ID)
    if distribucion is not None:
        motivo_ID = data.get('motivo_ID')
        if motivo_ID is not None:
            distribucion.motivo_ID = motivo_ID
        usuario_ID=data.get('usuario_ID')
        if usuario_ID is not None:
            distribucion.usuario_ID=usuario_ID
        estado = data.get('estado')
        if estado is not None:
            distribucion.estado = estado
        ventaNeta= data.get('ventaNeta')
        if ventaNeta is not None:
            distribucion.ventaNeta = ventaNeta
        costoDistribucion=data.get('costoDistribucion')
        if costoDistribucion is not None:
            distribucion.costoDistribucion=costoDistribucion
        despachoDao=DespachoDao()
        despacho=despachoDao.consultarDespacho(distribucion.despacho_ID)
        print(distribucion.__dict__)
        if dao.actualizarDistribucion(distribucion):
            response_object['mensaje']="distribución actualizada"
            texto="El usuario "+editor.usuario+" editó la distribución de la orden '"+str(despacho.orden_venta_ID)+"'"
            control=Control_venta(None,editor.usuario_ID,despacho.orden_venta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar distribución"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una distribución con ese ID"
    return response_object


def eliminarDistribucion(response_object,distribucion_ID,editor):
    """
    Función que permite actualizar distribuciones 

    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - distribucion_ID: que es el id de la distribución a actualizar
    
    Retorna el response_object modificado
    """
    dao = DistribucionDao()
    distribucion = dao.consultarDistribucion(distribucion_ID)
    despachoDao=DespachoDao()
    despacho=despachoDao.consultarDespacho(distribucion.despacho_ID)
    if distribucion is not None:
        if dao.eliminarDistribucion(distribucion):
            response_object['mensaje']="distribución eliminada"
            texto="El usuario "+editor.usuario+" eliminó la distribución de la orden '"+despacho.orden_venta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,despacho.orden_venta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlVenta(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar distribución"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una distribución con ese ID"
    return response_object