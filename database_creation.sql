-- Création des tables

CREATE TABLE Categorie_sql (
  id INT UNSIGNED AUTO_INCREMENT,
  nom VARCHAR(150) NOT NULL,
  description TEXT,
  PRIMARY KEY(id),
  FULLTEXT ind_nom_categorie (nom)
)
ENGINE=INNODB;
