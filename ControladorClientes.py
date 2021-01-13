from dao.models import Cliente
from dao.ClienteDao import ClienteDao
from dao.DireccionDao import DireccionDao
def crearCliente(data,response_object):
    """
    Función que permite crear clientes
    Parámetros
    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor

    Retorna el response_object modificado
    """
    primerNombre=data.get('primerNombre')
    segundoNombre=data.get('segundoNombre')
    primerApellido=data.get('primerApellido')
    segundoApellido=data.get('segundoApellido')
    telefono=data.get('telefono')
    correo=data.get('correo')
    direcciones=data.get('direcciones')
    tipoCliente=data.get('tipoCliente')
    cliente=Cliente(None,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,None,tipoCliente,None)
    dao = ClienteDao()
    direccionDao=DireccionDao()
    if(dao.consultarCliente(telefono) is None):
        if(dao.crearcliente(cliente)):
            for direccionDict in direcciones:
                direccionDao.consultarDireccion(direccionDict['idDireccion'])
            response_object['mensaje']="cliente creado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al crear cliente"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="Ya existe un cliente con ese documento o con ese correo"
    return response_object

def consultarClientes(response_object):
    """
    Función que permite consultar todos los clientes. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = ClienteDao()
    clientes=dao.consultarClientes()
    clientesJson=list()
    for cliente in clientes:
        clienteDict=cliente.__dict__
        direccionesDict= list()
        for direccion in cliente.direcciones:
            direccionesDict.append(direccion.__dict__)
        clienteDict['direcciones']=direccionesDict
        clientesJson.append(clienteDict)
    response_object['clientes']=clientesJson
    return response_object
