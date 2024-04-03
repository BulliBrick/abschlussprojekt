
-- Erstellt die Datenbank abschlussarbeit, falls sie noch nicht existiert
CREATE DATABASE IF NOT EXISTS abschlussarbeit;

-- Wechselt in die Datenbank abschlussarbeit
USE abschlussarbeit;

-- Erstellt die Tabelle members, falls sie noch nicht existiert
CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT,
    nachname VARCHAR(50),
    vorname VARCHAR(50),
    spitzname VARCHAR(50),
    age INT,
    PRIMARY KEY (id)
);

-- Fügt Sample-Daten in die Tabelle members ein
INSERT INTO members (nachname, vorname, spitzname, age) VALUES 
('Amsler', 'Simon', 'amsi', 17), 
('Schmutz', 'Seth', 'schmutzly', 17), 
('Topp', 'Tobias', 'tobi', 16), 
('Seeli', 'Markus', 'markus', 35), 
('Akkaya', 'Cem', 'cemmy', 18),
('Kunz', 'Joshua', 'josh', 17);

-- hier können SQL Statemets hinzugefügt werden. Diese werden beim kreieren ausgeführt und bestimmen so den Anfangszustand der Datenbank.COMMENT
