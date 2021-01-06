/**/
insert into Rol (Nombre) values ("Administrador");

/*Crear permisos*/
insert into Permiso (Nombre) values ("Usuarios.crear");
insert into Permiso (Nombre) values ("Usuarios.ver");
insert into Permiso (Nombre) values ("Usuarios.editar");
insert into Permiso (Nombre) values ("Usuarios.eliminar");


/*Agregar permisos a roles*/

insert into Rol_tiene_Permiso (Rol_ID,Permiso_ID)
values (1,1);


/*Insertar usuario*/
call insertarUsuario("Pedro","Antonio","Pataquiva","Rugeles","Cédula de ciudadanía","1234567890","3257550034","pedro@example.com",1,"1234");

/*Insertar categoria padre*/

insert into Categoria(Nombre) values ("Elegante");

/*Insertar categoría*/
insert into Categoria(Nombre,Padre_categoria_ID) values ("Gala",null);

/*Insert cliente*/
call insertarCliente("Carlos","Juan","Rodriguez","Ramirez","Cédula de ciudadanía","123456","3257550034","carlos@example.com",false);
/*Insertar producto a inventario*/
call insertarProducto("abdcdf","Camiseta Polo","img/src.jpg",2,20000,35000,1);


/*Insertar ciudad*/
insert into Ciudad (Nombre) values("Bogotá D.C.");
insert into Ciudad (Nombre) values("Medellín");

/*Insertar Departamento*/
insert into Departamento (Departamento) values ("Cundinamarca");

/*Insertar dirección*/


