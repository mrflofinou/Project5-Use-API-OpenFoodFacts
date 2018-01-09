-- Création de la base de donnée

CREATE DATABASE openfoodfacts CHARACTER SET 'utf8';

-- Création des tables

CREATE TABLE categories (
  id INT UNSIGNED AUTO_INCREMENT,
  nom VARCHAR(150) NOT NULL,
  PRIMARY KEY(id)
)
ENGINE=INNODB;

CREATE TABLE products (
  id INT UNSIGNED AUTO_INCREMENT,
  name VARCHAR(150) NOT NULL,
  id_category INT UNSIGNED,
  PRIMARY KEY(id),
  CONSTRAINT fk_id_category
    FOREIGN KEY (id_category)
    REFERENCES categories (id)
)
ENGINE=INNODB;
