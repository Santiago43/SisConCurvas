/*Actualizar un rol*/
update rol
set Nombre="Vendedor"
where Rol_ID = 2;
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

/*Actualizar los datos de un cliente*/
update Persona as p, Cliente as c
set p.Primer_nombre="Juan", 
p.Segundo_nombre="Sebastián", 
p.Primer_apellido="Bueno", 
p.Segundo_apellido="Ramírez",
p.Telefono="3257550036",
p.correo="juan@example.com",
c.tipo_cliente=true
where p.Telefono="3257550036" and p.Persona_ID=c.Persona_ID;


/*Actualizar una orden de venta*/
update Orden_venta set
Motivo_ID =1,
Origen_ID=1,
Modalidad_pago_ID=1,
Metodo_compra_ID=1,
Direccion_id=1,
Cliente_ID=1,
Usuario_ID=1,
Estado="No empacado",
Nota="Es una prueba",
Fecha_entrega="2021-01-15",
Tipo_venta=false,
Descuento=null
where Orden_venta_ID=1;

