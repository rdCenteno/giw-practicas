drop table if exists Marco;
drop table if exists Distribucion;
drop table if exists Ventas;
drop table if exists Clientes;
drop table if exists Concesionarios;
drop table if exists Coches;
drop table if exists Marcas;

CREATE TABLE Marcas(

	cifm int AUTO_INCREMENT,
	nombre varchar(20),
	ciudad varchar(40),
	PRIMARY KEY (cifm)
);

CREATE TABLE Coches(

	codcoche int AUTO_INCREMENT,
	nombre varchar(20),
	modelo varchar(30),
	PRIMARY KEY (codcoche)
);

CREATE TABLE Concesionarios(

	cifc int,
	nombre varchar(30),
	ciudad varchar(30),
	PRIMARY KEY(cifc)
);

CREATE TABLE Clientes(

	dni int AUTO_INCREMENT,
	nombre varchar(20),
	apellido varchar(40),
	ciudad varchar(40),
	PRIMARY KEY (dni)
);

CREATE TABLE Ventas(

	cifc int,
	dni int,
	codcoche int,
	color varchar(15),
	PRIMARY KEY(cifc, dni, codcoche),
	FOREIGN KEY (cifc) REFERENCES Concesionarios(cifc),
	FOREIGN KEY (dni) REFERENCES Clientes(dni),
	FOREIGN KEY (codcoche) REFERENCES Coches(codcoche)
);

CREATE TABLE Distribucion(

	cifc int,
	codcoche int,
	cantidad int,
	PRIMARY KEY (cifc, codcoche),
	FOREIGN KEY (cifc) REFERENCES Concesionarios(cifc),
	FOREIGN KEY (codcoche) REFERENCES Coches(codcoche)
);

CREATE TABLE Marco(

	cifm int,
	codcoche int,
	PRIMARY KEY (cifm, codcoche),
	FOREIGN KEY (cifm) REFERENCES Marcas(cifm),
	FOREIGN KEY (codcoche) REFERENCES Coches(codcoche)
);


INSERT INTO Marcas
VALUES (1, "seat", "Madrid");
INSERT INTO Marcas
VALUES (2, "renault", "Barcelona");
INSERT INTO Marcas
VALUES (3, "citroen", "Valencia");
INSERT INTO Marcas
VALUES (4, "audi", "Madrid");
INSERT INTO Marcas
VALUES (5, "opel", "Bilbao");
INSERT INTO Marcas
VALUES (6, "bmw", "Barcelona");



INSERT INTO Coches
VALUES (1, "ibiza", "glx");
INSERT INTO Coches
VALUES (2, "ibiza", "gti");
INSERT INTO Coches
VALUES (3, "ibiza", "gtd");
INSERT INTO Coches
VALUES (4, "toledo", "gtd");
INSERT INTO Coches
VALUES (5, "cordoba", "Bilbao");
INSERT INTO Coches
VALUES (6, "megane", "1.6");
INSERT INTO Coches
VALUES (7, "megane", "gti");
INSERT INTO Coches
VALUES (8, "laguna", "gtd");
INSERT INTO Coches
VALUES (9, "laguna", "td");
INSERT INTO Coches
VALUES (10, "zx", "16v");
INSERT INTO Coches
VALUES (11, "zx", "td");
INSERT INTO Coches
VALUES (12, "xantia", "gtd");
INSERT INTO Coches
VALUES (13, "a4", "1.8");
INSERT INTO Coches
VALUES (14, "a4", "2.8");
INSERT INTO Coches
VALUES (15, "astra", "caravan");
INSERT INTO Coches
VALUES (16, "astra", "gti");
INSERT INTO Coches
VALUES (17, "corsa", "1.4");



INSERT INTO Marco
VALUES (1, 1);
INSERT INTO Marco
VALUES (1, 2);
INSERT INTO Marco
VALUES (1, 3);
INSERT INTO Marco
VALUES (1, 4);
INSERT INTO Marco
VALUES (1, 5);
INSERT INTO Marco
VALUES (2, 6);
INSERT INTO Marco
VALUES (2, 7);
INSERT INTO Marco
VALUES (2, 8);
INSERT INTO Marco
VALUES (2, 9);
INSERT INTO Marco
VALUES (3, 10);
INSERT INTO Marco
VALUES (3, 11);
INSERT INTO Marco
VALUES (3, 12);
INSERT INTO Marco
VALUES (4, 13);
INSERT INTO Marco
VALUES (4, 14);
INSERT INTO Marco
VALUES (5, 15);
INSERT INTO Marco
VALUES (5, 16);
INSERT INTO Marco
VALUES (5, 17);


INSERT INTO Concesionarios
VALUES (1, "acar", "madrid");
INSERT INTO Concesionarios
VALUES (2, "bcar", "madrid");
INSERT INTO Concesionarios
VALUES (3, "ccar", "Barcelona");
INSERT INTO Concesionarios
VALUES (4, "dcar", "Valencia");
INSERT INTO Concesionarios
VALUES (5, "ecar", "Bilbao");


INSERT INTO Distribucion
VALUES (1, 1, 3);
INSERT INTO Distribucion
VALUES (1, 2, 7);
INSERT INTO Distribucion
VALUES (1, 3, 7);
INSERT INTO Distribucion
VALUES (2, 6, 5);
INSERT INTO Distribucion
VALUES (2, 7, 10);
INSERT INTO Distribucion
VALUES (2, 8, 10);
INSERT INTO Distribucion
VALUES (3, 10, 5);
INSERT INTO Distribucion
VALUES (3, 11, 3);
INSERT INTO Distribucion
VALUES (3, 12, 5);
INSERT INTO Distribucion
VALUES (4, 13, 10);
INSERT INTO Distribucion
VALUES (4, 14, 5);

INSERT INTO Clientes
VALUES (1, "Luis", "Garcia", "Madrid");
INSERT INTO Clientes
VALUES (2, "Antonio", "Lopez", "Valencia");
INSERT INTO Clientes
VALUES (3, "Juan", "Martin", "Madrid");
INSERT INTO Clientes
VALUES (4, "Maria", "Garcia", "Madrid");
INSERT INTO Clientes
VALUES (5, "Javier", "Gonzalez", "Barcelona");
INSERT INTO Clientes
VALUES (6, "Ana", "Lopez", "Barcelona");
INSERT INTO Clientes
VALUES (7, "Ana", "Lopez", "Madrid");
INSERT INTO Clientes
VALUES (8, "Ana", "Lopez", "Barcelona");


INSERT INTO Ventas
VALUES (1, 1, 1, "blanco");
INSERT INTO Ventas
VALUES (1, 2, 5, "rojo");
INSERT INTO Ventas
VALUES (2, 3, 8, "blanco");
INSERT INTO Ventas
VALUES (2, 1, 6, "rojo");
INSERT INTO Ventas
VALUES (3, 4, 11, "rojo");
INSERT INTO Ventas
VALUES (4, 5, 14, "verde");
INSERT INTO Ventas
VALUES (4, 5, 13, "rojo");
INSERT INTO Ventas
VALUES (4, 4, 14, "verde");