CREATE TABLE workers(
w_id text PRIMARY KEY,
w_name text,
w_age int,
w_salary real,
w_city text
);

INSERT INTO workers (w_id,w_name,w_age,w_salary,w_city)
VALUES
('W001','Alice',28,50000,'New York'),
('W002','Bob',34,60000,'Los Angeles'),
('W003','Charlie',25,55000,'Chicago'),
('W004','Diana',30,70000,'New York'),
('W005','Ethan',40,80000,'Phoenix'),
('W006','Fiona',29,65000,'New York');

SELECT * FROM workers;

SELECT * FROM workers WHERE w_city = 'New York' AND w_salary >= 60000;

SELECT * FROM workers WHERE w_city = 'New York' OR w_salary >= 60000;