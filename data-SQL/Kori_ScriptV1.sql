-- Set timezone
SET TIME ZONE 'America/Sao_Paulo';

-- SUBJECT
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- ADMINISTRATORS
CREATE TABLE administrators (
    id SERIAL PRIMARY KEY,
    username VARCHAR(40) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

-- PROFESSORS
CREATE TABLE professors (
    id SERIAL PRIMARY KEY,
    username VARCHAR(40) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    CONSTRAINT fk_professor_subject
        FOREIGN KEY (subject_id)
        REFERENCES subjects(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- GRADES
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    grade1 DECIMAL(10,2) NOT NULL CHECK (grade1 BETWEEN 0 AND 10),
    grade2 DECIMAL(10,2) NOT NULL CHECK (grade2 BETWEEN 0 AND 10),
    rec DECIMAL(10,2) NOT NULL CHECK (rec BETWEEN 0 AND 10),
    subject_id INTEGER NOT NULL,
    CONSTRAINT fk_grades_subject
        FOREIGN KEY (subject_id)
        REFERENCES subjects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
