import mysql.connector
import os

# Connect to the MySQL database using environment variables
def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "mydatabase")
    )

# Function to create tables if they don't exist
def create_tables(conn):
    cursor = conn.cursor()
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
    cursor.close()

# Define the function to run the complex query
def query_data(conn):
    cursor = conn.cursor()
    query = """
        SELECT c.name AS customer_name, SUM(oi.quantity * oi.price) AS total_spent
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        JOIN order_items oi ON o.id = oi.order_id
        GROUP BY c.name
        ORDER BY total_spent DESC;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# Main function to connect, create tables, run the query, and display results
if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_db()
    
    # Create tables if they don't exist
    create_tables(connection)
    
    # Run the complex query and fetch results
    results = query_data(connection)
    
    # Display the results
    for row in results:
        print(f"Customer: {row[0]}, Total Spent: ${row[1]:.2f}")
    
    # Close the connection
    connection.close()
