import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import utils

from ControladorOrdenVenta import consultarOrdenes, crearOrden, actualizarOrden, eliminarOrden
from ControladorRol import consultarRoles, crearRol,actualizarRol, eliminarRol, agregarPermisoARol, removerPermisoARol
from ControladorClientes import crearCliente, consultarClientes, actualizarCliente, eliminarCliente,consultarCliente
from ControladorUsuarios import consultarUsuarios, crearUsuario, actualizarUsuario,eliminarUsuario,login,agregarPermisoAUsuario,removerPermisoAUsuario,validarUsuario, validarUsuarioLogueadoPorToken, validarUsuarioPorToken
from ControladorInventario import crearProducto, consultarProductos, actualizarProducto, eliminarProducto,agregarStock,retirarStock
from ControladorOrigen import consultarOrigenes
from ControladorDespacho import crearDespacho, consultarDespachos
from ControladorCategorias import crearCategoria, consultarCategorias, actualizarcategoria, eliminarcategoria
from ControladorEmpaques import crearEmpaque, consultarEmpaques, actualizarEmpaque, eliminarEmpaque
from ControladorPagoDomiciliario import crearPago, consultarPagos, actualizarPago, eliminarPago
from ControladorDistribucion import crearDistribucion,consultarDistribuciones,actualizarDistribucion, eliminarDistribucion
from ControladorDireccion import consultarDireccion, consultarDirecciones
from ControladorMetodoCompra import consultarMetodosDeCompra
from ControladorMotivo import consultarMotivos
from ControladorModalidadPago import consultarModalidadesDePago
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def noAutorizado(response_object):
    response_object['tipo']="error"
    response_object['mensaje']="no autorizado"
    return response_object

@app.route("/")
def main_():
    """
    Función ping
    """
    headers=request.headers
    print(headers.get("Prueba"))
    return "<h1>Concurvas</h1>"

@app.route("/rol", methods=['POST','GET'])
def rol():
    """
    Ruta de roles para crear y consultar
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Rol.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearRol(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object) 
    elif request.method=="GET":
        (valor,editor)=validarUsuario("Rol.ver",token)
        if valor:    
            response_object=consultarRoles(response_object)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/rol/<rol_ID>", methods=['PUT','DELETE'])
def single_rol(rol_ID):
    """
    ruta de roles para actualizar y eliminar
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor)=validarUsuario("Rol.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarRol(data,response_object,rol_ID,editor) 
        else:
            response_object=noAutorizado(response_object)
    elif request.method=="DELETE":
        (valor,editor)=validarUsuario("Rol.eliminar",token)
        if valor:
            response_object=eliminarRol(response_object,rol_ID,editor)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/rol/permiso/<rol_ID>/<permiso_ID>",methods=['POST','DELETE'])
def permisosRol(rol_ID,permiso_ID):
    """
    Manejo de permisos de roles
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=='POST':
        (valor,editor) = validarUsuario("PermisoRol.modificar",token)
        if valor:
            response_object=agregarPermisoARol(response_object,rol_ID,permiso_ID, editor)
        else:
            response_object = noAutorizado(response_object)
    elif request.method=='GET':
        response_object['ans']="Funciona :D"
    elif request.method=='DELETE':
        (valor,editor) = validarUsuario("PermisoRol.modificar",token)
        if valor:
            response_object=removerPermisoARol(response_object,rol_ID,permiso_ID, editor)
        else:
            response_object = noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/usuario", methods=['POST','GET'])
def usuarios():
    """
    Ruta de usuarios para crear y listar todos
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor) = validarUsuario("Usuarios.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearUsuario(data,response_object) 
        else:
            response_object = noAutorizado(response_object)
    elif request.method=="GET":
        (valor,editor) = validarUsuario("Usuarios.ver",token)
        if valor:
            response_object=consultarUsuarios(response_object)  
        else:
            response_object = noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/usuario/<documento>", methods=['PUT','DELETE'])
def single_usuario(documento):
    """
    Ruta de usuarios para actualizar y eliminar
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor) = validarUsuario("Usuarios.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarUsuario(data,response_object,documento)
        else:
            response_object = noAutorizado(response_object)
    elif request.method=="DELETE":
        (valor,editor) = validarUsuario("Usuarios.eliminar",token)
        if valor:
            response_object=eliminarUsuario(response_object,documento)  
        else:
            response_object = noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/usuario/permiso/<documento>/<permiso_ID>", methods=['POST','DELETE'])
def usuarioPermisos(documento,permiso_ID):
    """
    Ruta de manejo de permisos de usuarios
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor) = validarUsuario("Usuarios.editar",token)
        if valor:
            response_object=agregarPermisoAUsuario(response_object,documento,permiso_ID)
        else:
            response_object = noAutorizado(response_object)
    elif request.method=="DELETE":
        (valor,editor) = validarUsuario("Usuarios.editar",token)
        if valor:
            response_object=removerPermisoAUsuario(response_object,documento,permiso_ID)  
        else:
            response_object = noAutorizado(response_object)  
    return jsonify(response_object)

