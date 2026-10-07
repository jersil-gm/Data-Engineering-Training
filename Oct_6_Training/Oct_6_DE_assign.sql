-- Practice Set 1 — Basics + CRUD + Filtering 
-- Scenario: Restaurant Menu

CREATE DATABASE restaurant_menu_db;
USE restaurant_menu_db;

CREATE TABLE menu_items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    available_qty INT
);

INSERT INTO menu_items VALUES
(1, 'Chicken Biryani', 'Main Course', 320, 25),
(2, 'Paneer Tikka', 'Starter', 240, 15),
(3, 'Masala Dosa', 'Breakfast', 120, 30),
(4, 'Veg Burger', 'Fast Food', 180, 10),
(5, 'Cold Coffee', 'Beverage', 150, 20),
(6, 'Chicken Burger', 'Fast Food', 220, 8),
(7, 'Idli', 'Breakfast', 80, 40),
(8, 'Fresh Lime', 'Beverage', 90, 0);

--  1
SELECT * FROM menu_items;

-- 2
SELECT item_name, price FROM menu_items;

-- 3
INSERT INTO menu_items VALUES (9, 'Gulab Jamun', 'Dessert', 100, 20);

-- 4
UPDATE menu_items SET price = 350 WHERE item_name = 'Chicken Biryani';

-- 5
UPDATE menu_items SET price = price + price * 0.10 WHERE category = 'Fast Food';

-- 6
UPDATE menu_items SET available_qty = available_qty - 2 WHERE item_name = 'Veg Burger';

-- 7
DELETE FROM menu_items WHERE available_qty = 0;

-- 8
SELECT * FROM menu_items WHERE price > 200;

-- 9
SELECT * FROM menu_items WHERE price BETWEEN 100 AND 250;

-- 10
SELECT * FROM menu_items WHERE category = 'Breakfast';

-- 11
SELECT * FROM menu_items WHERE category = 'Breakfast' OR category = 'Beverage';

-- 12
SELECT * FROM menu_items WHERE item_name LIKE '%Chicken%';

-- 13
SELECT * FROM menu_items ORDER BY price DESC;

-- 14
SELECT * FROM menu_items ORDER BY price DESC LIMIT 3;

--  15
SELECT * FROM menu_items WHERE available_qty < 15;

-- Practice Set 2 — Aggregate Functions + GROUP BY + HAVING
-- Scenario: Food Delivery Orders

CREATE DATABASE food_delivery_db;
USE food_delivery_db;

CREATE TABLE food_orders (
    order_id INT PRIMARY KEY,
    restaurant VARCHAR(100),
    city VARCHAR(50),
    food_type VARCHAR(50),
    order_amount DECIMAL(10,2),
    delivery_partner VARCHAR(50),
    order_date DATE
);

INSERT INTO food_orders VALUES
(101, 'Spice Hub', 'Hyderabad', 'Indian', 850, 'Ravi', '2026-09-01'),
(102, 'Burger Zone', 'Hyderabad', 'Fast Food', 520, 'Kiran', '2026-09-01'),
(103, 'Pizza Point', 'Mumbai', 'Fast Food', 1100, 'Ravi', '2026-09-02'),
(104, 'Curry House', 'Bangalore', 'Indian', 760, 'Aman', '2026-09-02'),
(105, 'Spice Hub', 'Hyderabad', 'Indian', 1250, 'Kiran', '2026-09-03'),
(106, 'Sushi World', 'Mumbai', 'Japanese', 1800, 'Aman', '2026-09-03'),
(107, 'Pizza Point', 'Mumbai', 'Fast Food', 900, 'Ravi', '2026-09-04'),
(108, 'Curry House', 'Bangalore', 'Indian', 640, 'Kiran', '2026-09-04'),
(109, 'Burger Zone', 'Hyderabad', 'Fast Food', 430, 'Aman', '2026-09-05'),
(110, 'Sushi World', 'Mumbai', 'Japanese', 2100, 'Ravi', '2026-09-05'),
(111, 'Spice Hub', 'Hyderabad', 'Indian', 950, 'Aman', '2026-09-06'),
(112, 'Curry House', 'Bangalore', 'Indian', 880, 'Ravi', '2026-09-06');

