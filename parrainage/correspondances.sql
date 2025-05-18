-- Étape 1 : dire à MySQL qu'on travaille dans la base parainnage
USE parainnage;

-- Étape 2 : créer la table correspondances
CREATE TABLE correspondances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parrain_tel INT,
    filleul_tel INT,
    FOREIGN KEY (parrain_tel) REFERENCES parains(numero_tel),
    FOREIGN KEY (filleul_tel) REFERENCES filleuls(numero_tel)
);
-- #pour vider une table
-- TRUNCATE TABLE correspondances;