@app.route("/validar", methods=['POST'])
def validarUsuarioLogueado():
    """
    Ruta de login
    """
    response_object = {'tipo': 'OK'}
    headers=request.headers
    token=headers.get('token')
    valor=validarUsuarioLogueadoPorToken(token)
    response_object['value']=valor
    response_object['usuario']=validarUsuarioPorToken(token)
    return jsonify(response_object)
@app.route("/orden",methods=['POST','GET'])
def ordenVenta():
    """
    Controlador de órdenes de venta
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Orden.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearOrden(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object)               
    elif request.method=="GET":
        (valor,editor)=validarUsuario("Orden.ver",token)
        if valor:
            response_object=consultarOrdenes(response_object)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/orden/<ordenVenta_ID>",methods=['PUT','DELETE'])
def single_orden(ordenVenta_ID):
    """
    Ruta de Ordenes de venta para actualizar y eliminar
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor) = validarUsuario("Orden.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarOrden(data,response_object,ordenVenta_ID,editor)
        else:
            response_object=noAutorizado(response_object)
    elif request.method=="DELETE":
        (valor,editor) = validarUsuario("Orden.eliminar",token)
        if valor:
            response_object=eliminarOrden(response_object,ordenVenta_ID,editor)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/login", methods=['POST'])
def loginUsuario():
    """
    Ruta de login
    """
    response_object = {'tipo': 'OK'}
    data=request.get_json()
    response_object=login(data,response_object)  
    return jsonify(response_object)

@app.route("/cliente",methods=['POST','GET'])
def cliente():
    """
    Ruta de clientes para crear y consultar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCliente(data,response_object)
    else:
        response_object=consultarClientes(response_object)
    return jsonify(response_object)

@app.route("/cliente/<telefono>",methods=['GET','PUT','DELETE'])
def single_cliente(telefono):
    """
    Ruta de clientes para actualizar y eliminar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarCliente(data,response_object,telefono)
    elif request.method=="GET":
        data=request.get_json()
        response_object=consultarCliente(response_object,telefono)
    elif request.method=="DELETE":
        response_object=eliminarCliente(response_object,telefono)
    return jsonify(response_object)

@app.route("/producto",methods=['POST','GET'])
def producto():
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Inventario.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearProducto(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object)
    else:
        (valor,editor)=validarUsuario("Inventario.ver",token)
        if valor:
            response_object=consultarProductos(response_object)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/producto/<referencia>",methods=['PUT','DELETE'])
def single_producto(referencia):
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor)=validarUsuario("Inventario.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarProducto(data,response_object,referencia,editor)
        else:
            response_object=noAutorizado(response_object)
    elif request.method=="DELETE":
        (valor,editor)=validarUsuario("Inventario.eliminar",token)
        if valor:
            response_object=eliminarProducto(response_object,referencia)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/producto/stock/<referencia>",methods=['PUT'])
def modifyStock(referencia):
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    (valor,editor)=validarUsuario("Inventario.editar",token)
    if valor:
        data=request.get_json()
        estado=data.get('estado')
        if estado:
            response_object=agregarStock(data,response_object,referencia,editor)
        else:
            response_object=retirarStock(data,response_object,referencia,editor)
    else:
        response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/categoria",methods=['POST','GET'])
def categoria():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCategoria(data,response_object)  
    else:
        response_object=consultarCategorias(response_object)
    return jsonify(response_object)

@app.route("/categoria/<categoria_ID>",methods=['PUT','DELETE'])
def single_categoria(categoria_ID):
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarcategoria(data,response_object,categoria_ID)
    elif request.method=="DELETE":
        response_object=eliminarcategoria(response_object,categoria_ID)
    return jsonify(response_object)

@app.route("/empaque",methods=['POST','GET'])
def empaque():
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Orden.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearEmpaque(data,response_object, editor)  
        else:
            response_object=noAutorizado(response_object)               
    else:
        response_object=consultarEmpaques(response_object)
    return jsonify(response_object)

@app.route("/origen",methods=['GET'])
def origen():
    """
    Ruta de orígenes de venta
    """
    response_object = {'tipo': 'OK'}
    response_object=consultarOrigenes(response_object)
    return jsonify(response_object)

@app.route("/despacho",methods=['POST','GET'])
def despacho():
    """
    Ruta de despachos
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Despacho.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearDespacho(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object)
    else:
        response_object=consultarDespachos(response_object)
    return jsonify(response_object)

@app.route("/despacho/<despacho_ID>",methods=['PUT','DELETE'])
def single_despacho(despacho_ID):
    """
    Ruta de despachos
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor)=validarUsuario("Despacho.editar",token)
        if valor:
            data=request.get_json()
            response_object=crearDespacho(data,response_object,editor)  
    else:
        response_object=consultarDespachos(response_object)

