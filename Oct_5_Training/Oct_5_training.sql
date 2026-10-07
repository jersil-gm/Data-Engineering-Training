create database DE_training_db;
use DE_training_db;

create table employees
(
	emp_id int primary key,
    emp_name varchar(100),
    department varchar(50),
    salary decimal(10,2),
    city varchar(50)
);

insert into employees
values
(1,'Anit Sharma','IT',60000,'Hyderabad'),
(2,'Sara Khan', 'HR',50000,'Banglore');

insert into employees
values
(3,'Rahul','Finance',55000,'Hyderabad'),
(4,'Neha','IT',65000,'Pune'),
(5,'Arjun','Sales',45000,'Mumbai');

select * from employees;

update employees
set emp_name= 'Rahul Verma'
where emp_id=3;

update employees
set emp_name='Neha Singh'
where emp_id=4;

delete from employees 
where emp_id =5;

-- oct 5 training
create database shop_db;
use shop_db;

create table products
(
	Product_ID int primary key,
    Product_name varchar(200),
    Category varchar(100),
    Price decimal(10,2),
    stock_quantity int
);

INSERT INTO products (product_id, product_name, category, price, stock_quantity) VALUES
(1, 'Smartphone', 'Electronics', 15000.00, 25),
(2, 'Laptop Backpack', 'Accessories', 1200.00, 15),
(3, 'Bluetooth Speaker', 'Electronics', 2500.00, 8),
(4, 'Running Shoes', 'Footwear', 3200.00, 12),
(5, 'Coffee Mug', 'Home & Kitchen', 350.00, 50),
(6, 'Desk Lamp', 'Home & Kitchen', 850.00, 5);

select * from products;

select product_name,Price from products;

INSERT INTO products (product_id, product_name, category, price, stock_quantity) 
VALUES (7, 'Wireless Mouse', 'Electronics', 899.00, 20);

update products set price='150' where product_id=5;

update products set price=price*1.10 where category='Electronics';

update products set stock_quantity=stock_quantity-3 where product_id=4;

update products set category='Electronics' where product_id=6;

select * from products where price >=1000;

select * from products where stock_quantity < 10;

select * from products where category='Electronics';

select * from products order by price Desc;

delete from products where product_id=2;

delete from products where stock_quantity=0;

select * from products;


