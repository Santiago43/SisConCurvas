from dao.MetodoCompraDao import MetodoCompraDao,Metodo_compra
def consultarMetodosDeCompra(response_object):
    """
    Función que permite consultar todos los métodos de compra. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = MetodoCompraDao()
    metodos=dao.consultarMetodos()
    metodosDict=list()
    for metodo in metodos:
        metodoDict=metodo.__dict__
        metodosDict.append(metodoDict)
    response_object['metodos']=metodosDict
    return response_object