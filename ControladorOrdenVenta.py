from datetime import datetime

from dao.DireccionDao import DireccionDao
from dao.models import Usuario
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
        objFecha=ordenDict['fecha_entrega']
        nuevaFecha=objFecha.strftime('%m/%d/%Y')
        ordenDict['fecha_entrega']=nuevaFecha
        ordenesDict.append(ordenDict)
    response_object['ordenes']=ordenesDict
    print(ordenesDict)
    return response_object
