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
in _token varchar(200),
in _usuario varchar(30)
)
begin
insert into Persona (Primer_nombre,Segundo_nombre,Primer_apellido,Segundo_apellido,Telefono,Correo)
values(_Primer_nombre,_Segundo_nombre,_Primer_apellido,_Segundo_apellido,_Telefono,_Correo);
insert into Usuario (Rol_ID, Persona_ID,Contraseña,Url_imagen,Tipo_documento,Documento,estado,token,usuario) values (_Rol_ID, (select Persona_ID from Persona order by Persona_ID desc limit 1),sha(_Contraseña),_Url_imagen,_Tipo_documento,_Documento,true,_token,_usuario);
end $$

#Crear cliente
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

#Crear pago domiciliario
delimiter $$

create procedure insertarPagoDomiciliario (
in _monto double,
in _Domiciliario_ID integer, 
in _Financiero_ID integer,
in _estado boolean
)
begin
insert into Pago_domiciliario (Estado,monto,fecha_pago)
values(_estado,_monto,(cast(sysdate() as date)));
insert into Domiciliario_tiene_Pago(Pago_domiciliario_ID, Usuario_ID) values ((select Pago_domiciliario_ID from Pago_domiciliario order by Pago_domiciliario_ID desc limit 1),_Domiciliario_ID);
insert into Financiero_hace_pago(Usuario_ID,Pago_domiciliario_ID) values(_Financiero_ID,(select Pago_domiciliario_ID from Pago_domiciliario order by Pago_domiciliario_ID desc limit 1));

end $$