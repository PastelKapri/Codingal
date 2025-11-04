CREATE TABLE workers(
w_id text PRIMARY KEY,
w_name text,
w_department text,
w_salary real
);

INSERT INTO workers (w_id,w_name,w_department,w_salary)
VALUES
('w001','Nina','Toys',15000),
('w002','Uzara','Clothes',20000),
('w003','Cyn','Accesories',800),
('w004','Veronica','Electronics',30000),
('w005','Mel','Toys',11000),
('w006','Cider','Furniture',12000);

SELECT DISTINCT(w_department) AS 'Total Departments' FROM workers;
SELECT AVG(w_salary) AS 'Average Salary' FROM workers;
SELECT SUM(w_salary) AS 'Total Salary' FROM workers;
SELECT MAX(w_salary) AS 'Maximum Salary' FROM workers;
SELECT MIN(w_salary) AS 'Minimum Salary' FROM workers;