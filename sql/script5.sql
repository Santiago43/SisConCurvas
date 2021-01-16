drop database if exists concurvas;
create database concurvas;
use concurvas;

CREATE TABLE Inventario (
  Referencia_Producto_ID VARCHAR(20) NOT NULL,
  Descripcion VARCHAR(150) NULL,
  Url_imagen VARCHAR(200) NULL,
  Stock INTEGER UNSIGNED NULL,
  Precio_costo DOUBLE NULL,
  Precio_venta DOUBLE NULL,
  PRIMARY KEY(Referencia_Producto_ID)
);

CREATE TABLE Pago_domiciliario (
  Pago_domiciliario_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Estado BOOL NULL,
  Monto DOUBLE NULL,
  PRIMARY KEY(Pago_domiciliario_ID)
);

CREATE TABLE Permiso (
  Permiso_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(20) NULL,
  PRIMARY KEY(Permiso_ID)
);

CREATE TABLE Rol (
  Rol_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(20) not NULL unique,
  PRIMARY KEY(Rol_ID)
);

CREATE TABLE Persona (
  Persona_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Primer_nombre VARCHAR(20) NOT NULL,
  Segundo_nombre VARCHAR(20) NULL,
  Primer_apellido VARCHAR(20) NOT NULL,
  Segundo_apellido VARCHAR(20) NULL,
  Telefono VARCHAR(20) NULL unique,
  Correo VARCHAR(30) NOT NULL,
  PRIMARY KEY(Persona_ID)
);

CREATE TABLE Origen (
  Origen_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Nombre_origen VARCHAR(30) NOT NULL,
  PRIMARY KEY(Origen_ID)
);

CREATE TABLE Motivo (
  Motivo_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Tipo VARCHAR(30) NOT NULL,
  Motivo VARCHAR(200) NOT NULL,
  PRIMARY KEY(Motivo_ID)
);

CREATE TABLE Metodo_compra (
  Metodo_compra_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Tipo VARCHAR(30) NOT NULL,
  PRIMARY KEY(Metodo_compra_ID)
);

CREATE TABLE Modalidad_pago (
  Modalidad_pago_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Modalidad VARCHAR(30) NULL,
  PRIMARY KEY(Modalidad_pago_ID)
);

CREATE TABLE Ruta (
  Ruta_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(50) NULL,
  PRIMARY KEY(Ruta_ID)
);

CREATE TABLE Departamento (
  Departamento_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Departamento VARCHAR(30) NULL,
  PRIMARY KEY(Departamento_ID)
);

