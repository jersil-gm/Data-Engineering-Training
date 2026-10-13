CREATE DATABASE IF NOT EXISTS expense_monitoring_db;
USE expense_monitoring_db;

-- 1. Schema: users, expenses, categories
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
);

-- 2. CRUD Operations
-- CREATE
INSERT INTO users (username, email) VALUES 
('jersil', 'jersil@example.com'),
('alex', 'alex@example.com');

INSERT INTO categories (category_name) VALUES 
('Groceries'),
('Utilities'),
('Entertainment'),
('Rent'),
('Healthcare');

INSERT INTO expenses (user_id, category_id, amount, expense_date, description) VALUES
(1, 1, 125.50, '2026-01-05', 'Weekly supermarket run'),
(1, 2, 85.00, '2026-01-12', 'Electricity bill'),
(2, 3, 45.00, '2026-01-15', 'Movie tickets'),
(1, 1, 64.20, '2026-01-20', 'Local market'),
(2, 4, 1200.00, '2026-01-28', 'January house rent');

-- READ
SELECT 
    e.expense_id,
    u.username,
    c.category_name,
    e.amount,
    e.expense_date,
    e.description
FROM expenses e
JOIN users u ON e.user_id = u.user_id
JOIN categories c ON e.category_id = c.category_id
ORDER BY e.expense_date DESC;

-- UPDATE
UPDATE expenses
SET amount = 95.00, description = 'Electricity bill (revised)'
WHERE expense_id = 2;

-- DELETE
DELETE FROM expenses
WHERE expense_id = 3;

-- 3. Stored Procedure: Calculate monthly total expenses per category
DROP PROCEDURE IF EXISTS CalculateMonthlyExpensesPerCategory;

DELIMITER $$
CREATE PROCEDURE CalculateMonthlyExpensesPerCategory(
    IN p_user_id INT,
    IN p_year INT,
    IN p_month INT
)
BEGIN
    SELECT 
        c.category_name,
        COALESCE(SUM(e.amount), 0.00) AS total_expense,
        COUNT(e.expense_id) AS total_transactions
    FROM categories c
    LEFT JOIN expenses e 
        ON c.category_id = e.category_id 
        AND e.user_id = p_user_id
        AND YEAR(e.expense_date) = p_year
        AND MONTH(e.expense_date) = p_month
    GROUP BY c.category_id, c.category_name
    ORDER BY total_expense DESC;
END$$
DELIMITER ;

-- Test procedure:
-- CALL CalculateMonthlyExpensesPerCategory(1, 2026, 1);