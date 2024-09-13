CREATE DATABASE Ensambladora;
USE Ensambladora;

CREATE TABLE Clientes (
    Id_cliente bigint PRIMARY KEY AUTO_INCREMENT,
    cliente varchar(40),
    Celular varchar(20),
    Domicilio varchar(40)
);

INSERT INTO clientes VALUES(null, 'Adrian Eduardo', '6623454245', 'Ernesto Dany #7');
INSERT INTO clientes VALUES(null, 'Pepe segundo', '6622222222', 'Ernesto Dany #9');
INSERT INTO clientes VALUES(null, 'Carlos Gamez', '6623321685', 'Ernesto Dany #11');

CREATE TABLE ventas (
    id_ventas bigint PRIMARY KEY AUTO_INCREMENT,
    id_cliente bigint,
    id_componen bigint,
    Monto decimal,
    FechaHora date
);

INSERT INTO ventas VALUES(null, 1, 1, 99, '2024-02-12');
INSERT INTO ventas VALUES(null, 2, 2, 500, '2024-01-11');
INSERT INTO ventas VALUES(null, 3, 3, 10000, '2023-12-29');

CREATE TABLE componentes (
    id_componen bigint PRIMARY KEY AUTO_INCREMENT,
    componente varchar(40),
    precio int,
    Disponible int
);

INSERT INTO componentes VALUES(null, 'Intel Core i3-4150', 5500, 12);
INSERT INTO componentes VALUES(null, 'amd Radeon RX 560', 2100, 15);
INSERT INTO componentes VALUES(null, 'kingston fury ddr3 8gb', 3700, 10);

CREATE TABLE Usuarios (
    Id_usuario bigint PRIMARY KEY AUTO_INCREMENT,
    Usuario varchar(40),
    Cuenta varchar(20),
    Clave varchar(128),
    nivel int,
    Idioma int
);

INSERT INTO Usuarios VALUES(null, 'Sadrach', 'admin', md5('12345'),1,1);



