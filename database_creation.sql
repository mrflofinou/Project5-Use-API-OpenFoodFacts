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
  id BIGINT UNSIGNED AUTO_INCREMENT,
  id_category INT UNSIGNED,
  name VARCHAR(150) NOT NULL,
  magasin VARCHAR(100),
  nutriscore VARCHAR(10),
  url VARCHAR(200),
  PRIMARY KEY(id),
  CONSTRAINT fk_id_category
    FOREIGN KEY (id_category)
    REFERENCES categories (id)
)
ENGINE=INNODB;

CREATE TABLE substitutes (
  id INT UNSIGNED AUTO_INCREMENT,
  id_substitute BIGINT UNSIGNED,
  id_product_substituted BIGINT UNSIGNED,
  nom VARCHAR(150) NOT NULL,
  magasin VARCHAR(100),
  url VARCHAR(200),
  PRIMARY KEY(id)
)
ENGINE=INNODB;
