from flask import Flask, jsonify, request
from flask_cors import CORS

from ControladorOrdenVenta import consultarOrdenes, crearOrden
from ControladorRol import consultarRoles, crearRol,actualizarRol, eliminarRol, agregarPermisoARol, removerPermisoARol
from ControladorUsuarios import consultarUsuarios, crearUsuario, actualizarUsuario,eliminarUsuario,login,agregarPermisoAUsuario,removerPermisoAUsuario,validarUsuario
from ControladorClientes import crearCliente, consultarClientes, actualizarCliente, eliminarCliente
from ControladorInventario import crearProducto, consultarProductos, actualizarProducto, eliminarProducto
from ControladorCategorias import crearCategoria, consultarCategorias
from ControladorOrigen import consultarOrigenes
from ControladorDespacho import crearDespacho, consultarDespachos
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

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
    return "Funciona :D"

@app.route("/rol", methods=['POST','GET'])
def rol():
    """
    Ruta de roles para crear y consultar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearRol(data,response_object)  
    elif request.method=="GET":
        response_object=consultarRoles(response_object)  
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
    response_object = {'tipo': 'OK'}
    if request.method=='POST':
        response_object=agregarPermisoARol(response_object,rol_ID,permiso_ID)
    elif request.method=='GET':
        response_object['ans']="Funciona :D"
    elif request.method=='DELETE':
        response_object=removerPermisoARol(response_object,rol_ID,permiso_ID)
    return jsonify(response_object)

@app.route("/usuario", methods=['POST','GET'])
def usuarios():
    """
    Ruta de usuarios para crear y listar todos
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearUsuario(data,response_object)  
    elif request.method=="GET":
        response_object=consultarUsuarios(response_object)  
    return jsonify(response_object)

@app.route("/usuario/<documento>", methods=['PUT','DELETE'])
def single_usuario(documento):
    """
    Ruta de usuarios para actualizar y eliminar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarUsuario(data,response_object,documento)  
    elif request.method=="DELETE":
        response_object=eliminarUsuario(response_object,documento)  
    return jsonify(response_object)

@app.route("/usuario/permiso/<documento>/<permiso_ID>", methods=['POST','DELETE'])
def usuarioPermisos(documento,permiso_ID):
    """
    Ruta de manejo de permisos de usuarios
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        response_object=agregarPermisoAUsuario(response_object,documento,permiso_ID)  
    elif request.method=="DELETE":
        response_object=removerPermisoAUsuario(response_object,documento,permiso_ID)  
    return jsonify(response_object)

@app.route("/orden",methods=['POST','GET'])
def ordenVenta():
    """
    Controlador de órdenes de venta
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearOrden(data,response_object)  
    elif request.method=="GET":
        response_object=consultarOrdenes(response_object)  
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

@app.route("/cliente/<telefono>",methods=['PUT','DELETE'])
def single_cliente(telefono):
    """
    Ruta de clientes para actualizar y eliminar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarCliente(data,response_object,telefono)
    elif request.method=="DELETE":
        response_object=eliminarCliente(response_object,telefono)
    return jsonify(response_object)

@app.route("/producto",methods=['POST','GET'])
def producto():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearProducto(data,response_object)
    else:
        response_object=consultarProductos(response_object)
    return jsonify(response_object)

@app.route("/producto/<referencia>",methods=['PUT','DELETE'])
def single_producto(referencia):
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarProducto(data,response_object,referencia)
    elif request.method=="DELETE":
        response_object=eliminarProducto(response_object,referencia)
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

@app.route("/empaque",methods=['POST','GET'])
def empaque():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCategoria(data,response_object)  
    else:
        response_object=consultarCategorias(response_object)
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
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearDespacho(data,response_object)  
    else:
        response_object=consultarDespachos(response_object)
    return jsonify(response_object)

@app.route("/despacho/<despacho_ID>",methods=['PUT','DELETE'])
def single_despacho(despacho_ID):
    """
    Ruta de despachos
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=crearDespacho(data,response_object)  
    else:
        response_object=consultarDespachos(response_object)
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
