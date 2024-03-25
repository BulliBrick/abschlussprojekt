CREATE DATABASE IF NOT EXISTS abschlussprojekt;

use abschlussprojekt;

CREATE TABLE members (
    id INT AUTO_INCREMENT,
    nachname VARCHAR(50),
    vorname VARCHAR(50),
    spitzname VARCHAR(50),
    age INT,
    PRIMARY KEY (id)
);


INSERT INTO members (vorname, nachname, spitzname, age) VALUES 
('Amsler', 'Simon', 'amsi', 17), 
('Schmutz', 'Seth', 'schmutzly', 17), 
('Topp', 'Tobias', 'tobi', 16), 
('Seeli', 'Markus', 'markus', 35), 
('Akkaya', 'Cem', 'cemmy', 18),
('Kunz', 'Joshua', 'josh', 17);
