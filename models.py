class Persona:
    """
    Clase Persona
    Parámetros:
    - ID de persona
    - nombres y apellidos
    - número y tipo de documento
    - teléfono
    - correo
    """
    def __init__(self, persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo):
        self.persona_ID=persona_ID
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.tipoDocumento=tipoDocumento
        self.documento=documento
        self.telefono=telefono
        self.correo=correo
class Cliente(Persona):
    def __init__(self,cliente_ID,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo,tipoCliente):
        self.cliente_ID=cliente_ID
        self.tipoCliente=tipoCliente
        Persona.__init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo)

class PadreCategoria:
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre
class Categoria:
    def __init__(self,id,nombre,idPadre):
        self.id=id
        self.nombre=nombre
        self.idPadre=idPadre

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