-- 1
SELECT COUNT(*) AS total_orders FROM food_orders;

-- 2
SELECT SUM(order_amount) AS total_revenue FROM food_orders;

-- 3
SELECT AVG(order_amount) AS avg_order_value FROM food_orders;

-- 4
SELECT MAX(order_amount) AS highest_amount FROM food_orders;

-- 5
SELECT MIN(order_amount) AS lowest_amount FROM food_orders;

-- 6
SELECT city, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY city;

-- 7
SELECT restaurant, COUNT(*) AS no_of_orders
FROM food_orders
GROUP BY restaurant;

-- 8
SELECT food_type, AVG(order_amount) AS avg_order_value
FROM food_orders
GROUP BY food_type;

-- 9
SELECT delivery_partner, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY delivery_partner;

-- 10
SELECT city, COUNT(*) AS no_of_orders
FROM food_orders
GROUP BY city
HAVING COUNT(*) > 3;

-- 11
SELECT restaurant, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY restaurant
HAVING SUM(order_amount) > 2000;

-- 12
SELECT delivery_partner, AVG(order_amount) AS avg_amount
FROM food_orders
GROUP BY delivery_partner
HAVING AVG(order_amount) > 800;

-- 13
SELECT food_type, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY food_type
HAVING SUM(order_amount) > 2500;

-- 14
SELECT city, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY city
ORDER BY total_revenue DESC;

-- 15
SELECT restaurant, SUM(order_amount) AS total_revenue
FROM food_orders
GROUP BY restaurant
ORDER BY total_revenue DESC
LIMIT 1;

-- Practice Set 3 — JOIN Practice
-- Scenario: Training Institute

CREATE DATABASE training_institute_db;
USE training_institute_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    city VARCHAR(50)
);

INSERT INTO students VALUES
(1, 'Arun', 'Hyderabad'),
(2, 'Megha', 'Mumbai'),
(3, 'Zaid', 'Hyderabad'),
(4, 'Pooja', 'Pune'),
(5, 'Rohan', 'Delhi'),
(6, 'Sana', NULL),
(7, 'Vijay', 'Bangalore');

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    fee DECIMAL(10,2)
);

INSERT INTO courses VALUES
(101, 'Python', 15000),
(102, 'Data Engineering', 25000),
(103, 'Power BI', 12000),
(104, 'Cloud Computing', 20000),
(105, 'Cyber Security', 22000),
(106, 'Machine Learning', 28000);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE
);

INSERT INTO enrollments VALUES
(1001, 1, 101, '2026-09-01'),
(1002, 1, 102, '2026-09-03'),
(1003, 2, 103, '2026-09-04'),
(1004, 3, 102, '2026-09-05'),
(1005, 4, 104, '2026-09-06'),
(1006, 2, 101, '2026-09-07'),
(1007, 3, 105, '2026-09-08'),
(1008, 20, 102, '2026-09-09'),
(1009, 5, NULL, '2026-09-10');

-- 1
SELECT s.student_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 2
SELECT s.student_name, s.city, c.course_name, c.fee
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 3
SELECT s.student_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Data Engineering';

-- 4
SELECT s.student_name, e.enrollment_id, e.course_id
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id;

-- 5
SELECT s.student_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- 6
SELECT c.course_name, e.enrollment_id
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id;

-- 7
SELECT c.course_name
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- 8
SELECT e.*
FROM enrollments e
LEFT JOIN students s ON e.student_id = s.student_id
WHERE s.student_id IS NULL;

-- 9
SELECT e.*
FROM enrollments e
LEFT JOIN courses c ON e.course_id = c.course_id
WHERE c.course_id IS NULL;

-- 10
SELECT s.student_id, s.student_name, COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name;

-- 11
SELECT s.student_id, s.student_name, SUM(c.fee) AS total_fee
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id
GROUP BY s.student_id, s.student_name;

-- 12
SELECT s.student_name, COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name
HAVING COUNT(e.course_id) > 1;

-- 13
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
HAVING COUNT(e.student_id) > 1;

-- 14
SELECT c.course_name, SUM(c.fee) AS total_revenue
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- 15
SELECT c.course_name, SUM(c.fee) AS total_revenue
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY total_revenue DESC
LIMIT 1;

