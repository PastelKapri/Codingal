CREATE TABLE salesman(
s_id text PRIMARY KEY,
s_name text,
s_city text,
s_comission real
);

INSERT INTO salesman (s_id,s_name,s_city,s_comission)
VALUES
('S001','John Doe','New York',0.11),
('S002','Robert Smith','Los Angeles',0.13),
('S003','Alex Johnson','Chicago',0.12),
('S005','Michael Brown','Phoenix',0.16);

CREATE TABLE costomers(
c_id text PRIMARY KEY,
c_name text,
c_city text,
s_id text,
FOREIGN KEY(s_id) REFERENCES salesman(s_id)
);

INSERT INTO costomers (c_id,c_name,c_city,s_id)
VALUES
('C001','Alice','New York','S001'),
('C002','Bob','Los Angeles','S002'),
('C003','Charlie','Chicago','S003'),
('C004','David','Houston','S005'),
('C005','Eva','Phoenix','S001');

CREATE TABLE orders(
o_id text PRIMARY KEY,
o_date date,
o_amount real,
pur_amt real,
s_id text,
c_id text,
FOREIGN KEY(c_id) REFERENCES costomers(c_id),
FOREIGN KEY(s_id) REFERENCES salesman(s_id)
);

INSERT INTO orders (o_id,o_date,o_amount,pur_amt,c_id,s_id)
VALUES
('O001','2023-01-15',150.00,120.00,'C001','S001'),
('O002','2023-02-20',200.00,130.00,'C002','S002'),
('O003','2023-03-10',300.00,200.00,'C003','S003'),
('O004','2023-04-05',250.00,160.00,'C004','S005'),
('O005','2023-05-25',400.00,370.00,'C005','S001');

SELECT costomers.c_name, salesman.s_name, salesman.s_city
FROM costomers
JOIN salesman ON costomers.c_city = salesman.s_city;

SELECT costomers.c_name, salesman.s_name
FROM costomers
JOIN salesman ON costomers.s_id = salesman.s_id;

SELECT orders.o_id, costomers.c_name, orders.c_id, orders.s_id
FROM orders
JOIN costomers ON orders.c_id = costomers.c_id
JOIN salesman ON orders.s_id = salesman.s_id
WHERE costomers.c_city <> salesman.s_city;

SELECT orders.o_id, costomers.c_name
FROM orders
JOIN costomers ON orders.c_id = costomers.c_id;

SELECT costomers.c_name AS 'costomers', costomers.grade AS 'Grade'
FROM orders
JOIN salesman ON orders.s_id = salesman.s_id
JOIN costomers ON orders.c_id = costomers.c_id
WHERE costomers.grade IS NOT NULL;

SELECT costomers.c_name AS 'costomers'
costomers.c_city AS 'city'
salesman.s_name AS 'salesman'
salesman.comission
FROM costomers
JOIN salesman ON costomers.s_id = salesman.s_id
WHERE salesman.comission BETWEEN 0.12 AND 0.14;

SELECT orders.o_id, costomers.c_name, salesman.comission AS 'comission%'
orders.pur_amt * salesman.comission AS 'comission'
FROM orders
JOIN salesman ON orders.s_id = salesman.s_id
JOIN costomers ON orders.c_id = costomers.c_id
WHERE costomers.grade >= 200;

