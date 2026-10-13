USE sales_analytics;

-- Overall KPIs
SELECT
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS unique_customers,
    ROUND(SUM(quantity * unit_price) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM sales;

-- Monthly sales trend
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- Top customers by revenue
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY customer_id, customer_name
ORDER BY revenue DESC;

-- Product performance
SELECT
    product,
    category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY product, category
ORDER BY revenue DESC;

-- Regional performance
SELECT
    region,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY region
ORDER BY revenue DESC;
