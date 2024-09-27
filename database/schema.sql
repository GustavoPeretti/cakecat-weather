CREATE SCHEMA cakecat_weather;

USE cakecat_weather;

CREATE TABLE administradores (
	usuario VARCHAR(30) PRIMARY KEY,
    senha BINARY(32) NOT NULL
);

CREATE TABLE cidades (
	cep CHAR(8) PRIMARY KEY,
    cidade VARCHAR(60) NOT NULL,
    estado VARCHAR(30) NOT NULL
);

CREATE TABLE tempo (
	cep CHAR(8),
    data_tempo DATE,
    administrador VARCHAR(30),
    condicao VARCHAR(30) NOT NULL,
    maxima FLOAT NOT NULL,
    minima FLOAT NOT NULL,
    chuva FLOAT NOT NULL,
    vento FLOAT NOT NULL,
    umidade FLOAT NOT NULL,
    arco_iris VARCHAR(30) NOT NULL,
    inicio_sol TIME NOT NULL,
    fim_sol TIME NOT NULL,
    lua VARCHAR(30) NOT NULL,
    PRIMARY KEY (cep, data_tempo),
    FOREIGN KEY (cep) REFERENCES cidades (cep) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (administrador) REFERENCES administradores (usuario) ON UPDATE CASCADE ON DELETE CASCADE
);
