class Persona:
    """
    Clase Persona
    Parámetros:
    - ID de persona
    - nombres y apellidos
    - número y tipo de documento
    - teléfono
    - correo
    - Direccion
    """
    def __init__(self, persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo,direccion):
        self.persona_ID=persona_ID
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.tipoDocumento=tipoDocumento
        self.documento=documento
        self.telefono=telefono
        self.correo=correo
        self.direccion
class Cliente(Persona):
    """
    Clase Cliente 
    Parámetros:
    - Id del cliente 
    - Id de persona
    - Nombres y apelllidos
    - número y tipo de documento
    - teléfono
    - correo
    - Direccion
    """
    def __init__(self,cliente_ID,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo,tipoCliente):
        self.cliente_ID=cliente_ID
        self.tipoCliente=tipoCliente
        Persona.__init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo)
class Usuario(persona):
    """
    Clase Usuario 
    Parámetros:
    - Id del usuario 
    - Id de persona
    - Nombres y apelllidos
    - número y tipo de documento
    - teléfono
    - correo
    - Direccion
    - contraseña
    - Id del rol
    """
    def __init__(self,usuario_ID,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo, contraseña, rol_ID):
        self.usuario_ID=usuario_ID
        self.contraseña=contraseña
        self.rol_ID=rol_ID
        Persona.__init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo)
class Direccion():
    """
    Clase direccion 
    Parámetros:
    - Id de la direccion 
    - Id de la ciudad 
    - id del departamento
    - barrio
    """
    def __init__(self,direccion_ID,ciudad_ID,departamento_ID,barrio):
        self.direccion_ID=direccion_ID
        self.ciudad_ID=ciudad_ID
        self.departamento_ID=departamento_ID
        self.barrio=barrio
class Departamento():
    """
    Clase direccion 
    Parámetros:
    - Id del departamento 
    - nombre del departamento
    """
    def __init__(self,departamento_ID,departamento):
        self.departamento_ID=departamento_ID
        self.departamento=departamento
class Ciudad():
    """
    Clase ciudad 
    Parámetros:
    - Id de la ciudad 
    - nombre de la ciudad
    """
    def __init__(self,ciudad_ID,nombre):
        self.ciudad_ID=ciudad_ID
        self.nombre=nombre
class PadreCategoria:
    """
    Clase PadreCategoria 
    Parámetros:
    - Id de la categoria padre 
    - nombre de la categoria padre 
    """
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre
class Categoria:
    """
    Clase Categoria 
    Parámetros:
    - Id de la categoria  
    - nombre de la categoria  
    """
    def __init__(self,id,nombre,idPadre):
        self.id=id
        self.nombre=nombre
        self.idPadre=idPadre
class Pago_Domiciliario():
    """
    Clase Pago domiciliario 
    Parámetros:
    - Id del pago  
    - estado 
    - monto a pagar
    - Id del domiciliario 
    - Id del financiero
    """
    def __init__(self,Pago_domiciliario_ID,estado,monto,domiciliario_ID,financiero_ID):
        self.Pago_domiciliario_ID=Pago_domiciliario_ID
        self.estado
        self.monto
        self.domiciliario_ID=domiciliario_ID
        self.financiero_ID=financiero_ID
class Empaque():
    """
    Clase Empaque 
    Parámetros:
    - Id del empaque 
    - Id de la orden de venta 
    - Id del motivo
    - Id del usuario 
    - numero de prendas llevadas 
    - estado
    - observaciones
    """
    def __init__(self,empaque_ID,orden_venta_ID,motivo_ID,usuario_ID,numero_prendas,estado,observaciones):
        self.empaque_ID=empaque_ID
        self.orden_venta_ID=orden_venta_ID
        self.motivo_ID=motivo_ID
        self.usuario_ID=usuario_ID
        self.numero_prendas=numero_prendas
        self.estado=estado
        self.observaciones=observaciones
class Inventario:
    """
    Clase inventario
    Parámetros:
    - Referencia del producto
    - Descripción del producto
    - Url de la imagen
    - Stock
    - Costo de venta
    - Precio de venta
    - Lista con las categorías
    """
    def __init__(self, referenciaProducto,descripcion,urlImagen,stock,precioCosto,precioVenta,categorias):
        self.referenciaProducto=referenciaProducto
        self.descripcion=descripcion
        self.urlImagen=urlImagen
        self.stock=stock
        self.precioCosto=precioCosto
        self.precioVenta=precioVenta
        self.categorias=categorias


class Rol:
    def __init__(self,idRol,nombre):
        self.idRol=idRol
        self.nombre=nombre