-- Practice Set 4 — Stored Procedures
-- Scenario: Vehicle Rental

CREATE DATABASE vehicle_rental_db;
USE vehicle_rental_db;

CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_name VARCHAR(100),
    vehicle_type VARCHAR(50),
    daily_rate DECIMAL(10,2),
    available_status VARCHAR(20)
);

INSERT INTO vehicles VALUES
(1, 'Honda City', 'Car', 2500, 'Available'),
(2, 'Toyota Innova', 'Car', 3500, 'Available'),
(3, 'Royal Enfield', 'Bike', 1200, 'Rented'),
(4, 'Activa', 'Scooter', 700, 'Available'),
(5, 'Mahindra Thar', 'SUV', 4500, 'Rented'),
(6, 'Hyundai Creta', 'SUV', 3200, 'Available'),
(7, 'KTM Duke', 'Bike', 1500, 'Available');

DELIMITER $$
-- 1
CREATE PROCEDURE GetAllVehicles()
BEGIN
    SELECT * FROM vehicles;
END $$

-- 2
CREATE PROCEDURE GetAvailableVehicles()
BEGIN
    SELECT * FROM vehicles WHERE available_status = 'Available';
END $$

-- 3
CREATE PROCEDURE GetVehiclesByType(IN v_type VARCHAR(50))
BEGIN
    SELECT * FROM vehicles WHERE vehicle_type = v_type;
END $$

-- 4
CREATE PROCEDURE GetVehiclesByMaxRate(IN max_rate DECIMAL(10,2))
BEGIN
    SELECT * FROM vehicles WHERE daily_rate <= max_rate;
END $$

-- 5
CREATE PROCEDURE UpdateDailyRate(IN v_id INT, IN new_rate DECIMAL(10,2))
BEGIN
    UPDATE vehicles SET daily_rate = new_rate WHERE vehicle_id = v_id;
END $$

-- 6
CREATE PROCEDURE ChangeVehicleStatus(IN v_id INT, IN new_status VARCHAR(20))
BEGIN
    UPDATE vehicles SET available_status = new_status WHERE vehicle_id = v_id;
END $$

-- 7
CREATE PROCEDURE IncreaseDailyRate(IN percent DECIMAL(5,2))
BEGIN
    UPDATE vehicles SET daily_rate = daily_rate + (daily_rate * percent / 100);
END $$

-- 8
CREATE PROCEDURE DeleteVehicle(IN v_id INT)
BEGIN
    DELETE FROM vehicles WHERE vehicle_id = v_id;
END $$

-- 9
CREATE PROCEDURE GetVehiclesBetweenRates(IN min_rate DECIMAL(10,2), IN max_rate DECIMAL(10,2))
BEGIN
    SELECT * FROM vehicles WHERE daily_rate BETWEEN min_rate AND max_rate;
END $$

-- 10
CREATE PROCEDURE CountVehiclesByType(IN v_type VARCHAR(50))
BEGIN
    SELECT COUNT(*) AS vehicle_count FROM vehicles WHERE vehicle_type = v_type;
END $$

DELIMITER ;

-- Practice Set 5 — Data Cleansing + RegEx
-- Scenario: Online Registration Data

CREATE DATABASE registration_data_db;
USE registration_data_db;

CREATE TABLE registrations (
    registration_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    mobile VARCHAR(40),
    city VARCHAR(50),
    postal_code VARCHAR(20)
);

INSERT INTO registrations VALUES
(1, ' rohit sharma ', ' ROHIT@GMAIL.COM ', '+91-98765-43210', 'hyderabad ', '500001'),
(2, 'SARA KHAN', 'sara@yahoo.com', '99887 66554', ' MUMBAI ', '400001'),
(3, ' amit patel ', '', '(040)99887766', 'Hyderabad', '500 032'),
(4, 'Neha Singh ', NULL, '9876543210', 'BANGALORE', '560001'),
(5, 'imran ali', 'IMRAN@MAIL.COM ', '91 9988772211', NULL, '500084'),
(6, 'Priya Rao', 'priya@gmail', '98765-AB210', 'Pune', '411001');

-- 1
SELECT TRIM(full_name) AS full_name FROM registrations;

