CREATE  database customer;
use customer;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);

INSERT INTO customers VALUES
(1, 'Aman', 'Delhi'),
(2, 'Riya', 'Mumbai'),
(3, 'Kabir', 'Delhi'),
(4, 'Neha', 'Pune'),
(5, 'Arjun', 'Bangalore'),
(6, 'Simran', 'Mumbai'),
(7, 'Rahul', 'Delhi'),
(8, 'Pooja', 'Chennai'),
(9, 'Vikas', 'Pune'),
(10, 'Anita', 'Bangalore');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 60000),
(102, 1, 'Mouse', 1500),
(103, 2, 'Mobile', 30000),
(104, 3, 'Keyboard', 2500),
(105, 3, 'Monitor', 12000),
(106, 5, 'Tablet', 20000),
(107, 6, 'Laptop', 65000),
(108, 7, 'Mobile', 28000),
(109, 7, 'Earphones', 2000),
(110, 11, 'Camera', 40000);

// #Q.1 Show customer_name,product and amount
select c.customer_name,o.product,o.amount from customers c join orders o on c.customer_id=o.customer_id;
// +---------------+-----------+--------+
// | customer_name | product   | amount |
// +---------------+-----------+--------+
// | Aman          | Laptop    |  60000 |
// | Aman          | Mouse     |   1500 |
// | Riya          | Mobile    |  30000 |
// | Kabir         | Keyboard  |   2500 |
// | Kabir         | Monitor   |  12000 |
// | Arjun         | Tablet    |  20000 |
// | Simran        | Laptop    |  65000 |
// | Rahul         | Mobile    |  28000 |
// | Rahul         | Earphones |   2000 |
// +---------------+-----------+--------+

// Q.2Show customer_name,product and order_id
select c.customer_name,o.product,o.order_id from customers c join orders o on c.customer_id=o.customer_id;
// +---------------+-----------+----------+
// | customer_name | product   | order_id |
// +---------------+-----------+----------+
// | Aman          | Laptop    |      101 |
// | Aman          | Mouse     |      102 |
// | Riya          | Mobile    |      103 |
// | Kabir         | Keyboard  |      104 |
// | Kabir         | Monitor   |      105 |
// | Arjun         | Tablet    |      106 |
// | Simran        | Laptop    |      107 |
// | Rahul         | Mobile    |      108 |
// | Rahul         | Earphones |      109 |
// +---------------+-----------+----------+


// #Q.3 Show customers from delhi who placed orders
select c.customer_name,o.product from customers c join orders o on c.customer_id=o.customer_id where city="delhi";
// +---------------+-----------+
// | customer_name | product   |
// +---------------+-----------+
// | Aman          | Laptop    |
// | Aman          | Mouse     |
// | Kabir         | Keyboard  |
// | Kabir         | Monitor   |
// | Rahul         | Mobile    |
// | Rahul         | Earphones |
// +---------------+-----------+

// #Q.4 show all customers even they have no orders
select c.customer_name,o.product from customers c left join orders o on c.customer_id=o.customer_id;
// +---------------+-----------+
// | customer_name | product   |
// +---------------+-----------+
// | Aman          | Mouse     |
// | Aman          | Laptop    |
// | Riya          | Mobile    |
// | Kabir         | Monitor   |
// | Kabir         | Keyboard  |
// | Neha          | NULL      |
// | Arjun         | Tablet    |
// | Simran        | Laptop    |
// | Rahul         | Earphones |
// | Rahul         | Mobile    |
// | Pooja         | NULL      |
// | Vikas         | NULL      |
// | Anita         | NULL      |
// +---------------+-----------+

