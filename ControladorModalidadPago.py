from dao.ModalidadPagoDao import Modalidad_pago,ModalidadPagoDao
def consultarModalidadesDePago(response_object):
    """
    Función que permite consultar todas las modalidades de pago. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = ModalidadPagoDao()
    modalidades=dao.consultarModalidades()
    modalidadesDict=list()
    for modalidad in modalidades:
        modalidadDict=modalidad.__dict__
        modalidadesDict.append(modalidadDict)
    response_object['modalidades']=modalidadesDict
    return response_object