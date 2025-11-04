CREATE TABLE products(
p_id text PRIMARY KEY,
p_name text,
p_category text,
p_price real,
p_supplier text
);

INSERT INTO products (p_id,p_name,p_category,p_price,p_supplier)
VALUES
('P001','N plushie','Toys',15.99,'ToyCo'),
('P002','Uzi shirt','Clothes',199.99,'FashionHub'),
('P003','Cyn keychain','Accesories',89.99,'ChainGain'),
('P004','V Smart Watch','Electronics',149.99,'GadgetWorld'),
('P005','MD Action Figure','Toys',25.99,'ToyCo'),
('P006','Cyn shirt','Furniture',129.99,'FashionHub');

SELECT COUNT(p_id) AS 'Total Products' FROM products;
SELECT AVG(p_price) AS 'Average Price' FROM products;
SELECT SUM(p_price) AS 'Total Price' FROM products;
SELECT DISTINCT(p_supplier) AS 'Unique Supplier' FROM products;