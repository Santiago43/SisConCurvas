
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
select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID from Persona as p
inner join Usuario as u on u.Persona_ID=p.Persona_ID
where Documento=1234567890;

/*Y sus direcciones asociadas*/
select d.* from Direccion as d
inner join Persona_tiene_Direccion as pd on d.Direccion_id
inner join Persona as p on p.Persona_ID=pd.Persona_ID
where p.Telefono="3777777";
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

/*Clientes*/
select p.*,c.Cliente_ID,tipo_cliente from Persona as p 
inner join Cliente as c 
on c.Persona_ID=p.Persona_ID;

select p.*,c.* from Persona as p 
inner join Cliente as c 
on c.Persona_ID=p.Persona_ID
where p.Telefono='3257550036';

/*Consultar vendedores*/

select p.*,u.* from Usuario as u
inner join Persona as p on p.Persona_ID=u.Persona_ID
inner join Rol as r on u.Rol_ID=r.Rol_ID
where r.Rol_ID = (select Rol_ID from Rol where Nombre="Vendedor");

/**/
select p.*,u.* from Usuario as u
inner join Persona as p on p.Persona_ID=u.Persona_ID
inner join Rol as r on u.Rol_ID=r.Rol_ID
where r.Rol_ID = (select Rol_ID from Rol where Nombre="Domiciliario");

/*Consultar usuario mediante correo y contraseña*/
select p.*,u.* from Usuario as u
inner join Persona as p on p.Persona_ID=u.Persona_ID
where p.Correo = "pedro@example.com" and u.Contraseña=sha("1234");

/*Consultar orden de venta*/
select *,(select sum(q.Precio_venta*q.cantidad) from (select i.Precio_venta, oc.cantidad from Inventario as i
		inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
		inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
		where o.Orden_venta_ID=ov.Orden_venta_ID) as q) as precio  from Orden_venta as ov;

select i.*, oc.cantidad from Inventario as i
inner join Orden_venta_tiene_producto as oc on oc.Inventario_Referencia_Producto_ID = i.Referencia_Producto_ID
inner join Orden_venta as o on oc.Orden_venta_ID = o.Orden_Venta_ID
where o.Orden_venta_ID=1;

select * from Empaque;


select p.* from Rol_tiene_Permiso as rp inner join Rol as r on r.Rol_ID=rp.Rol_ID 
inner join Permiso as p on p.Permiso_ID=rp.Permiso_ID where r.Rol_ID=1;
select * from Permiso;

select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token from Persona as p inner join Usuario as u on u.Persona_ID=p.Persona_ID;
select p.*,u.Rol_ID,u.Contraseña,u.usuario_ID,u.Url_imagen,u.Tipo_documento,u.Documento,u.estado,u.token from Usuario as u
            inner join Persona as p on p.Persona_ID=u.Persona_ID;

select p.* from Usuario_tiene_Permiso as up inner join Usuario as u on u.Usuario_ID=up.Usuario_ID 
inner join Permiso as p on p.Permiso_ID=up.Permiso_ID where u.Usuario_ID=1;
select * from Permiso;


select * from Motivo;
select * from Origen;


select * from Control_Rol;

select * from Control_Inventario;


select * from Control_venta;


select pd.*,dp.Usuario_ID as Domiciliario_ID,fp.Usuario_ID as Financiero_ID from Pago_domiciliario as pd
inner join Domiciliario_tiene_Pago as dp on dp.Pago_domiciliario_ID=pd.Pago_domiciliario_ID
inner join Financiero_hace_pago as fp on pd.Pago_domiciliario_ID=fp.Pago_domiciliario_ID
where pd.Pago_domiciliario_ID=2;

select * from Pago_domiciliario;

select p.*,dp.cantidad from Inventario as p
inner join Distribucion_tiene_prendas_Devueltas as dp on dp.Inventario_Referencia_Producto_ID=p.Referencia_Producto_ID
inner join Distribucion as d on d.Distribucion_ID=dp.Distribucion_ID
where d.Distribucion_ID=1;

select c.* from Categoria as c
inner join Inventario_tiene_Categoria as ic on ic.Categoria_ID=c.Categoria_ID
where ic.Inventario_Referencia_Producto_ID="abdcdf";

select * from Despacho;
select * from Distribucion where Distribucion_ID=1;