from dao.models import Inventario,Categoria,Control_inventario
from dao.InventarioDao import InventarioDao
from dao.ControlDao import ControlDao
from dao.CategoriaDao import CategoriaDao
def crearProducto(data,response_object,usuario):
    """
    Función que permite crear productos
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    referenciaProducto=data.get('referenciaProducto')
    descripcion=data.get('descripcion')
    urlImagen=data.get('urlImagen')
    stock=data.get('stock')
    precioCosto=data.get('precioCosto')
    precioVenta=data.get('precioVenta')
    precioMayorista=data.get('precioMayorista')
    categorias=data.get('categorias')
    producto=Inventario(referenciaProducto,descripcion,urlImagen,stock,precioCosto,precioVenta,precioMayorista,categorias)
    dao = InventarioDao()
    if(dao.consultarProducto(referenciaProducto) is None):
        if(dao.crearProducto(producto)):
            response_object['mensaje']="producto creado"
            categoriaDao=CategoriaDao()
            for categoria in categorias:
                print(categoria)
                categoriaObj=categoriaDao.consultarCategoria(categoria['id'])
                dao.agregarCategoria(producto,categoriaObj)
            control=Control_inventario(usuario.usuario_ID,None,referenciaProducto,None,0,"Se crea: "+descripcion,stock,True)
            controlDao=ControlDao()
            controlDao.crearControlInventario(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear producto"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe un producto con esa referencia"
    return response_object

def consultarProductos(response_object):
    """
    Función que permite consultar todos los productos. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios.
    
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = InventarioDao()
    productos=dao.consultarProductos()
    productosDict=list()
    for producto in productos:
        productoDict=producto.__dict__
        categoriasDict=list()
        for categoria in producto.categorias:
            categoriasDict.append(categoria.__dict__)
        productoDict['categorias']=categoriasDict
        productosDict.append(productoDict)
    response_object['productos']=productosDict
    return response_object

def actualizarProducto(data,response_object,referencia,usuario):
    """
    Función que permite actualizar un producto mediante su referencia. 

    Parámetros:
    - data: data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao = InventarioDao()
    producto=dao.consultarProducto(referencia)
    if producto is not None:
        camposEditados=""
        descripcion = data.get("descripcion")
        if descripcion is not None:
            camposEditados+="Descripción, "
            producto.descripcion=descripcion
        urlImagen = data.get("urlImagen")
        if urlImagen is not None:
            camposEditados+="Imagen, "
            producto.urlImagen=urlImagen
        stock = data.get("stock")
        if stock is not None:
            camposEditados+="Stock, "
            producto.stock=stock
        precioCosto=data.get("precioCosto")
        if precioCosto is not None:
            camposEditados+="Precio costo, "
            producto.precioCosto=precioCosto
        precioVenta=data.get("precioVenta")
        if precioVenta is not None:
            camposEditados+="Precio venta"
            producto.precioVenta=precioVenta
        precioMayorista=data.get("precioMayorista")
        if precioMayorista is not None:
            camposEditados+="Precio venta"
            producto.precioMayorista=precioMayorista
        if dao.actualizarProducto(producto):
            response_object['mensaje']="Producto actualizado"
            control = Control_inventario(usuario.usuario_ID,None,producto.referenciaProducto,None,producto.stock,"El usuario "+usuario.usuario+ " editó los campos: "+camposEditados,0,False)
            controlDao=ControlDao()
            controlDao.crearControlInventario(control)
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar producto"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un producto con esa referencia"
    return response_object


def eliminarProducto(response_object,referencia):
    """
    Función que permite actualizar un producto mediante su referencia. 

    Parámetros:
    - data: data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao = InventarioDao()
    producto=dao.consultarProducto(referencia)
    if producto is not None:
        if dao.eliminarproducto(producto):
            response_object['mensaje']="Producto eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar producto"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un producto con esa referencia"
    return response_object


def agregarStock(data,response_object,referencia,usuario):
    """
    Función que permite actualizar un el stock de producto mediante su referencia. 

    Parámetros:
    - data: data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao = InventarioDao()
    producto=dao.consultarProducto(referencia)
    stock=data.get('stock')
    if producto is not None:
        if stock is not None:
            producto.stock+=stock
            if dao.actualizarProducto(producto):
                response_object['mensaje']="Producto actualizado"
                control = Control_inventario(usuario.usuario_ID,None,referencia,None,producto.stock-stock,"El usuario "+usuario.usuario+" agregó al inventario "+str(stock)+ " del producto '"+producto.referenciaProducto+"'",stock,True)
                controlDao=ControlDao()
                controlDao.crearControlInventario(control)
            else:
                response_object['tipo']="error"
                response_object['mensaje']="Error al actualizar producto"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Valor inválido de ingreso"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un producto con esa referencia"
    return response_object


def retirarStock(data,response_object,referencia,usuario):
    """
    Función que permite actualizar un el stock de producto mediante su referencia.

    Parámetros:
    
    - data: data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    
    Retorna el response_object modificado
    """
    dao = InventarioDao()
    producto=dao.consultarProducto(referencia)
    if producto is not None:
        stock = data.get("stock")
        if stock is not None:
            if stock >producto.stock:
                response_object['tipo']="error"
                response_object['mensaje']="No puede retirar más de la cantidad presente en el inventario. Actualmente hay "+str(producto.stock)+" unidad(es)"
            else:
                producto.stock-=stock
                if dao.actualizarProducto(producto):
                    response_object['mensaje']="Stock actualizado"
                    control=Control_inventario(usuario.usuario_ID,None,referencia,None,producto.stock+stock,"El usuario "+usuario.usuario+" retiró del inventario "+str(stock)+ " del producto '"+producto.referenciaProducto+"'",stock,False)
                    controlDao=ControlDao()
                    controlDao.crearControlInventario(control)
                else:
                    response_object['tipo']="error"
                    response_object['mensaje']="Error al actualizar producto"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Valor inválido de retiro"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un producto con esa referencia"
    return response_object