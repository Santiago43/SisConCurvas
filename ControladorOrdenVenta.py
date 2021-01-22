from datetime import datetime

from dao.models import Usuario,OrdenVenta,Control_venta
from dao.OrdenVentaDao import OrdenDao
from dao.RolesDao import RolesDao
from dao.UsuariosDao import UsuariosDao
from dao.ControlDao import ControlDao
from dao.DireccionDao import DireccionDao
from dao.OrigenDao import OrigenDao
from dao.ModalidadPagoDao import ModalidadPagoDao
from dao.MetodoCompraDao import MetodoCompraDao

def crearOrden(data,response_object,editor):
    """
    Función que permite crear órdenes
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - editor: Usuario que realiza la acción

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
    precio=data.get('precio')
    ordenVenta=OrdenVenta(None,motivo_ID,origen_ID,modalidad_pago_ID,metodo_compra_ID,direccion_ID,cliente_ID,usuario_ID,estado,None,nota,fecha_entrega,tipo_venta,descuento,list(),precio)
    dao=OrdenDao()
    idorden = dao.crearOrden(ordenVenta)
    if idorden is not None:
        response_object['mensaje']="Orden creada"
        texto="El usuario "+editor.usuario+" creó la orden '"+idorden+"'"
        control=Control_venta(None,editor.usuario_ID,idorden,None,texto)
        controlDao=ControlDao()
        controlDao.crearControlRol(control)
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
    direccionDao=DireccionDao()
    modalidadPagoDao=ModalidadPagoDao()
    ordenesVenta=dao.consultarOrdenes()
    origenDao=OrigenDao()
    metodoCompraDao=MetodoCompraDao()
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
            productoEnOrdenDict['producto'].pop('stock')
            if ordenVenta.tipo_venta ==1:
                productoEnOrdenDict['producto'].pop('precioVenta')
            else:
                productoEnOrdenDict['producto'].pop('precioMayorista')
            productosDict.append(productoEnOrdenDict)
        ordenDict['productos']=productosDict
        objFechaEntrega=ordenDict['fecha_entrega']
        nuevaFechaEntrega=objFechaEntrega.strftime('%Y-%m-%d')
        ordenDict['fecha_entrega']=nuevaFechaEntrega
        objFechaVenta=ordenDict['fecha_venta']
        nuevaFechaVenta=objFechaVenta.strftime('%Y-%m-%d,%H:%M:%S')
        ordenDict['fecha_venta']=nuevaFechaVenta
        direccion_ID=ordenDict['direccion_ID']
        direccion=direccionDao.consultarDireccion(direccion_ID)
        ordenDict['direccion']=direccion.__dict__
        ciudad=direccionDao.consultarCiudad(direccion.ciudad_ID)
        departamento=direccionDao.consultarDepartamento(ciudad.departamento_ID)
        ordenDict['direccion']['ciudad']=ciudad.__dict__
        ordenDict['direccion']['departamento']=departamento.__dict__
        ordenDict['direccion'].pop('ciudad_ID')
        ordenDict.pop('direccion_ID')
        modalidad_pago_ID=ordenDict['modalidad_pago_ID']
        modalidadPago=modalidadPagoDao.consultarModalidad(modalidad_pago_ID)
        ordenDict['modalidadPago']=modalidadPago.__dict__
        origen=origenDao.consultarOrigen(ordenDict['origen_ID'])
        ordenDict['origen']=origen.__dict__
        ordenDict.pop('origen_ID')
        ordenDict['']
        ordenDict.pop('modalidad_pago_ID')
        metodo=metodoCompraDao.consultarMetodo(ordenDict['metodo_compra_ID'])
        ordenDict['metodoCompra']=metodo.__dict__
        ordenDict.pop('metodo_compra_ID')
        ordenesDict.append(ordenDict)
    response_object['ordenes']=ordenesDict
    return response_object

def actualizarOrden(data,response_object,ordenVenta_ID,editor):
    """
    Función que permite actualizar una orden a partir de su ID. 
 
    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - ordenVenta_ID: que es el ID de la orden
    - editor: Usuario que realiza la acción

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
            texto="El usuario "+editor.usuario+" modificó la orden '"+ordenVenta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar la orden de venta"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una orden de venta con ese ID"
    return response_object

def eliminarOrden(response_object, ordenVenta_ID,editor):
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
            texto="El usuario "+editor.usuario+" eliminó la orden '"+ordenVenta_ID+"'"
            control=Control_venta(None,editor.usuario_ID,ordenVenta_ID,None,texto)
            controlDao=ControlDao()
            controlDao.crearControlRol(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar la orden de venta"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una orden de venta con ese ID"
    return response_object