from dao.models import Inventario
from dao.models import Categoria
from dao.InventarioDao import InventarioDao
def crearProducto(data,response_object):
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
    categorias=data.get('categorias')
    producto=Inventario(referenciaProducto,descripcion,urlImagen,stock,precioCosto,precioVenta,categorias)
    dao = InventarioDao()
    if(dao.consultarProducto(referenciaProducto) is None):
        if(dao.crearProducto(producto)):
            response_object['mensaje']="producto creado"
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

def actualizarProducto(data,response_object,referencia):
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
        descripcion = data.get("descripcion")
        if descripcion is not None:
            producto.descripcion=descripcion
        urlImagen = data.get("urlImagen")
        if urlImagen is not None:
            producto.urlImagen=urlImagen
        stock = data.get("stock")
        if stock is not None:
            producto.stock=stock
        precioCosto=data.get("precioCosto")
        if precioCosto is not None:
            producto.precioCosto=precioCosto
        precioVenta=data.get("precioVenta")
        if precioVenta is not None:
            producto.precioVenta=precioVenta
        if dao.actualizarProducto(producto):
            response_object['mensaje']="Producto actualizado"
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
