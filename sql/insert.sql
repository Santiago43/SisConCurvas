/**/
insert into Rol (Nombre) values ("Administrador");
insert into Rol (Nombre) values ("Vendedor");
/*Crear permisos*/
insert into Permiso (Nombre) values ("Usuarios.crear");
insert into Permiso (Nombre) values ("Usuarios.ver");
insert into Permiso (Nombre) values ("Usuarios.editar");
insert into Permiso (Nombre) values ("Usuarios.eliminar");

insert into Permiso (Nombre) values ("Orden.crear");
insert into Permiso (Nombre) values ("Orden.ver");
insert into Permiso (Nombre) values ("Orden.editar");
insert into Permiso (Nombre) values ("Orden.eliminar");
/*Agregar permisos a roles*/

insert into Rol_tiene_Permiso (Rol_ID,Permiso_ID)
values (1,1);

insert into Rol_tiene_Permiso(Rol_ID,Permiso_ID) 
values (
(select Rol_ID from Rol where Nombre="Vendedor"),
(select Permiso_ID from Permiso where Nombre="Orden.crear"));

/*Insertar usuario*/
call insertarUsuario("Pedro","Antonio","Pataquiva","Rugeles","Cédula de ciudadanía","1234567890","3257550034","pedro@example.com",1,"1234");
call insertarUsuario("Jorge","Alberto","Sánchez","Cárdenas","Cédula de ciudadanía","2345678901","3257550034","jorge@example.com",(select Rol_ID from Rol where Nombre="Vendedor"),"1234");

/*Insertar motivos en órdenes de venta*/
insert into Motivo (Tipo, Motivo) values ("Venta","Venta");
insert into Motivo (Tipo, Motivo) values ("Venta","Cambio");

insert into Motivo (Tipo, Motivo) values ("No empaque","Falta de existencias en inventarios");


/*Insertar cliente*/
call insertarCliente("Juan","Sebastián","Bueno","Ramírez","Cédula de ciudadanía","3456789012","3257550034","juan@example.com",true);
/*Insertar categoria padre*/

insert into Categoria(Nombre) values ("Elegante");

/*Insertar categoría*/
insert into Categoria(Nombre,Padre_categoria_ID) values ("Gala",null);


/*Insertar producto a inventario*/
call insertarProducto("abdcdf","Camiseta Polo","img/src.jpg",2,20000,35000,1);


/*Insertar ciudad*/
insert into Ciudad(Nombre) values("Bogotá D.C.");
insert into Ciudad(Nombre) values("Medellín");
insert into Ciudad(Nombre) values("Soacha");

/*Insertar Departamento*/
insert into Departamento (Departamento) values ("Cundinamarca");
insert into Departamento (Departamento) values ("Antioquia");


/*Insertar dirección*/
insert into Direccion (Ciudad_ID, Departamento_ID, Barrio, Direccion) values (1,1,"Las Cruces",'cra 7 # 2-24 sur');
insert into Direccion (Ciudad_ID, Departamento_ID, Barrio, Direccion) values (3,1,"San Mateo",'cra 14 este # 32a');

/*insert into Persona_tiene_direccion(Persona_ID,Direccion_id)
values (3,1);*/

/*Insertar origen*/

insert into Origen (Nombre_origen) values ("Facebook");
insert into Origen (Nombre_origen) values ("WhatsApp");

/*Insertar Modalidad de pago*/
insert into Modalidad_pago(Modalidad) values ("Efectivo");

/*Insertar Método de compra*/
insert into Metodo_compra (Tipo) values ("Contra entrega");

/*Insertar orden de venta*/
insert into Orden_venta 
(Origen_ID,Modalidad_pago_ID,Metodo_compra_ID,Direccion_id,Cliente_ID,Usuario_ID,Estado,Fecha_venta,Precio,Nota,Fecha_entrega,Tipo_venta,Descuento)
values
((select Origen_ID from Origen where Nombre_origen="Facebook"),
(select Modalidad_pago_ID from Modalidad_pago where Modalidad="Efectivo"),
(select Metodo_compra_ID from Metodo_compra where Tipo="Contra entrega"),
(select d.Direccion_id from Direccion as d where d.Direccion='cra 7 # 2-24 sur'),
1,
2,
"No empacado",
cast(sysdate() as DATE),
5000,
"Es prueba",
"2021-01-31",
false,
null
);

insert into Orden_venta_tiene_producto (Orden_venta_ID,Inventario_Referencia_Producto_ID,cantidad) 
values (1,"abdcdf",3);

/*Insertar distribución*/


/**/