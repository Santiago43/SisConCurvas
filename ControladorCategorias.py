from dao.models import Categoria
from dao.CategoriaDao import CategoriaDao
def crearCategoria(data,response_object):
    """
    Función que permite crear categorias
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    nombre=data.get('nombre')
    idPadre=data.get('idPadre')
    categoria=Categoria(None,idPadre,nombre)
    dao = CategoriaDao()
    if(dao.consultarCategoriaPorNombre(nombre) is None):
        if(dao.crearCategoria(categoria)):
            response_object['mensaje']="categoría creada"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear categoría"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe una categoría con ese nombre"
    return response_object

def consultarCategorias(response_object):
    """
    Función que permite consultar todos los categorias. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = CategoriaDao()
    categorias=dao.consultarCategorias()
    categoriasDict=list()
    for categoria in categorias:
        categoriasDict.append(categoria.__dict__)
    response_object['categorias']=categoriasDict
    return response_object

def actualizarcategoria(response_object):
    """
    Función que permite consultar todos los categorias. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = CategoriaDao()

def eliminarcategoria(response_object, categoria_ID):
    """
    Función que permite consultar todos los categorias. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = CategoriaDao()
    categoria = dao.consultarCategoria(categoria_ID)
    if categoria is not None:
        if dao.eliminarcategoria(categoria):
            response_object['mensaje']="Categoria eliminada"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar categoria"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe una categoria con ese número telefónico"
    return response_object