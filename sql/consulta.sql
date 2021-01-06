
/*Consultar todos los roles*/
select * from Rol;

/*Consultar rol por id*/
select * from Rol where Rol_ID=2;

/*Consultar todos los permisos que tienen todos los roles*/
select * from Rol_tiene_Permiso;


/*Consultar los permisos de un rol*/
select p.* from Rol_tiene_Permiso as rp
inner join Rol as r on r.Rol_ID=rp.Rol_ID
inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID
where r.Rol_ID=1;

#Usuarios

/*Consultar usuario por cédula*/
select p.*,u.Rol_ID,u.Contraseña from Persona as p
inner join Usuario as u on u.Persona_ID=p.Persona_ID
where Documento=1234567890;
#Categorías

/*Consultar categoría padre*/
select * from Categoria where Padre_categoria_ID is null;

/*Consultar categorias hijas*/
select * from Categoria where Padre_categoria_ID is not null;

select * from Categoria;


/*Consultar productos de inventario*/

select * from Inventario;

select * from Inventario_tiene_Categoria;

/*Consultar datos de un producto*/

select * from Inventario where Referencia_Producto_ID="abdcdf";

select c.* from Categoria as c
inner join Inventario_tiene_Categoria as ic on c.Categoria_ID=ic.Categoria_ID
where Inventario_Referencia_Producto_ID="abdcdf";

/* consulta cliente*/
select * from Persona as p 
inner join Cliente as c on c.Persona_ID=p.Persona_ID 
where Documento=123456