CREATE TABLE Ciudad (
  Ciudad_ID BIGINT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(50) NULL,
  Departamento_ID integer unsigned not null,
  PRIMARY KEY(Ciudad_ID),
  INDEX Ciudad_FKIndex1(Departamento_ID),
  FOREIGN KEY(Departamento_ID)
    REFERENCES Departamento(Departamento_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Cliente (
  Cliente_ID Integer NOT NULL AUTO_INCREMENT,
  Persona_ID INTEGER UNSIGNED NOT NULL,
  tipo_cliente bool null,
  PRIMARY KEY(Cliente_ID),
  INDEX Cliente_FKIndex1(Persona_ID),
  FOREIGN KEY(Persona_ID)
    REFERENCES Persona(Persona_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Control_Inventario (
  Control_Inventario_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Inventario_Referencia_Producto_ID VARCHAR(20) NOT NULL,
  Fecha DATE NULL,
  Inventario_inicial INTEGER UNSIGNED NULL,
  Detalle VARCHAR(150) NULL,
  Numero_prendas INTEGER UNSIGNED NULL,
  Tipo BOOL NULL,
  PRIMARY KEY(Control_Inventario_ID),
  INDEX Control_Inventario_FKIndex1(Inventario_Referencia_Producto_ID),
  FOREIGN KEY(Inventario_Referencia_Producto_ID)
    REFERENCES Inventario(Referencia_Producto_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Categoria (
  Categoria_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Padre_categoria_ID INTEGER UNSIGNED NULL,
  Nombre VARCHAR(20) not NULL unique,
  PRIMARY KEY(Categoria_ID),
  INDEX Categoria_FKIndex1(Padre_categoria_ID),
  FOREIGN KEY(Padre_categoria_ID)
    REFERENCES Categoria(Categoria_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Rol_tiene_Permiso (
  Rol_ID INTEGER UNSIGNED NOT NULL,
  Permiso_ID INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Rol_ID, Permiso_ID),
  INDEX Rol_tiene_Permiso_FKIndex1(Rol_ID),
  INDEX Rol_tiene_Permiso_FKIndex2(Permiso_ID),
  FOREIGN KEY(Rol_ID)
    REFERENCES Rol(Rol_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Permiso_ID)
    REFERENCES Permiso(Permiso_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Usuario (
  Usuario_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Rol_ID INTEGER UNSIGNED NOT NULL,
  Persona_ID INTEGER UNSIGNED NOT NULL,
  Contraseña VARCHAR(200) NOT NULL,
  Url_imagen varchar(200) null,
  Tipo_documento VARCHAR(20) NULL,
  Documento VARCHAR(20) not NULL unique,
  estado boolean not null,
  PRIMARY KEY(Usuario_ID),
  INDEX Usuario_FKIndex1(Persona_ID),
  INDEX Usuario_FKIndex2(Rol_ID),
  FOREIGN KEY(Persona_ID)
    REFERENCES Persona(Persona_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Rol_ID)
    REFERENCES Rol(Rol_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Domiciliario_tiene_Pago (
  Pago_domiciliario_ID INTEGER UNSIGNED NOT NULL,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Pago_domiciliario_ID, Usuario_ID),
  INDEX Pago_domiciliario_has_Usuario_FKIndex1(Pago_domiciliario_ID),
  INDEX Pago_domiciliario_has_Usuario_FKIndex2(Usuario_ID),
  FOREIGN KEY(Pago_domiciliario_ID)
    REFERENCES Pago_domiciliario(Pago_domiciliario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Direccion (
  Direccion_id BIGINT NOT NULL AUTO_INCREMENT,
  Ciudad_ID BIGINT NOT NULL,
  Departamento_ID INTEGER UNSIGNED NOT NULL,
  Barrio VARCHAR(50) NULL,
  Direccion VARCHAR(60) NOT NULL,
  PRIMARY KEY(Direccion_id),
  INDEX Direccion_FKIndex1(Departamento_ID),
  INDEX Direccion_FKIndex2(Ciudad_ID),
  FOREIGN KEY(Departamento_ID)
    REFERENCES Departamento(Departamento_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Ciudad_ID)
    REFERENCES Ciudad(Ciudad_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Control_Rol (
  Control_Rol_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Rol_ID INTEGER UNSIGNED NOT NULL,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Fecha_modificacion DATE NOT NULL,
  Tipo INTEGER UNSIGNED NOT NULL,
  Detalle VARCHAR(200) NULL,
  PRIMARY KEY(Control_Rol_ID),
  INDEX Control_Rol_FKIndex1(Usuario_ID),
  INDEX Control_Rol_FKIndex2(Rol_ID),
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Rol_ID)
    REFERENCES Rol(Rol_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Inventario_tiene_Categoria (
  Inventario_Referencia_Producto_ID VARCHAR(20) NOT NULL,
  Categoria_ID INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Inventario_Referencia_Producto_ID, Categoria_ID),
  INDEX Inventario_tiene_Categoria_FKIndex1(Inventario_Referencia_Producto_ID),
  INDEX Inventario_tiene_Categoria_FKIndex2(Categoria_ID),
  FOREIGN KEY(Inventario_Referencia_Producto_ID)
    REFERENCES Inventario(Referencia_Producto_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Categoria_ID)
    REFERENCES Categoria(Categoria_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Financiero_hace_pago (
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Pago_domiciliario_ID INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Usuario_ID, Pago_domiciliario_ID),
  INDEX Usuario_has_Pago_domiciliario_FKIndex1(Usuario_ID),
  INDEX Usuario_has_Pago_domiciliario_FKIndex2(Pago_domiciliario_ID),
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Pago_domiciliario_ID)
    REFERENCES Pago_domiciliario(Pago_domiciliario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Orden_venta (
  Orden_venta_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Motivo_ID INTEGER UNSIGNED NULL,
  Origen_ID INTEGER UNSIGNED NOT NULL,
  Modalidad_pago_ID INTEGER UNSIGNED NOT NULL,
  Metodo_compra_ID INTEGER UNSIGNED NOT NULL,
  Direccion_id BIGINT NOT NULL,#
  Cliente_ID Integer NOT NULL,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Estado VARCHAR(50) NOT NULL,
  Fecha_venta timestamp NOT NULL,
  Nota VARCHAR(150) NULL,#
  Fecha_entrega DATE NOT NULL,
  Tipo_venta BOOL NULL,
  Descuento FLOAT NULL,#
  PRIMARY KEY(Orden_venta_ID),
  INDEX Orden_venta_FKIndex1(Usuario_ID),
  INDEX Orden_venta_FKIndex2(Cliente_ID),
  INDEX Orden_venta_FKIndex3(Direccion_id),
  INDEX Orden_venta_FKIndex4(Metodo_compra_ID),
  INDEX Orden_venta_FKIndex5(Modalidad_pago_ID),
  INDEX Orden_venta_FKIndex6(Origen_ID),
  INDEX Orden_venta_FKIndex7(Motivo_ID),
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Cliente_ID)
    REFERENCES Cliente(Cliente_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Direccion_id)
    REFERENCES Direccion(Direccion_id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Metodo_compra_ID)
    REFERENCES Metodo_compra(Metodo_compra_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Modalidad_pago_ID)
    REFERENCES Modalidad_pago(Modalidad_pago_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Origen_ID)
    REFERENCES Origen(Origen_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Motivo_ID)
    REFERENCES Motivo(Motivo_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Persona_tiene_Direccion (
  Persona_ID INTEGER UNSIGNED NOT NULL,
  Direccion_id BIGINT NOT NULL,
  PRIMARY KEY(Persona_ID, Direccion_id),
  INDEX Persona_tiene_Direccion_FKIndex1(Persona_ID),
  INDEX Persona_tiene_Direccion_FKIndex2(Direccion_id),
  FOREIGN KEY(Persona_ID)
    REFERENCES Persona(Persona_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Direccion_id)
    REFERENCES Direccion(Direccion_id)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Usuario_tiene_Permiso (
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Permiso_ID INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Usuario_ID, Permiso_ID),
  INDEX Usuario_tiene_Permiso_FKIndex1(Usuario_ID),
  INDEX Usuario_tiene_Permiso_FKIndex2(Permiso_ID),
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Permiso_ID)
    REFERENCES Permiso(Permiso_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Control_venta (
  Control_venta_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Orden_venta_ID INTEGER UNSIGNED NOT NULL,
  Fecha_modificacion DATE NULL,
  Cambio VARCHAR(200) NULL,
  PRIMARY KEY(Control_venta_ID),
  INDEX Control_venta_FKIndex1(Orden_venta_ID),
  INDEX Control_venta_FKIndex2(Usuario_ID),
  FOREIGN KEY(Orden_venta_ID)
    REFERENCES Orden_venta(Orden_venta_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Orden_venta_tiene_producto (
  Orden_venta_ID INTEGER UNSIGNED NOT NULL,
  Inventario_Referencia_Producto_ID VARCHAR(20) NOT NULL,
  cantidad INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Orden_venta_ID, Inventario_Referencia_Producto_ID),
  INDEX Orden_venta_has_Inventario_FKIndex1(Orden_venta_ID),
  INDEX Orden_venta_has_Inventario_FKIndex2(Inventario_Referencia_Producto_ID),
  FOREIGN KEY(Orden_venta_ID)
    REFERENCES Orden_venta(Orden_venta_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Inventario_Referencia_Producto_ID)
    REFERENCES Inventario(Referencia_Producto_ID)
      ON DELETE cascade
      ON UPDATE cascade
);

CREATE TABLE Empaque (
  Empaque_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Orden_venta_ID INTEGER UNSIGNED NOT NULL,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Numero_prendas INTEGER UNSIGNED NOT NULL,
  Estado BOOL NOT NULL,
  Observaciones VARCHAR(200) NULL,
  Motivo_ID INTEGER UNSIGNED NULL,
  PRIMARY KEY(Empaque_id, Orden_venta_ID),
  INDEX Empaque_FKIndex1(Usuario_ID),
  INDEX Empaque_FKIndex2(Orden_venta_ID),
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Orden_venta_ID)
    REFERENCES Orden_venta(Orden_venta_ID)
      ON DELETE cascade
      ON UPDATE cascade,
   FOREIGN KEY(Motivo_ID)
    REFERENCES Motivo(Motivo_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Despacho (
  Despacho_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Orden_venta_ID INTEGER UNSIGNED NOT NULL,
  Ruta_ID INTEGER UNSIGNED NOT NULL,
  Estado BOOL NOT NULL,
  Fecha_despacho DATE NULL,
  Motivo_ID INTEGER UNSIGNED NULL,
  Id_envia  VARCHAR(50) NULL,
  PRIMARY KEY(Despacho_ID),
  INDEX Despacho_FKIndex1(Ruta_ID),
  INDEX Despacho_FKIndex2(Orden_venta_ID),
  INDEX Despacho_FKIndex3(Usuario_ID),
  FOREIGN KEY(Ruta_ID)
    REFERENCES Ruta(Ruta_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Orden_venta_ID)
    REFERENCES Orden_venta(Orden_venta_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Motivo_ID)
    REFERENCES Motivo(Motivo_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Distribucion (
  Distribucion_ID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Usuario_ID INTEGER UNSIGNED NOT NULL,
  Despacho_ID INTEGER UNSIGNED NOT NULL,
  Estado BOOL NOT NULL,
  Motivo_ID INTEGER UNSIGNED NULL,
  Venta_neta DOUBLE NULL,
  Costo_distribucion DOUBLE NULL,
  PRIMARY KEY(Distribucion_ID),
  INDEX Distribucion_FKIndex1(Despacho_ID),
  INDEX Distribucion_FKIndex2(Usuario_ID),
  INDEX Distribucion_FKIndex3(Motivo_ID),
  FOREIGN KEY(Despacho_ID)
    REFERENCES Despacho(Despacho_ID)
      ON DELETE cascade
      ON UPDATE cascade,
  FOREIGN KEY(Motivo_ID)
    REFERENCES Motivo(Motivo_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Usuario_ID)
    REFERENCES Usuario(Usuario_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE Distribucion_tiene_prendas_Devueltas (
  Distribucion_ID INTEGER UNSIGNED NOT NULL,
  Inventario_Referencia_Producto_ID VARCHAR(20) NOT NULL,
  cantidad INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Distribucion_ID, Inventario_Referencia_Producto_ID),
  INDEX Distribucion_has_Inventario_FKIndex1(Distribucion_ID),
  INDEX Distribucion_has_Inventario_FKIndex2(Inventario_Referencia_Producto_ID),
  FOREIGN KEY(Distribucion_ID)
    REFERENCES Distribucion(Distribucion_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Inventario_Referencia_Producto_ID)
    REFERENCES Inventario(Referencia_Producto_ID)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);



