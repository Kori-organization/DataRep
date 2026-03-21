-- ============================================
-- DATA LOAD SCRIPT
-- ============================================

-- SUBJECTS (5 insertions)
INSERT INTO subjects (name) VALUES
('Matemática'),
('Português'),
('História'),
('Ciências'),
('Informática');

-- ADMINISTRATORS (5 insertions)
INSERT INTO administrators (username, password_hash) VALUES
('Davi', 	 'PdQf53796'),
('Felipe',   'nAGv51932'),
('Gabriela', 'EnQV84581'),
('Igor',     'bRDa06415'),
('Lucas',    'bkaM61067'),
('MEduarda', 'QjaF29358'),
('Diogo',    'gjLd10397');

-- PROFESSORS (5 insertions)
INSERT INTO professors (username, password_hash, subject_id) VALUES
('ana.mat', 	 '123456', (select id from subjects where name = 'Matemática')),
('carlos.port',  '123456', (select id from subjects where name = 'Português')),
('juliana.hist', '123456', (select id from subjects where name = 'História')),
('marcos.cien',  '123456', (select id from subjects where name = 'Ciências')),
('diogo.info', 	 '123456', (select id from subjects where name = 'Informática'));

-- STUDENTS (10 insertions for variety)
INSERT INTO students (email, password, name, serie) VALUES
('joao.silva@korieducation.com', 		'student123', 	'João Silva', 		1),
('maria.santos@korieducation.com', 	    'student456', 	'Maria Santos', 	4),
('pedro.oliveira@korieducation.com', 	'student789', 	'Pedro Oliveira', 	3),
('ana.costa@korieducation.com', 		'student012', 	'Ana Costa', 		3),
('lucas.ferreira@korieducation.com', 	'student345', 	'Lucas Ferreira', 	1),
('julia.almeida@korieducation.com', 	'student678', 	'Júlia Almeida',    2),
('carlos.rodrigues@korieducation.com',  'student901', 	'Carlos Rodrigues', 5),
('beatriz.lima@korieducation.com', 	    'student234', 	'Beatriz Lima', 	4),
('rafael.martins@korieducation.com', 	'student567', 	'Rafael Martins', 	5),
('gabriela.souza@korieducation.com',	'student890', 	'Gabriela Souza', 	1);

-- GRADES (15 insertions - 3 per subject)
INSERT INTO grades (grade1, grade2, rec, subject_id) VALUES
-- Matemática 
(8.5, 7.0, NULL, (select id from subjects where name = 'Matemática')), 
(6.0, 5.5, 7.0,  (select id from subjects where name = 'Matemática')), 
(9.0, 8.5, NULL, (select id from subjects where name = 'Matemática')), 
-- Português 
(7.5, 8.0, NULL, (select id from subjects where name = 'Português')), 
(5.0, 6.0, 6.5,  (select id from subjects where name = 'Português')), 
(8.0, 7.5, NULL, (select id from subjects where name = 'Português')), 
-- História 
(7.0, 6.5, NULL, (select id from subjects where name = 'História')), 
(4.5, 5.0, 6.0,  (select id from subjects where name = 'História')),
(8.5, 9.0, NULL, (select id from subjects where name = 'História')),
-- Ciências 
(6.5, 7.0, NULL, (select id from subjects where name = 'Ciências')), 
(5.5, 6.0, 7.5,  (select id from subjects where name = 'Ciências')), 
(9.5, 9.0, NULL, (select id from subjects where name = 'Ciências')), 
-- Informática 
(8.0, 8.5, NULL, (select id from subjects where name = 'Informática')), 
(6.0, 6.5, NULL, (select id from subjects where name = 'Informática')), 
(7.5, 7.0, NULL, (select id from subjects where name = 'Informática')); 

-- REPORT_CARD (9 insertions - matching grades)
INSERT INTO report_card (final_situation, student_id) VALUES
('Em Andamento', (select enrollment from students where name = 'João Silva')),   
('Em Andamento',(select enrollment from students where name = 'Maria Santos')),  
('Em Andamento',(select enrollment from students where name = 'Pedro Oliveira')),   
('Em Andamento',(select enrollment from students where name = 'Ana Costa')),   
('Em Andamento',(select enrollment from students where name = 'Lucas Ferreira')),   
('Em Andamento',(select enrollment from students where name = 'Júlia Almeida')),   
('Em Andamento',(select enrollment from students where name = 'Carlos Rodrigues')),  
('Em Andamento',(select enrollment from students where name = 'Beatriz Lima')),   
('Em Andamento',(select enrollment from students where name = 'Rafael Martins'));

-- GRADE_REP (15 insertions - linking report cards to grades)
INSERT INTO grade_rep (rep_id, grade_id) VALUES
(1, 1),   
(1, 4),   
(1, 7),   
(2, 2),   
(2, 5),   
(2, 13),     
(3, 15),  
(3, 12),  
(4, 11),  
(4, 4),    
(5, 14),  
(6, 10),   
(7, 6),   
(8, 8), 
(9, 9); 

-- OBSERVATIONS (8 insertions)
INSERT INTO observations (observation, student_id) VALUES
('Excelente participação em aula. Mostra fortes habilidades analíticas.',              (select enrollment from students where name = 'João Silva')),
('Precisa melhorar a finalização de lição de casas. Considerar uma tutoria extra.',    (select enrollment from students where name = 'Maria Santos')),
('Estudante muito dedicado. Sempre pontual e engajado.',                               (select enrollment from students where name = 'Pedro Oliveira')),
('Tem problemas com concentração. Recomendo reunião com os pais.',                     (select enrollment from students where name = 'Ana Costa')),
('Performance extraordinária em projetos em grupo',                                    (select enrollment from students where name = 'Lucas Ferreira')),
('Melhoria significante percebida no último semestre. Continue com o bom trabalho!',   (select enrollment from students where name = 'Júlia Almeida')),
('Falta frequentemente. Performance acadêmica está sendo afetada.',                    (select enrollment from students where name = 'Carlos Rodrigues')),
('Grande potencial em pensamentos criaticvos. Incentivar cursos para melhorar.',       (select enrollment from students where name = 'Beatriz Lima'));