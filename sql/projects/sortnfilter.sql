CREATE TABLE tickets(
ticket_id text PRIMARY KEY,
ticket_type text,
ticket_depot text,
price real,
sales real
);

INSERT INTO tickets(ticket_id,ticket_type,ticket_depot,price,sales)
VALUES
('0001','Concert','D001',60,90),
('0002','Plane','D002',5500,800),
('0003','Speeding','D001',20,860),
('0004','Plane','D003',500,900),
('0005','Concert','D002',6500,1234);

SELECT * FROM tickets;

SELECT ticket_depot as 'Department Code', COUNT(*) as 'No. of tickets'
FROM tickets
GROUP BY ticket_depot;

SELECT ticket_depot, SUM(price) as 'Total Revenue'
FROM tickets
GROUP BY ticket_depot;

SELECT ticket_depot as 'Department Code', COUNT(*) as 'No. of tickets',
SUM(price) as 'Total Revenue'
FROM tickets
GROUP BY ticket_depot;

SELECT ticket_depot, SUM(price)
FROM tickets
GROUP BY ticket_depot
ORDER BY SUM(price) DESC;