-- 2
SELECT UPPER(TRIM(full_name)) AS full_name FROM registrations;

-- 3
SELECT LOWER(TRIM(email)) AS email FROM registrations;

-- 4
SELECT NULLIF(TRIM(email), '') AS email FROM registrations;

-- 5
SELECT REPLACE(REPLACE(mobile, ' ', ''), '-', '') AS mobile FROM registrations;

-- 6
SELECT REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile FROM registrations;

-- 7
SELECT UPPER(TRIM(city)) AS city FROM registrations;

-- 8
SELECT * FROM registrations WHERE city IS NULL;

-- 9
SELECT * FROM registrations WHERE email IS NULL OR TRIM(email) = '';

-- 10
SELECT * FROM registrations
WHERE LOWER(TRIM(email)) REGEXP 'gmail\\.com$';

-- 11
SELECT * FROM registrations
WHERE email IS NOT NULL AND TRIM(email) <> ''
AND LOWER(TRIM(email)) NOT REGEXP '^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$';

-- 12
SELECT registration_id, REGEXP_REPLACE(postal_code, '[^0-9]', '') AS postal_code
FROM registrations;

-- 13
SELECT * FROM registrations WHERE mobile REGEXP '[A-Za-z]';

-- 14
SELECT UPPER(TRIM(full_name)) AS name,
       NULLIF(LOWER(TRIM(email)), '') AS email,
       REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile,
       UPPER(TRIM(city)) AS city
FROM registrations;

-- 15
CREATE TABLE registrations_clean AS
SELECT registration_id,
       UPPER(TRIM(full_name)) AS full_name,
       NULLIF(LOWER(TRIM(email)), '') AS email,
       REGEXP_REPLACE(mobile, '[^0-9]', '') AS mobile,
       UPPER(TRIM(city)) AS city,
       REGEXP_REPLACE(postal_code, '[^0-9]', '') AS postal_code
FROM registrations;


-- Practice Set 6 — Analytical Functions + OVER + PARTITION BY
-- Scenario: Call Centre Performance

CREATE DATABASE call_centre_db;
USE call_centre_db;

CREATE TABLE call_performance (
    call_id INT PRIMARY KEY,
    agent_name VARCHAR(100),
    team VARCHAR(50),
    calls_handled INT,
    customer_rating DECIMAL(3,2),
    performance_date DATE
);

INSERT INTO call_performance VALUES
(1, 'Aman', 'Alpha', 42, 4.50, '2026-09-01'),
(2, 'Sara', 'Alpha', 38, 4.70, '2026-09-01'),
(3, 'Ravi', 'Beta', 50, 4.20, '2026-09-01'),
(4, 'Neha', 'Beta', 45, 4.80, '2026-09-01'),
(5, 'Aman', 'Alpha', 48, 4.60, '2026-09-02'),
(6, 'Sara', 'Alpha', 44, 4.50, '2026-09-02'),
(7, 'Ravi', 'Beta', 46, 4.30, '2026-09-02'),
(8, 'Neha', 'Beta', 52, 4.90, '2026-09-02'),
(9, 'Kabir', 'Alpha', 41, 4.40, '2026-09-01'),
(10, 'Kabir', 'Alpha', 49, 4.60, '2026-09-02'),
(11, 'Pooja', 'Beta', 45, 4.70, '2026-09-01'),
(12, 'Pooja', 'Beta', 50, 4.80, '2026-09-02');

-- 1
SELECT *, SUM(calls_handled) OVER () AS total_calls
FROM call_performance;

-- 2
SELECT *, SUM(calls_handled) OVER (PARTITION BY team) AS team_total_calls
FROM call_performance;

-- 3
SELECT agent_name, team, calls_handled,
       AVG(calls_handled) OVER (PARTITION BY team) AS team_avg_calls
FROM call_performance;

-- 4
SELECT *, AVG(customer_rating) OVER (PARTITION BY team) AS team_avg_rating
FROM call_performance;

-- 5
SELECT agent_name, performance_date, calls_handled,
       SUM(calls_handled) OVER (PARTITION BY agent_name ORDER BY performance_date) AS running_total
FROM call_performance;

-- 6
SELECT team, performance_date, calls_handled,
       SUM(calls_handled) OVER (PARTITION BY team ORDER BY performance_date) AS team_running_total
