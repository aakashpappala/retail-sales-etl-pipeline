SELECT COUNT(*) FROM sales;

SELECT SUM(total_amount) AS total_revenue
FROM sales;

SELECT product,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;