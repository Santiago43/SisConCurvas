from dao.models import Direccion
from dao.DireccionDao import DireccionDao

def consultarDireccion(response_object, direccionID):
    """
    Función que permite consultar las direcciones. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = DireccionDao()
    direccion=dao.consultarDireccion(direccionID)
    response_object['direccion']=direccion.__dict__
    return response_object