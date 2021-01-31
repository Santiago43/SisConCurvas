#Roles

delete from rol where Rol_ID=1;

/*Remover permisos a roles*/

delete from rol_tiene_permiso
where (Rol_ID,Permiso_ID) =(1,1);


delete from Rol_tiene_Permiso where (Rol_ID,Permiso_ID)=(
(select Rol_ID from Rol where Nombre="Administrador"),
(select Permiso_ID from Permiso where Nombre="Inventario.editar"));

/*Eliminar un usuario mediante su cedula*/
delete from usuario
where Persona_ID=(select Persona_ID from persona where Documento=1234567891);

delete from persona 
where Documento=1234567891;

/*Eliminar un producto del inventario*/

delete from Inventario
where Referencia_Producto_ID="abdcdf";


/*Eliminar una orden de venta*/

delete from Orden_venta
where Orden_venta_ID=1;

/*Eliminar producto de una orden de venta*/
delete from Orden_venta_tiene_producto
where (Orden_venta_ID,Inventario_Referencia_Producto_ID)=(1,"abdcfe");

/*Eliminar pago*/
delete from Pago_domiciliario where Pago_domiciliario_ID=2;


delete from Distribucion where Distribucion_ID=1;

delete from Distribucion_tiene_prendas_Devueltas where (Distribucion_ID,Inventario_Referencia_producto_ID)=(2,"abdcdf");
