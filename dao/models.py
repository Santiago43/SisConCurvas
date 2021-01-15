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
    def __init__(self, persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,direcciones):
        self.persona_ID=persona_ID
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.telefono=telefono
        self.correo=correo
        self.direcciones=direcciones
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
    def __init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,direcciones,tipoCliente,cliente_ID):
        self.cliente_ID=cliente_ID
        self.tipoCliente=tipoCliente
        Persona.__init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,direcciones)
class Usuario(Persona):
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
    def __init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,direcciones, rol_ID, contraseña,usuario_ID,permisos,urlImagen,tipoDocumento,documento):
        self.usuario_ID=usuario_ID
        self.contraseña=contraseña
        self.rol_ID=rol_ID
        self.permisos=permisos
        self.urlImagen=urlImagen
        self.tipoDocumento=tipoDocumento
        self.documento=documento
        Persona.__init__(self,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,telefono,correo,direcciones)

class Direccion:
    """
    Clase direccion 
    Parámetros:
    - Id de la direccion 
    - Id de la ciudad 
    - id del departamento
    - barrio
    - direccion
    """
    def __init__(self,direccion_ID,ciudad_ID,departamento_ID,barrio,direccion):
        self.direccion_ID=direccion_ID
        self.ciudad_ID=ciudad_ID
        self.departamento_ID=departamento_ID
        self.barrio=barrio
        self.direccion=direccion
class Departamento:
    """
    Clase direccion 
    Parámetros:
    - Id del departamento 
    - nombre del departamento
    """
    def __init__(self,departamento_ID,departamento):
        self.departamento_ID=departamento_ID
        self.departamento=departamento
class Ciudad:
    """
    Clase ciudad 
    Parámetros:
    - Id de la ciudad 
    - nombre de la ciudad
    """
    def __init__(self,ciudad_ID,nombre):
        self.ciudad_ID=ciudad_ID
        self.nombre=nombre
class Categoria:
    """
    Clase Categoria 
    Parámetros:
    - Id de la categoria  
    - nombre de la categoria  
    """
    def __init__(self,id,idPadre,nombre):
        self.id=id
        self.nombre=nombre
        self.idPadre=idPadre
class Pago_Domiciliario:
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
        self.estado=estado
        self.monto=monto
        self.domiciliario_ID=domiciliario_ID
        self.financiero_ID=financiero_ID
class Empaque:
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
    def __init__(self,empaque_ID,ordenVenta_ID,motivo_ID,usuario_ID,numero_prendas,estado,observaciones):
        self.empaque_ID=empaque_ID
        self.ordenVenta_ID=ordenVenta_ID
        self.motivo_ID=motivo_ID
        self.usuario_ID=usuario_ID
        self.numero_prendas=numero_prendas
        self.estado=estado
        self.observaciones=observaciones
class Despacho:
    """
    Clase despacho 
    Parámetros:
    - Id del despacho 
    - Id del motivo
    - Id del usuario 
    - Id de la orden de venta 
    - Id de la ruta
    - estado
    - fecha de despacho
    """
    def __init__(self,despacho_ID,motivo_ID,usuario_ID,orden_venta_ID,ruta_ID,estado,fecha_despacho,id_envia):
        self.despacho_ID=despacho_ID
        self.motivo_ID=motivo_ID
        self.usuario_ID=usuario_ID
        self.orden_venta_ID=orden_venta_ID
        self.ruta_ID=ruta_ID
        self.estado=estado
        self.fecha_despacho=fecha_despacho
        self.id_envia=id_envia
class Distribucion:
    """
    Clase Distribucion 
    Parámetros:
    - Id de la Distribucion 
    - Id del motivo
    - Id del despacho
    - estado 
    - venta neta
    - costo de distribucion 
    - productos
    """
    def __init__(self,distribucion_ID, motivo_ID,usuario_ID,despacho_ID,estado,venta_neta,costo_distribucion,productos):
        self.distribucion_ID=distribucion_ID
        self.motivo_ID=motivo_ID
        self.usuario_ID=usuario_ID
        self.despacho_ID=despacho_ID
        self.estado=estado
        self.venta_neta=venta_neta
        self.costo_distribucion=costo_distribucion
        self.productos=productos
class Motivo:
    """
    Clase motivo
    Parámetros:
    - Id del motivo
    - tipo del motivo
    - motivo
    """
    def __init__(self,motivo_ID,tipo,motivo):
        self.motivo_ID=motivo_ID
        self.tipo=tipo
        self.motivo=motivo
