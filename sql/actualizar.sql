/*Actualizar un rol*/
update rol
set Nombre="Administrador"
where Rol_ID = 1;
set SQL_SAFE_UPDATES=0;

/*Actualizar los datos de un usuario*/
update persona as p, usuario as u
set p.Primer_nombre="Pedro", 
p.Segundo_nombre="Antonio", 
p.Primer_apellido="Pataquiva", 
p.Segundo_apellido="Rugeles",
p.Tipo_documento="Cédula de ciudadanía",
p.Telefono="3777777",
p.correo="pedro@example.com",
u.Rol_ID=1,
u.Contraseña=sha("1234")
where p.Documento="1234567890" and p.Persona_ID=u.Persona_ID;


/*Actualizar una categoria*/
update categoria
set Padre_categoria_ID=1,
Nombre="Polo"
where Categoria_ID=2;

/*Actualizar un producto del inventario*/
update Inventario
set Descripcion="Camiseta Polo",
Url_imagen="",
Stock=3,
Precio_costo=20000,
Precio_venta=35000
where Referencia_Producto_ID="abdcdf";
