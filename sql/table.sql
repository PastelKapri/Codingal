CREATE TABLE students(
s_id int PRIMARY KEY,
s_name text,
s_age int,
ave_grade real
);

INSERT INTO students (s_id,s_name,s_age,ave_grade)
VALUES (001, 'Jess', 12, 78.5),(002, 'Mark', 13, 85.0),(003, 'Lily', 12, 92.3);

SELECT * FROM students;

SELECT s_name,ave_grade FROM students WHERE ave_grade > 80.0;

SELECT * FROM students WHERE s_age = 12;

DROP TABLE students;

SELECT * FROM students;