/**/
insert into Rol (Nombre) values ("Administrador");
insert into Rol (Nombre) values ("Vendedor");
insert into Rol (Nombre) values ("Financiero");
insert into Rol (Nombre) values ("Domiciliario");
/*Crear permisos*/
insert into Permiso (Nombre) values ("Usuarios.crear");
insert into Permiso (Nombre) values ("Usuarios.ver");
insert into Permiso (Nombre) values ("Usuarios.editar");
insert into Permiso (Nombre) values ("Usuarios.eliminar");

insert into Permiso (Nombre) values ("Orden.crear");
insert into Permiso (Nombre) values ("Orden.ver");
insert into Permiso (Nombre) values ("Orden.editar");
insert into Permiso (Nombre) values ("Orden.eliminar");

insert into Permiso (Nombre) values ("Empaque.crear");
insert into Permiso (Nombre) values ("Empaque.ver");
insert into Permiso (Nombre) values ("Empaque.editar");
insert into Permiso (Nombre) values ("Empaque.eliminar");

insert into Permiso (Nombre) values ("Despacho.crear");
insert into Permiso (Nombre) values ("Despacho.ver");
insert into Permiso (Nombre) values ("Despacho.editar");
insert into Permiso (Nombre) values ("Despacho.eliminar");

insert into Permiso (Nombre) values ("Distribucion.crear");
insert into Permiso (Nombre) values ("Distribucion.ver");
insert into Permiso (Nombre) values ("Distribucion.editar");
insert into Permiso (Nombre) values ("Distribucion.eliminar");

insert into Permiso (Nombre) values ("Rol.crear");
insert into Permiso (Nombre) values ("Rol.ver");
insert into Permiso (Nombre) values ("Rol.editar");
insert into Permiso (Nombre) values ("Rol.eliminar");


insert into Permiso (Nombre) values ("Pagodomiciliario.crear");
insert into Permiso (Nombre) values ("Pagodomiciliario.ver");
insert into Permiso (Nombre) values ("Pagodomiciliario.editar");
insert into Permiso (Nombre) values ("Pagodomiciliario.eliminar");

insert into Permiso (Nombre) values ("Inventario.crear");
insert into Permiso (Nombre) values ("Inventario.ver");
insert into Permiso (Nombre) values ("Inventario.editar");
insert into Permiso (Nombre) values ("Inventario.eliminar");

insert into Permiso (Nombre) values ("PermisoRol.modificar");
/*Agregar permisos a roles*/


insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Vendedor"),
(select Permiso_ID from Permiso where Nombre="Orden.crear"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Rol.crear"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Rol.ver"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Rol.editar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Pagodomiciliario.crear"));
insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Pagodomiciliario.ver"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Pagodomiciliario.editar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Pagodomiciliario.eliminar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Inventario.crear"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Inventario.ver"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Inventario.editar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Inventario.eliminar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Distribucion.ver"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Distribucion.crear"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Distribucion.editar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Distribucion.eliminar"));


insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Usuarios.ver"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Usuarios.crear"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Usuarios.editar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Usuarios.eliminar"));

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Orden.ver"));

/*Insertar usuario*/
call insertarUsuario("Pedro","Antonio","Pataquiva","Rugeles","Cédula de ciudadanía","1234567890","3257550034","pedro@example.com",1,"1234","profile1.jpg","1234567890987654321","Pepataquiva");
call insertarUsuario("Jorge","Alberto","Sánchez","Cárdenas","Cédula de ciudadanía","2345678901","3257550035","jorge@example.com",(select Rol_ID from Rol where Nombre="Vendedor"),"1234","profile2.jpg","#$%&/()=)(/&%$#","JogeSan");
call insertarUsuario("Jorge","Alberto","Sánchez","Cárdenas","Cédula de ciudadanía","2345678902","3257550030","jorge2@example.com",(select Rol_ID from Rol where Nombre="Domiciliario"),"1234","profile2.jpg",".$%&/()=)(/&%$#","JogeSan2");
/*Insertar motivos en órdenes de venta*/
insert into Motivo (Tipo, Motivo) values ("Venta","Venta");
insert into Motivo (Tipo, Motivo) values ("Venta","Cambio");

