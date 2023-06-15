-- Création de la table Étudiants
CREATE TABLE Etudiants (
    numero_etudiant INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    groupe TEXT,
    photo BLOB,
    email TEXT
);

-- Création de la table Unités d'enseignement
CREATE TABLE Unites_enseignement (
    code TEXT PRIMARY KEY,
    nom TEXT,
    semestre INTEGER,
    credit_ects INTEGER
);

-- Création de la table Ressources associées à une UE
CREATE TABLE Ressources_UE (
    code_ressource TEXT PRIMARY KEY,
    nom TEXT,
    descriptif TEXT,
    coefficient INTEGER
);

-- Création de la table Enseignants
CREATE TABLE Enseignants (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT
);

-- Création de la table Examens
CREATE TABLE Examens (
    id INTEGER PRIMARY KEY,
    titre TEXT,
    date TEXT,
    coefficient INTEGER
);

-- Création de la table Notes
CREATE TABLE Notes (
    examen INTEGER,
    etudiant INTEGER,
    note REAL,
    appreciation TEXT,
    FOREIGN KEY (examen) REFERENCES Examens(id),
    FOREIGN KEY (etudiant) REFERENCES Etudiants(numero_etudiant)
);

