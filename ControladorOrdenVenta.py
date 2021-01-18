from datetime import datetime

from dao.DireccionDao import DireccionDao
from dao.models import Usuario,OrdenVenta
from dao.OrdenVentaDao import OrdenDao
from dao.RolesDao import RolesDao
from dao.UsuariosDao import UsuariosDao

def crearOrden(data,response_object):
    """
    Función que permite crear órdenes
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    motivo_ID=data.get('motivo_ID')
    origen_ID=data.get('origen_ID')
    modalidad_pago_ID=data.get('modalidad_pago_ID')
    metodo_compra_ID=data.get('metodo_compra_ID')
    direccion_ID=data.get('direccion_ID')
    cliente_ID=data.get('cliente_ID')
    usuario_ID=data.get('usuario_ID')
    estado=data.get('estado')
    nota=data.get('nota')
    fecha_entrega=data.get('fecha_entrega')
    tipo_venta=data.get('tipo_venta')
    descuento=data.get('descuento')
    ordenVenta=OrdenVenta(None,motivo_ID,origen_ID,modalidad_pago_ID,metodo_compra_ID,direccion_ID,cliente_ID,usuario_ID,estado,None,nota,fecha_entrega,tipo_venta,descuento,list(),None)
    dao=OrdenDao()
    if dao.crearOrden(ordenVenta):
        response_object['mensaje']="Orden creada"
    else:
        response_object['tipo']="Error"
        response_object['mensaje']="Error al crear la orden"
    return response_object

def consultarOrdenes(response_object):
    """
    Función que permite consultar todas las órdenes de venta. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = OrdenDao()
    ordenesVenta=dao.consultarOrdenes()
    ordenesDict=list()
    for ordenVenta in ordenesVenta:
        ordenDict=ordenVenta.__dict__
        productosEnOrden=ordenDict['productos']
        productosDict=list()
        for productoEnOrden in productosEnOrden:
            productoEnOrdenDict=productoEnOrden.__dict__
            producto=productoEnOrdenDict['producto']
            productoDict=producto.__dict__
            productoEnOrdenDict['producto']=productoDict
            categorias=productoEnOrdenDict['producto']['categorias']
            categoriasDict=list()
            for categoria in categorias:
                categoriaDict=categoria.__dict__
                categoriasDict.append(categoriaDict)
            productoEnOrdenDict['producto']['categorias']=categoriasDict
            productosDict.append(productoEnOrdenDict)
        ordenDict['productos']=productosDict
        objFechaEntrega=ordenDict['fecha_entrega']
        nuevaFechaEntrega=objFechaEntrega.strftime('%Y-%m-%d')
        ordenDict['fecha_entrega']=nuevaFechaEntrega
        objFechaVenta=ordenDict['fecha_venta']
        nuevaFechaVenta=objFechaVenta.strftime('%Y-%m-%d,%H:%M:%S')
        ordenDict['fecha_venta']=nuevaFechaVenta
        ordenesDict.append(ordenDict)
    response_object['ordenes']=ordenesDict
    return response_object

def actualizarOrden(data,response_object,ordenVenta_ID):
    """
    Función que permite actualizar una orden a partir de su ID. 
 
    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - ordenVenta_ID: que es el ID de la orden

    Retorna el response_object modificado
    """
    dao = OrdenDao()
    orden = dao.consultarOrden(ordenVenta_ID)
    if orden is not None:
        motivo_ID = data.get('motivo_ID')
        if motivo_ID is not None:
            orden.motivo_ID = motivo_ID
        origen_ID=data.get('origen_ID')
        if origen_ID is not None:
            orden.origen_ID=origen_ID
        modalidad_pago_ID = data.get('modalidad_pago_ID')
        if modalidad_pago_ID is not None:
            orden.modalidad_pago_ID = modalidad_pago_ID
        metodo_compra_ID = data.get('metodo_compra_ID')
        if metodo_compra_ID is not None:
            orden.metodo_compra_ID = metodo_compra_ID
        direccion_ID = data.get('direccion_ID')
        if direccion_ID is not None:
            orden.direccion_ID = direccion_ID
        cliente_ID = data.get('cliente_ID')
        if cliente_ID is not None:
            orden.cliente_ID = cliente_ID
        usuario_ID = data.get('usuario_ID')
        if usuario_ID is not None:
            orden.usuario_ID = usuario_ID
        estado = data.get('estado')
        if estado is not None:
            orden.estado = estado
        fecha_venta = data.get('fecha_venta')
        if fecha_venta is not None:
            orden.fecha_venta = fecha_venta
        nota = data.get('nota')
        if nota is not None:
            orden.nota = nota
        fecha_entrega = data.get('fecha_entrega')
        if fecha_entrega is not None:
            orden.fecha_entrega = fecha_entrega
        tipo_venta = data.get('tipo_venta')
        if tipo_venta is not None:
            orden.tipo_venta = tipo_venta
        descuento = data.get('descuento')
        if descuento is not None:
            orden.descuento = descuento
        productos = data.get('productos')
        if productos is not None:
            orden.productos = productos
        precio = data.get('precio')
        if precio is not None:
            orden.precio = precio
        if dao.actualizarOrden(orden):
            response_object['mensaje']="Orden de venta actualizada"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar la orden de venta"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una orden de venta con ese ID"
    return response_object

def eliminarOrden(response_object, ordenVenta_ID):
    """
    Función que permite eliminar los datos de un empaque a partir de su ID.
    Primero realiza la consulta del empaque para posteriormente eliminarlo.

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    - empaque_ID: que es el número de teléfono del cliente
    
    Retorna el response_object modificado
    """
    dao = OrdenDao()
    orden = dao.consultarOrden(ordenVenta_ID)
    if orden is not None:
        if dao.eliminarOrden(orden):
            response_object['mensaje']="Orden de venta eliminada"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar la orden de venta"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una orden de venta con ese ID"
    return response_object