FROM call_performance;

-- 7
SELECT agent_name, team, calls_handled,
       AVG(calls_handled) OVER (PARTITION BY team) AS team_avg,
       calls_handled - AVG(calls_handled) OVER (PARTITION BY team) AS difference
FROM call_performance;

-- 8
SELECT agent_name, performance_date, calls_handled,
       LAG(calls_handled) OVER (PARTITION BY agent_name ORDER BY performance_date) AS prev_day_calls
FROM call_performance;

-- 9
SELECT agent_name, performance_date, calls_handled,
       calls_handled - LAG(calls_handled) OVER (PARTITION BY agent_name ORDER BY performance_date) AS difference
FROM call_performance;

-- 10
SELECT *, SUM(calls_handled) OVER (PARTITION BY agent_name) AS agent_total_calls
FROM call_performance;

-- Practice Set 7 — Ranking

USE call_centre_db;

-- 1
SELECT *, RANK() OVER (ORDER BY calls_handled DESC) AS call_rank
FROM call_performance;

-- 2
SELECT *, ROW_NUMBER() OVER (ORDER BY calls_handled DESC) AS row_num
FROM call_performance;

-- 3
SELECT *, RANK() OVER (ORDER BY calls_handled DESC) AS call_rank
FROM call_performance;

-- 4
SELECT *, DENSE_RANK() OVER (ORDER BY calls_handled DESC) AS dense_rank_no
FROM call_performance;

-- 5
SELECT agent_name, calls_handled,
       ROW_NUMBER() OVER (ORDER BY calls_handled DESC) AS row_num,
       RANK() OVER (ORDER BY calls_handled DESC) AS rank_no,
       DENSE_RANK() OVER (ORDER BY calls_handled DESC) AS dense_rank_no
FROM call_performance;

-- 6
SELECT team, agent_name, calls_handled,
       RANK() OVER (PARTITION BY team ORDER BY calls_handled DESC) AS team_rank
FROM call_performance;

-- 7
SELECT *, RANK() OVER (ORDER BY customer_rating DESC) AS rating_rank
FROM call_performance;

-- 8
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY team ORDER BY calls_handled DESC) AS rn
    FROM call_performance
)
SELECT * FROM ranked WHERE rn <= 3;

-- 9
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY agent_name ORDER BY calls_handled DESC) AS rn
    FROM call_performance
)
SELECT * FROM ranked WHERE rn = 1;

-- 10
SELECT agent_name, SUM(calls_handled) AS total_calls,
       RANK() OVER (ORDER BY SUM(calls_handled) DESC) AS agent_rank
FROM call_performance
GROUP BY agent_name;

-- Practice Set 8 — CTE + Correlated Subqueries
-- Scenario: Insurance Claims

CREATE DATABASE insurance_claims_db;
USE insurance_claims_db;

CREATE TABLE insurance_claims (
    claim_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    insurance_type VARCHAR(50),
    claim_amount DECIMAL(12,2),
    branch VARCHAR(50)
);

INSERT INTO insurance_claims VALUES
(1, 'Ajay Kumar', 'Health', 75000, 'Hyderabad'),
(2, 'Meena Shah', 'Motor', 45000, 'Mumbai'),
(3, 'Rohit Jain', 'Health', 125000, 'Hyderabad'),
(4, 'Sara Ali', 'Travel', 30000, 'Delhi'),
(5, 'Vikas Rao', 'Motor', 85000, 'Mumbai'),
(6, 'Nisha Singh', 'Health', 60000, 'Delhi'),
(7, 'Imran Khan', 'Travel', 55000, 'Hyderabad'),
(8, 'Pooja Patel', 'Motor', 40000, 'Delhi'),
(9, 'Karan Mehta', 'Health', 150000, 'Mumbai'),
(10, 'Farah Ahmed', 'Travel', 35000, 'Hyderabad');

-- 1
WITH type_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT * FROM type_total;

-- 2
WITH branch_total AS (
    SELECT branch, SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY branch
)
SELECT * FROM branch_total;

-- 3
WITH type_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT * FROM type_total WHERE total_claims > 200000;

