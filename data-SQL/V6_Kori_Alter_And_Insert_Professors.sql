ALTER TABLE professors ADD COLUMN name VARCHAR(100);

UPDATE professors SET name = 'Ana Souza'
WHERE username = 'ana.mat';

UPDATE professors SET name = 'Carlos Lima'
WHERE username = 'carlos.port';

UPDATE professors SET name = 'Juliana Rocha'
WHERE username = 'juliana.hist';

UPDATE professors SET name = 'Marcos Pereira'
WHERE username = 'marcos.cien';

UPDATE professors SET name = 'Diogo Nascimento'
WHERE username = 'diogo.info';