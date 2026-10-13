CREATE DATABASE IF NOT EXISTS sales_analytics;
USE sales_analytics;

CREATE TABLE IF NOT EXISTS sales (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    customer_name VARCHAR(120) NOT NULL,
    region VARCHAR(50) NOT NULL,
    product VARCHAR(120) NOT NULL,
    category VARCHAR(80) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL
);
