CREATE TABLE departments(
employee_id text PRIMARY KEY,
name text,
department_id text,
manager_id text,
salary real
);

INSERT INTO departments (employee_id,name,department_id,manager_id,salary)
VALUES
('E001','Alice','D001','M001',60000),
('E002','Bob','D002','M002',55000),
('E003','Charlie','D001','M001',70000),
('E004','David','D003','M003',50000),
('E005','Eva','D002','M002',65000);

SELECT * FROM departments;

SELECT department_id as 'Department Code', COUNT(*) as 'Number of Employees'
FROM departments
GROUP BY department_id;

SELECT department_id, SUM(salary) as 'Total Salary'
FROM departments
GROUP BY department_id;

SELECT department_id as 'Department Code', COUNT(*) as 'Number of Employees',
SUM(salary) as 'Total Salary'
FROM departments
GROUP BY department_id;

SELECT department_id, SUM(salary)
FROM departments
GROUP BY department_id
ORDER BY SUM(salary) DESC;

