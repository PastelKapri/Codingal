CREATE TABLE yummers(
name text,
neighborhood text,
cuisine text,
rating real,
price real
);

INSERT INTO yummers (name,neighborhood,cuisine,rating,price)
VALUES
('Pasta Palace','Downtown','Italian',4.5,25.00),
('Sushi Central','Uptown','Japanese',4.8,40.00),
('Curry Corner','Midtown','Indian',4.2,15.00),
('Burger Barn','Suburbs','American',4.0,10.00),
('Taco Town','Downtown','Mexico',4.7,20.00);

SELECT * FROM yummers;

SELECT DISTINCT neighborhood FROM yummers;

SELECT DISTINCT cuisine FROM yummers;

SELECT * FROM yummers WHERE cuisine = 'Italian';
SELECT * FROM yummers WHERE rating >= 4.5;
SELECT * FROM yummers WHERE neighborhood = 'Downtown' AND price <= 20.00;

SELECT * FROM yummers WHERE neighborhood = 'Downtown' OR price <= 20.00;

SELECT * FROM yummers ORDER BY rating DESC;

SELECT * FROM yummers WHERE name LIKE '%C%';
SELECT * FROM yummers WHERE neighborhood in('Downtown','Uptown');       