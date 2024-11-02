import pytest
import mysql.connector
from main import query_data

# Set up MySQL database connection parameters
DB_CONFIG = {
    'host': 'localhost',
    'user': 'user',          # Same as in docker-compose.yml
    'password': 'password',   # Same as in docker-compose.yml
    'database': 'mydatabase'  # Same as in docker-compose.yml
}

@pytest.fixture
def db_conn():
    # Connect to the MySQL database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Set up the necessary tables
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, order_date DATE, FOREIGN KEY (customer_id) REFERENCES customers(id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS order_items (id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, product_name VARCHAR(255), quantity INT, price DECIMAL(10, 2), FOREIGN KEY (order_id) REFERENCES orders(id));")

    yield conn  # Provide the database connection to the test functions

    # Clean up tables after tests
    cursor.execute("DROP TABLE IF EXISTS order_items;")
    cursor.execute("DROP TABLE IF EXISTS orders;")
    cursor.execute("DROP TABLE IF EXISTS customers;")
    conn.close()

def test_table_creation(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SHOW TABLES LIKE 'customers';")
    assert cursor.fetchone() is not None, "Table 'customers' was not created."

    cursor.execute("SHOW TABLES LIKE 'orders';")
    assert cursor.fetchone() is not None, "Table 'orders' was not created."

    cursor.execute("SHOW TABLES LIKE 'order_items';")
    assert cursor.fetchone() is not None, "Table 'order_items' was not created."

def test_query_data(db_conn):
    # Insert sample data for testing
    cursor = db_conn.cursor()
    cursor.execute("INSERT INTO customers (name) VALUES ('Test Customer');")
    customer_id = cursor.lastrowid
    cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, NOW());", (customer_id,))
    order_id = cursor.lastrowid
    cursor.execute("INSERT INTO order_items (order_id, product_name, quantity, price) VALUES (%s, 'Test Product', 2, 50.00);", (order_id,))

    db_conn.commit()

    # Run the query and check the output
    result = query_data(db_conn)
    assert len(result) > 0, "Query returned no results."
    assert result[0][0] == 'Test Customer', "Customer name does not match."
    assert result[0][1] == 100.00, "Total spent calculation is incorrect."

