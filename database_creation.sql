-- Création des tables

CREATE TABLE Categorie (
  id INT UNSIGNED AUTO_INCREMENT,
  nom_categorie VARCHAR(150) NOT NULL,
  description TEXT,
  PRIMARY KEY(id)
)
;
