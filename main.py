import mysql.connector

# Connect to the MySQL database in the Docker container
connection = mysql.connector.connect(
    host="localhost",     
    user="user",          
    password="password",  
    database="mydatabase" 
)

cursor = connection.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);
""")

# Complex SQL query to join multiple tables, aggregate data, and sort results
query = """
    SELECT c.name AS customer_name, SUM(oi.quantity * oi.price) AS total_spent
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    GROUP BY c.name
    ORDER BY total_spent DESC;
"""

# Execute the query
cursor.execute(query)

# Fetch and display the results
results = cursor.fetchall()
for row in results:
    print(f"Customer: {row[0]}, Total Spent: ${row[1]:.2f}")

# Close the connection
cursor.close()
connection.close()



