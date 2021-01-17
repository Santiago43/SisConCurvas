from dao.OrigenDao import OrigenDao
def consultarOrigenes(response_object):
    """
    Función que permite consultar todos los Origenes. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = OrigenDao()
    origenes=dao.consultarOrigenes()
    origenesDict=list()
    for origen in origenes:
        origenDict=origen.__dict__
        origenesDict.append(origenDict)
    response_object['origenes']=origenesDict
    return response_object