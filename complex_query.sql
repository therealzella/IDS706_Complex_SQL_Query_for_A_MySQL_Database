SELECT customers.customer_name, SUM(orders.order_total) AS total_spent
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
GROUP BY customers.customer_name
ORDER BY total_spent DESC;