// Q.5 show all orders even customer doess not exist
SELECT *FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id;
// +----------+-------------+-----------+--------+-------------+---------------+-----------+
// | order_id | customer_id | product   | amount | customer_id | customer_name | city      |
// +----------+-------------+-----------+--------+-------------+---------------+-----------+
// |      101 |           1 | Laptop    |  60000 |           1 | Aman          | Delhi     |
// |      102 |           1 | Mouse     |   1500 |           1 | Aman          | Delhi     |
// |      103 |           2 | Mobile    |  30000 |           2 | Riya          | Mumbai    |
// |      104 |           3 | Keyboard  |   2500 |           3 | Kabir         | Delhi     |
// |      105 |           3 | Monitor   |  12000 |           3 | Kabir         | Delhi     |
// |      106 |           5 | Tablet    |  20000 |           5 | Arjun         | Bangalore |
// |      107 |           6 | Laptop    |  65000 |           6 | Simran        | Mumbai    |
// |      108 |           7 | Mobile    |  28000 |           7 | Rahul         | Delhi     |
// |      109 |           7 | Earphones |   2000 |           7 | Rahul         | Delhi     |
// |      110 |          11 | Camera    |  40000 |        NULL | NULL          | NULL      |
// +----------+-------------+-----------+--------+-------------+---------------+-----------+

// #Q.6Final orders with no matching customers
SELECT *  FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id WHERE c.customer_id IS NULL;
// +----------+-------------+---------+--------+-------------+---------------+------+
// | order_id | customer_id | product | amount | customer_id | customer_name | city |
// +----------+-------------+---------+--------+-------------+---------------+------+
// |      110 |          11 | Camera  |  40000 |        NULL | NULL          | NULL |
// +----------+-------------+---------+--------+-------------+---------------+------+

// #Q.7Show all customers and all orders
SELECT * FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT * FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;
// +-------------+---------------+-----------+----------+-------------+-----------+--------+
// | customer_id | customer_name | city      | order_id | customer_id | product   | amount |
// +-------------+---------------+-----------+----------+-------------+-----------+--------+
// |           1 | Aman          | Delhi     |      102 |           1 | Mouse     |   1500 |
// |           1 | Aman          | Delhi     |      101 |           1 | Laptop    |  60000 |
// |           2 | Riya          | Mumbai    |      103 |           2 | Mobile    |  30000 |
// |           3 | Kabir         | Delhi     |      105 |           3 | Monitor   |  12000 |
// |           3 | Kabir         | Delhi     |      104 |           3 | Keyboard  |   2500 |
// |           4 | Neha          | Pune      |     NULL |        NULL | NULL      |   NULL |
// |           5 | Arjun         | Bangalore |      106 |           5 | Tablet    |  20000 |
// |           6 | Simran        | Mumbai    |      107 |           6 | Laptop    |  65000 |
// |           7 | Rahul         | Delhi     |      109 |           7 | Earphones |   2000 |
// |           7 | Rahul         | Delhi     |      108 |           7 | Mobile    |  28000 |
// |           8 | Pooja         | Chennai   |     NULL |        NULL | NULL      |   NULL |
// |           9 | Vikas         | Pune      |     NULL |        NULL | NULL      |   NULL |
// |          10 | Anita         | Bangalore |     NULL |        NULL | NULL      |   NULL |
// |        NULL | NULL          | NULL      |      110 |          11 | Camera    |  40000 |
// +-------------+---------------+-----------+----------+-------------+-----------+--------+

// #Q.7Find customers who have placed atleast one order
select customer_name from customers where customer_id IN (select customer_id from orders);
// +---------------+
// | customer_name |
// +---------------+
// | Aman          |
// | Riya          |
// | Kabir         |
// | Arjun         |
// | Simran        |
// | Rahul         |
// +---------------+

// #Q.8Find customers who have not place any order
select customer_name from customers where customer_id NOT IN (select customer_id from orders);
// +---------------+
// | customer_name |
// +---------------+
// | Neha          |
// | Pooja         |
// | Vikas         |
// | Anita         |
// +---------------+

// #Q.9Find customers who have place an order with amount greater than the avg of amount
select customer_name from customers where customer_id IN(select customer_id from orders where amount>(select avg(amount) from orders));
// +---------------+
// | customer_name |
// +---------------+
// | Aman          |
// | Riya          |
// | Simran        |
// | Rahul         |
// +---------------