class Ruta:
    """
    Clase Ruta
    Parámetros:
    - Id de la ruta
    - nombre
    """
    def __init__(self,ruta_ID,nombre):
        self.ruta_ID=ruta_ID
        self.nombre=nombre
class Metodo_compra:
    """
    Clase Metodo_compra
    Parámetros:
    - Id del metodo de compra
    - tipo
    """
    def __init__(self,metodo_compra_ID,tipo):
        self.metodo_compra_ID=metodo_compra_ID
        self.tipo=tipo
class Modalidad_pago:
    """
    Clase Modalidad_pago
    Parámetros:
    - Id de la modalidad de pago
    - madalidad
    """
    def __init__(self,modalidad_pago_ID,modalidad):
        self.modalidad_pago_ID=modalidad_pago_ID
        self.modalidad=modalidad
class Origen:
    """
    Clase Origen
    Parámetros:
    - Id del origen
    - nombre
    """
    def __init__(self,origen_ID,nombre):
        self.origen_ID=origen_ID
        self.nombre=nombre
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
class Contro_inventario:
    """
    Clase Contro_inventario
    Parámetros:
    - Id del Contro_inventario
    - referencia del producto
    - fecha
    - inventario inicial
    - numero de prendas
    - tipo 
    """   
    def __init__(self, control_inventario_ID,referenciaProducto,fecha,inventario_inicial,detalle,numero_prendas,tipo):
        self.control_inventario_ID=control_inventario_ID
        self.referenciaProducto=referenciaProducto
        self.fecha=fecha
        self.inventario_inicial=inventario_inicial
        self.detalle=detalle
        self.numero_prendas=numero_prendas
        self.tipo=tipo

class Rol:
    """
    Clase rol
    Parámetros:
    - Id del rol 
    - nombre del rol 
    """
    def __init__(self,idRol,nombre,permisos):
        self.idRol=idRol
        self.nombre=nombre
        self.permisos=permisos
class Control_rol:
    """
    Clase Control_rol:
    Parámetros:
    - Id de Control_rol:
    - Id del rol 
    - Id del usuario 
    - fecha de modificacion
    - tipo 
    - detalle
    """
    def __init__(self,control_rol_ID, rol_ID,usuario_ID,fecha_modificacion,tipo,detalle):
        self.control_rol_ID=control_rol_ID
        self.rol_ID=rol_ID
        self.usuario_ID=usuario_ID
        self.fecha_modificacion=fecha_modificacion
        self.tipo=tipo
        self.detalle=detalle

class Permiso:
    """
    Clase permiso
    Parámetros:
    - Id del permiso
    - nombre del permiso
    """
    def __init__(self,permiso_ID,nombre):
        self.permiso_ID=permiso_ID
        self.nombre=nombre

class OrdenVenta:
    """
    Clase Orden_venta
    Parámetros:
    - Id del motivo
    - Id del origen 
    - Id de la modalida de pago
    - Id del metodo de compra
    - Id de la direccion
    - Id del cliente 
    - Id del usuario 
    - estado 
    - fecha de venta 
    - precio 
    - nota 
    - fecha de entrega 
    - tipo de venta 
    - descuento 
    - productos 
    """
    def __init__(self,ordenVenta_ID,motivo_ID,origen_ID,modalidad_pago_ID,metodo_compra_ID,direccion_ID,cliente_ID,usuario_ID,estado,fecha_venta,nota,fecha_entrega,tipo_venta,descuento,productos,precio):
        self.ordenVenta_ID=ordenVenta_ID
        self.motivo_ID=motivo_ID
        self.origen_ID=origen_ID
        self.modalidad_pago_ID=modalidad_pago_ID
        self.metodo_compra_ID=metodo_compra_ID
        self.direccion_ID=direccion_ID
        self.cliente_ID=cliente_ID
        self.usuario_ID=usuario_ID
        self.estado=estado
        self.fecha_venta=fecha_venta
        self.nota=nota
        self.fecha_entrega=fecha_entrega
        self.tipo_venta=tipo_venta
        self.descuento=descuento
        self.productos=productos
        self.precio=precio
class Control_venta:
    """
    Clase Control_venta
    Parámetros:
    - Id del Control_venta
    - Id del usuario 
    - Id de la orden de venta 
    - fecha de la modificacion 
    - cambio 
    """
    def __init__(self,control_venta_ID,usuario_ID,orden_venta_ID,fecha_modificacion,cambio):
        self.control_venta_ID=control_venta_ID
        self.usuario_ID=usuario_ID
        self.orden_venta_ID=orden_venta_ID
        self.fecha_modificacion=fecha_modificacion
        self.cambio=cambio
class ProductoEnOrden:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad
