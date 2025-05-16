mysql -u root -p
CREATE DATABASE parainnage;
USE parainnage;
CREATE TABLE parains (
    numero_tel INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    departement VARCHAR(100),
    mot_de_passe VARCHAR(100)
);

CREATE TABLE filleuls (
    numero_tel INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    departement VARCHAR(100),
    mot_de_passe VARCHAR(100)
);

