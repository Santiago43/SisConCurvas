from dao.MotivoDao import MotivoDao
def consultarMotivos(response_object):
    """
    Función que permite consultar todos los motivos. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = MotivoDao()
    motivos=dao.consultarMotivos()
    motivosDict=list()
    for motivo in motivos:
        motivoDict=motivo.__dict__
        motivosDict.append(motivoDict)
    response_object['motivos']=motivosDict
    return response_object