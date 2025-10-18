CREATE TABLE workers(
id text PRIMARY KEY,
name text,
age int,
salary real
);

INSERT INTO workers (id,name,age,salary)
VALUES ('W001','Alisa',25,3000),('W002','Brian',30,4500),('W003','Cathy',28,4000);

SELECT * FROM workers;

SELECT name,salary FROM workers WHERE salary > 3500;