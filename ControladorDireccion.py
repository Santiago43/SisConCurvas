from dao.models import Direccion
from dao.DireccionDao import DireccionDao

def consultarDireccion(response_object, direccionID):
    """
    Función que permite consultar la dirección por ID. 

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

def consultarDirecciones(response_object):
    """
    Función que permite consultar todas las direcciones

    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = DireccionDao()
    direcciones=dao.consultarDirecciones()
    direccionesJson=list()
    for direccion in direcciones:
        direccionDict=direccion.__dict__
        direccionesJson.append(direccionDict)
    response_object['direcciones']=direccionesJson
    return response_object

def consultarDepartamentos(response_object):
    """
    Función que permite consultar todas los departamentos

    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = DireccionDao()
    departamentos=dao.consultarDepartamentos()
    departamentosDict=list()
    for departamento in departamentos:
        departamentoDict=departamento.__dict__
        departamentosDict.append(departamentoDict)
    response_object['departamentos']=departamentosDict
    return response_object

def consultarCiudades(response_object):
    """
    Función que permite consultar todas las ciudades

    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = DireccionDao()
    ciudades=dao.consultarCiudades()
    ciudadesDict=list()
    for ciudad in ciudades:
        ciudadDict=ciudad.__dict__
        ciudadesDict.append(ciudadDict)
    response_object['ciudades']=ciudadesDict
    return response_object