@app.route("/empaque/<empaque_ID>",methods=['PUT','DELETE'])
def single_empaque(empaque_ID):
    """
    Ruta de empaque para actualizar y eliminar
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor) = validarUsuario("Orden.editar",token)
        if valor:
            data=request.get_json()
        response_object=actualizarEmpaque(data,response_object,empaque_ID,editor)
    elif request.method=="DELETE":
        response_object=eliminarEmpaque(response_object,empaque_ID)
    return jsonify(response_object)


@app.route("/pagoDomiciliario",methods=['POST','GET'])
def pagoDomiciliario():
    """
    Ruta de pagos de domiciliario
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Pagodomiciliario.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearPago(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object)
    else:
        (valor,editor)=validarUsuario("Pagodomiciliario.ver",token)
        if valor is True:
            response_object=consultarPagos(response_object)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/pagoDomiciliario/<pago_domiciliario_ID>",methods=['PUT','DELETE'])
def single_pagoDomiciliario(pago_domiciliario_ID):
    """
    Ruta de pagos de domiciliario
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor)=validarUsuario("Pagodomiciliario.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarPago(data,response_object,editor,pago_domiciliario_ID)
        else:
            response_object=noAutorizado(response_object)  
    else:
        (valor,editor)=validarUsuario("Pagodomiciliario.eliminar",token)
        if valor:
            response_object=eliminarPago(response_object,pago_domiciliario_ID)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/distribucion",methods=['POST','GET'])
def distribucion():
    """
    Ruta de distribución
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        (valor,editor)=validarUsuario("Distribucion.crear",token)
        if valor:
            data=request.get_json()
            response_object=crearDistribucion(data,response_object,editor)
        else:
            response_object=noAutorizado(response_object)  
    else:
        (valor,editor)=validarUsuario("Distribucion.ver",token)
        if valor:
            response_object=consultarDistribuciones(response_object)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/distribucion/<distribucion_ID>",methods=['PUT','DELETE'])
def single_distribucion(distribucion_ID):
    """
    Ruta de distribución
    """
    headers=request.headers
    token=headers.get('token')
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        (valor,editor)=validarUsuario("Distribucion.editar",token)
        if valor:
            data=request.get_json()
            response_object=actualizarDistribucion(data,response_object,distribucion_ID,editor)
        else:
            response_object=noAutorizado(response_object)  
    else:
        (valor,editor)=validarUsuario("Distribucion.eliminar",token)
        if valor:
            response_object=eliminarDistribucion(response_object,distribucion_ID,editor)
        else:
            response_object=noAutorizado(response_object)
    return jsonify(response_object)

@app.route("/direccion",methods=['GET'])
def direccion():
    """
    Ruta de dirección
    """
    response_object = {'tipo': 'OK'}
    if request.method=='GET':
        response_object=consultarDirecciones(response_object)
    return jsonify(response_object)

@app.route("/direccion/<direccionID>",methods=['GET'])
def single_direccion(direccionID):
    """
    Ruta de direccion por ID
    """
    response_object = {'tipo': 'OK'}
    response_object=consultarDireccion(response_object,direccionID)
    return jsonify(response_object)

@app.route("/metodoCompra",methods=['GET'])
def metodosCompra():
    """
    Ruta para consultar los métodos de compra
    """
    response_object = {'tipo': 'OK'}
    response_object=consultarMetodosDeCompra(response_object)
    return jsonify(response_object)


@app.route("/motivo",methods=['GET'])
def motivos():
    """
    Ruta para consultar los motivos (de venta, no empaque, no despacho, no distribución, etc).
    """
    response_object = {'tipo': 'OK'}
    response_object=consultarMotivos(response_object)
    return jsonify(response_object)


@app.route("/modalidadPago",methods=['GET'])
def modalidades():
    """
    Ruta para consultar las modalidades de pago
    """
    response_object = {'tipo': 'OK'}
    response_object=consultarModalidadesDePago(response_object)
    return jsonify(response_object)


@app.route("/imgProducto",methods=['POST','GET'])
def imgProducto():
    """
    Ruta para subir imágenes de productos
    """
    headers=request.headers
    fileName=headers.get('fileName')
    target = os.path.join(APP_ROOT, "../homeConcurvas/img/producto/")
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files)
    if 'file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})
    file = request.files['file']
    destination = '/'.join([target, fileName])
    file.save(destination)
    success = "Success!"
    return jsonify({'file': success})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