-- 4
WITH avg_claim AS (
    SELECT AVG(claim_amount) AS avg_amount FROM insurance_claims
)
SELECT c.*
FROM insurance_claims c, avg_claim a
WHERE c.claim_amount > a.avg_amount;

-- 5
WITH type_total AS (
    SELECT insurance_type, SUM(claim_amount) AS total_claims
    FROM insurance_claims
    GROUP BY insurance_type
)
SELECT insurance_type, total_claims,
       RANK() OVER (ORDER BY total_claims DESC) AS type_rank
FROM type_total;

-- 6
WITH type_total AS (
    SELECT insurance_type, SUM(claim_amount) AS type_amount
    FROM insurance_claims
    GROUP BY insurance_type
),
branch_total AS (
    SELECT branch, SUM(claim_amount) AS branch_amount
    FROM insurance_claims
    GROUP BY branch
)
SELECT c.claim_id, c.customer_name, c.insurance_type, c.branch,
       c.claim_amount, t.type_amount, b.branch_amount
FROM insurance_claims c
JOIN type_total t ON c.insurance_type = t.insurance_type
JOIN branch_total b ON c.branch = b.branch;

-- 7
SELECT * FROM insurance_claims c
WHERE claim_amount > (SELECT AVG(claim_amount) FROM insurance_claims
                      WHERE insurance_type = c.insurance_type);

-- 8
SELECT * FROM insurance_claims c
WHERE claim_amount > (SELECT AVG(claim_amount) FROM insurance_claims
                      WHERE branch = c.branch);

-- 9
SELECT * FROM insurance_claims c
WHERE claim_amount = (SELECT MAX(claim_amount) FROM insurance_claims
                      WHERE insurance_type = c.insurance_type);

-- 10
SELECT customer_name, branch, claim_amount
FROM insurance_claims c
WHERE claim_amount > (SELECT AVG(claim_amount) FROM insurance_claims
                      WHERE branch = c.branch);
                      
-- Practice Set 9 — Hierarchical Queries
-- Scenario: Company Reporting Structure

CREATE DATABASE company_structure_db;
USE company_structure_db;

CREATE TABLE staff_hierarchy (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    manager_id INT,
    designation VARCHAR(100)
);

INSERT INTO staff_hierarchy VALUES
(1, 'Raj Malhotra', NULL, 'CEO'),
(2, 'Meera Shah', 1, 'CTO'),
(3, 'Vikram Rao', 1, 'Sales Director'),
(4, 'Aman Khan', 2, 'Engineering Manager'),
(5, 'Sara Ali', 2, 'Data Manager'),
(6, 'Rohit Das', 4, 'Developer'),
(7, 'Priya Singh', 4, 'Developer'),
(8, 'Kabir Ahmed', 5, 'Data Engineer'),
(9, 'Neha Rao', 5, 'Data Analyst'),
(10, 'Imran Sheikh', 3, 'Sales Manager'),
(11, 'Pooja Jain', 10, 'Sales Executive');

-- 1
SELECT * FROM staff_hierarchy WHERE manager_id IS NULL;

-- 2
SELECT * FROM staff_hierarchy
WHERE manager_id = (SELECT employee_id FROM staff_hierarchy WHERE designation = 'CEO');

-- 3
SELECT * FROM staff_hierarchy
WHERE manager_id = (SELECT employee_id FROM staff_hierarchy WHERE designation = 'CTO');

-- 4
WITH RECURSIVE org AS (
    SELECT employee_id, employee_name, manager_id, designation
    FROM staff_hierarchy
    WHERE manager_id IS NULL
    UNION ALL
    SELECT s.employee_id, s.employee_name, s.manager_id, s.designation
    FROM staff_hierarchy s
    JOIN org o ON s.manager_id = o.employee_id
)
SELECT * FROM org;

-- 5
WITH RECURSIVE org AS (
    SELECT employee_id, employee_name, manager_id, designation, 1 AS level_no
    FROM staff_hierarchy
    WHERE manager_id IS NULL
    UNION ALL
    SELECT s.employee_id, s.employee_name, s.manager_id, s.designation, o.level_no + 1
    FROM staff_hierarchy s
    JOIN org o ON s.manager_id = o.employee_id
)
SELECT * FROM org;

