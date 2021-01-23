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

def actualizarCliente(data,response_object,telefono):
    """
    Función que permite actualizar los datos de un cliente a partir de su número telefónico

    Parámetros:

    - data: que son los datos que vienen de la vista
    - response_object: que es una referencia a la respuesta del servidor
    - telefono: que es el número de teléfono del cliente

    Retorna el response_object modificado
    """
    dao=ClienteDao()
    cliente=dao.consultarCliente(telefono)
    if cliente is not None:
        primerNombre=data.get('primerNombre')
        if primerNombre is not None:
            cliente.primerNombre=primerNombre
        segundoNombre=data.get('segundoNombre')
        if segundoNombre is not None:
            cliente.segundonombre=segundoNombre
        primerApellido=data.get('primerApellido')
        if primerApellido is not None:
            cliente.primerApellido=primerApellido
        segundoApellido=data.get('segundoApellido')
        if segundoApellido is not None:
            cliente.segundoApellido=segundoApellido
        correo=data.get('correo')
        if correo is not None:
            cliente.correo=correo
        tipoCliente=data.get('tipoCliente')
        if tipoCliente is not None:
            cliente.tipoCliente=tipoCliente
        if dao.actualizarCliente(cliente):
            response_object['mensaje']="Cliente actualizado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al actualizar cliente"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un cliente con ese número telefónico"
    return response_object

def eliminarCliente(response_object,telefono):
    """
    Función que permite eliminar los datos de un cliente a partir de su número telefónico.
    Primero realiza la consulta del cliente para posteriormente eliminarlo.

    Parámetros:

    - response_object: que es una referencia a la respuesta del servidor
    - telefono: que es el número de teléfono del cliente
    
    Retorna el response_object modificado
    """
    dao=ClienteDao()
    cliente=dao.consultarCliente(telefono)
    if cliente is not None:
        if dao.eliminarCliente(cliente):
            response_object['mensaje']="Cliente eliminado"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Error al eliminar cliente"
    else:
        response_object['tipo']="error"
        response_object['mensaje']="No existe un cliente con ese número telefónico"
    return response_object
    
def consultarCliente(response_object,telefono):
    """
    Función que permite consultar todos los clientes. 

    Esta opera de tal forma que convierte los datos de la base de datos en objetos 
    y luego los convierte en diccionarios. 
    Parámetros:
    - response_object: que es una referencia a la respuesta del servidor
    Retorna el response_object modificado
    """
    dao = ClienteDao()
    clientes=dao.consultarCliente(telefono)
    clienteDict=cliente.__dict__
    direccionesDict= list()
    for direccion in cliente.direcciones:
        direccionesDict.append(direccion.__dict__)
    clienteDict['direcciones']=direccionesDict
    clientesJson.append(clienteDict)
    response_object['clientes']=clientesJson
    return response_object