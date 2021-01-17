/*Insertar usuario*/

delimiter $$

create procedure insertarUsuario (
in _Primer_nombre varchar(20),
in _Segundo_nombre varchar(20), 
in _Primer_apellido varchar(20),
in _Segundo_apellido varchar(20),
in _Tipo_documento varchar(20), 
in _Documento varchar(20),
in _Telefono varchar(20),
in _Correo varchar(30),
in _Rol_ID int,
in _Contraseña varchar(200),
in _Url_imagen varchar(200),
in token varchar(200)
)
begin
insert into Persona (Primer_nombre,Segundo_nombre,Primer_apellido,Segundo_apellido,Telefono,Correo)
values(_Primer_nombre,_Segundo_nombre,_Primer_apellido,_Segundo_apellido,_Telefono,_Correo);
insert into Usuario (Rol_ID, Persona_ID,Contraseña,Url_imagen,Tipo_documento,Documento,estado,token) values (_Rol_ID, (select Persona_ID from Persona order by Persona_ID desc limit 1),sha(_Contraseña),_Url_imagen,_Tipo_documento,_Documento,true,token);
end $$

drop procedure insertarProducto;
/*Insertar Producto*/
delimiter $$
create procedure insertarProducto (
in _Referencia_Producto_ID varchar (30),
in _Descripcion varchar(50),
in _Url_imagen varchar(200),
in _Stock int,
in _Precio_costo double,
in _Precio_venta double,
in _Categoria_ID int
)
begin
insert into Inventario(Referencia_Producto_ID,Descripcion,Url_imagen,Stock,Precio_costo,Precio_venta)
values(_Referencia_Producto_ID,_Descripcion,_Url_imagen,_Stock,_Precio_costo,_Precio_venta);
insert into Inventario_tiene_Categoria values (_Referencia_Producto_ID,_Categoria_ID);
end $$

delimiter $$

create procedure insertarCliente (
in _Primer_nombre varchar(20),
in _Segundo_nombre varchar(20), 
in _Primer_apellido varchar(20),
in _Segundo_apellido varchar(20),
in _Telefono varchar(20),
in _Correo varchar(30),
in _tipoCliente bool 
)
begin
insert into Persona (Primer_nombre,Segundo_nombre,Primer_apellido,Segundo_apellido,Telefono,Correo)
values(_Primer_nombre,_Segundo_nombre,_Primer_apellido,_Segundo_apellido,_Telefono,_Correo);
insert into Cliente (Persona_ID, tipo_cliente) values ((select Persona_ID from Persona order by Persona_ID desc limit 1), _tipoCliente);
end $$