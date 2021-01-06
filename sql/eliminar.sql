#Roles

delete from rol where Rol_ID=1;

/*Remover permisos a roles*/

delete from rol_tiene_permiso
where (Rol_ID,Permiso_ID) =(1,1);


/*Eliminar un usuario mediante su cedula*/
delete from usuario
where Persona_ID=(select Persona_ID from persona where Documento=1234567891);

delete from persona 
where Documento=1234567891;

/*Eliminar un producto del inventario*/

delete from Inventario
where Referencia_Producto_ID="abdcdf";
