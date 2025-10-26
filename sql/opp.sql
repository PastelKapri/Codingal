CREATE TABLE IF NOT EXISTS students(
s_id text PRIMARY KEY,
s_name text,
s_age int,
s_grade real
);

INSERT INTO students (s_id,s_name,s_age,s_grade)
VALUES
('0001','Jax',20,40),
('0002','Pomni',19,80),
('0003','Ragetha',21,90),
('0004','Gangle',17,80),
('0005','Zooble',22,80),
('0006','Kinger',30,90);

SELECT * FROM students;

SELECT * FROM students WHERE s_age >= 20 AND s_grade >= 80;

SELECT MIN(s_age) AS Youngest_Student FROM students;

SELECT MAX(s_age) AS Oldest_Student FROM students;

SELECT * FROM students WHERE s_age >=25 or s_grade <80;

SELECT * FROM students WHERE s_name LIKE 'R%';

UPDATE students SET s_grade = 100 WHERE s_id = '0001';

SELECT * FROM students;

DELETE FROM students WHERE s_id = '0001';

SELECT * FROM students;