insert into Motivo (Tipo, Motivo) values ("No empaque","Falta de existencias en inventarios");

insert into Motivo (Tipo,Motivo) values ("No distribución", "Dirección errónea");

/*Insertar cliente*/
call insertarCliente("Juan","Sebastián","Bueno","Ramírez","3257550036","juan@example.com",true);
/*Insertar categoria padre*/

insert into Categoria(Nombre) values ("Elegante");

/*Insertar categoría*/
insert into Categoria(Nombre,Padre_categoria_ID) values ("Gala",null);


/*Insertar producto a inventario*/

insert into Inventario(Referencia_Producto_ID,Descripcion,Url_imagen,Stock,Precio_costo,Precio_venta,Precio_mayorista)
values("abdcdf","Camiseta Polo","img/src.jpg",2,20000,35000,30000);

insert into Inventario_tiene_Categoria (Inventario_Referencia_Producto_ID,Categoria_ID) values ("abdcdf",1);





/*Insertar dirección*/
insert into Direccion (Ciudad_ID, Barrio, Direccion) values ((select Ciudad_ID from Ciudad where Nombre="Bogotá D.C."),"Las Cruces",'cra 7 # 2-24 sur');
insert into Direccion (Ciudad_ID, Barrio, Direccion) values ((select Ciudad_ID from Ciudad where Nombre="Soacha"),"San Mateo",'cra 14 este # 32a');

insert into Persona_tiene_Direccion(Persona_ID,Direccion_id)
values (3,1);
/*Insertar origen*/

insert into Origen (Nombre_origen) values ("Facebook");
insert into Origen (Nombre_origen) values ("WhatsApp");

/*Insertar Modalidad de pago*/
insert into Modalidad_pago(Modalidad) values ("Efectivo");

/*Insertar Método de compra*/
insert into Metodo_compra (Tipo) values ("Contra entrega");

/*Insertar orden de venta*/
insert into Orden_venta 
(Origen_ID,Motivo_ID,Modalidad_pago_ID,Metodo_compra_ID,Direccion_id,Cliente_ID,Usuario_ID,Estado,Fecha_venta,Nota,Fecha_entrega,Tipo_venta,Descuento,precio)
values
((select Origen_ID from Origen where Nombre_origen="Facebook"),
(select Motivo_ID from Motivo where Motivo="Venta"),
(select Modalidad_pago_ID from Modalidad_pago where Modalidad="Efectivo"),
(select Metodo_compra_ID from Metodo_compra where Tipo="Contra entrega"),
(select d.Direccion_id from Direccion as d where d.Direccion='cra 7 # 2-24 sur'),
1,
2,
"No empacado",
sysdate(),
"Es prueba",
"2021-01-31",
false,
null,
105000
);

insert into Orden_venta_tiene_producto (Orden_venta_ID,Inventario_Referencia_Producto_ID,cantidad) 
values (1,"abdcdf",3);

/*Insertar distribución*/


/**/

insert into Ruta (Nombre) values ("Norte");

insert into Despacho(Usuario_ID,Orden_venta_ID,Ruta_ID,Estado,Fecha_despacho,Motivo_ID,Id_envia) values (1,1,1,1,'12/01/20',1,1);
/*Insertar pago a domiciliario*/
call insertarPagoDomiciliario(6000,1,1,true);


/*Insertar Distribución*/

insert into Distribucion(Usuario_ID,Despacho_ID,Estado,Motivo_ID,Venta_neta,Costo_distribucion)
values(1,1,false,null,50000,3000);
/*Agregar prendas devueltas a la distribución*/
insert into Distribucion_tiene_prendas_Devueltas(Distribucion_ID,Inventario_Referencia_Producto_ID,cantidad)
values (1,"abdcdf",1);