-- 6
WITH RECURSIVE team AS (
    SELECT employee_id, employee_name, manager_id, designation
    FROM staff_hierarchy
    WHERE manager_id = (SELECT employee_id FROM staff_hierarchy WHERE employee_name = 'Meera Shah')
    UNION ALL
    SELECT s.employee_id, s.employee_name, s.manager_id, s.designation
    FROM staff_hierarchy s
    JOIN team t ON s.manager_id = t.employee_id
)
SELECT * FROM team;

-- 7
WITH RECURSIVE team AS (
    SELECT employee_id, employee_name, manager_id, designation
    FROM staff_hierarchy
    WHERE manager_id = (SELECT employee_id FROM staff_hierarchy WHERE employee_name = 'Aman Khan')
    UNION ALL
    SELECT s.employee_id, s.employee_name, s.manager_id, s.designation
    FROM staff_hierarchy s
    JOIN team t ON s.manager_id = t.employee_id
)
SELECT * FROM team;

-- 8
SELECT e.employee_name AS employee, m.employee_name AS manager
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m ON e.manager_id = m.employee_id;

-- 9
WITH RECURSIVE org AS (
    SELECT employee_id, manager_id, 1 AS level_no
    FROM staff_hierarchy
    WHERE manager_id IS NULL
    UNION ALL
    SELECT s.employee_id, s.manager_id, o.level_no + 1
    FROM staff_hierarchy s
    JOIN org o ON s.manager_id = o.employee_id
)
SELECT level_no, COUNT(*) AS total_employees
FROM org
GROUP BY level_no
ORDER BY level_no;

-- 10
WITH RECURSIVE org AS (
    SELECT employee_id, employee_name, designation, 1 AS level_no,
           CAST(employee_name AS CHAR(500)) AS path
    FROM staff_hierarchy
    WHERE manager_id IS NULL
    UNION ALL
    SELECT s.employee_id, s.employee_name, s.designation, o.level_no + 1,
           CONCAT(o.path, ' > ', s.employee_name)
    FROM staff_hierarchy s
    JOIN org o ON s.manager_id = o.employee_id
)
SELECT employee_name, designation, level_no, path
FROM org
ORDER BY path;

-- Practice Set 10 — GROUP BY Extensions / ROLLUP
-- Scenario: Hotel Revenue

CREATE DATABASE hotel_revenue_db;
USE hotel_revenue_db;

CREATE TABLE hotel_bookings (
    booking_id INT PRIMARY KEY,
    hotel_city VARCHAR(50),
    room_type VARCHAR(50),
    nights INT,
    amount DECIMAL(10,2)
);

INSERT INTO hotel_bookings VALUES
(1, 'Hyderabad', 'Standard', 2, 6000),
(2, 'Hyderabad', 'Deluxe', 3, 13500),
(3, 'Hyderabad', 'Suite', 2, 18000),
(4, 'Mumbai', 'Standard', 2, 9000),
(5, 'Mumbai', 'Deluxe', 3, 18000),
(6, 'Mumbai', 'Suite', 1, 15000),
(7, 'Bangalore', 'Standard', 3, 10500),
(8, 'Bangalore', 'Deluxe', 2, 12000),
(9, 'Bangalore', 'Suite', 2, 20000);

-- 1
SELECT hotel_city, SUM(amount) AS total_revenue
FROM hotel_bookings
GROUP BY hotel_city;

-- 2
SELECT room_type, SUM(amount) AS total_revenue
FROM hotel_bookings
GROUP BY room_type;

-- 3
SELECT hotel_city, room_type, SUM(amount) AS total_revenue
FROM hotel_bookings
GROUP BY hotel_city, room_type;

-- 4
SELECT hotel_city, room_type, SUM(amount) AS total_revenue
FROM hotel_bookings
GROUP BY hotel_city, room_type WITH ROLLUP;

-- 5
SELECT SUM(amount) AS grand_total FROM hotel_bookings;

-- 6
SELECT hotel_city, room_type, SUM(nights) AS total_nights
FROM hotel_bookings
GROUP BY hotel_city, room_type;

-- 7
SELECT hotel_city, room_type, SUM(nights) AS total_nights, SUM(amount) AS total_amount
FROM hotel_bookings
GROUP BY hotel_city, room_type WITH ROLLUP;



