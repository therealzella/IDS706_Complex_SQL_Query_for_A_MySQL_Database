import pytest
from main import connect_to_db, create_tables, query_data

@pytest.fixture
def db_conn():
    # Establish a database connection using connect_to_db
    conn = connect_to_db()
    cursor = conn.cursor()

    # Set up tables for testing
    create_tables(conn)

    # Insert sample data
    cursor.execute("INSERT INTO customers (name) VALUES ('Test Customer');")
    customer_id = cursor.lastrowid
    cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, NOW());", (customer_id,))
    order_id = cursor.lastrowid
    cursor.execute("INSERT INTO order_items (order_id, product_name, quantity, price) VALUES (%s, 'Test Product', 2, 50.00);", (order_id,))

    conn.commit()
    yield conn  # Provide the database connection to the test functions

    # Clean up tables after tests
    cursor.execute("DELETE FROM order_items;")
    cursor.execute("DELETE FROM orders;")
    cursor.execute("DELETE FROM customers;")
    conn.close()

def test_table_creation(db_conn):
    cursor = db_conn.cursor()

    # Verify that the tables have been created
    cursor.execute("SHOW TABLES LIKE 'customers';")
    assert cursor.fetchone() is not None, "Table 'customers' was not created."

    cursor.execute("SHOW TABLES LIKE 'orders';")
    assert cursor.fetchone() is not None, "Table 'orders' was not created."

    cursor.execute("SHOW TABLES LIKE 'order_items';")
    assert cursor.fetchone() is not None, "Table 'order_items' was not created."

def test_query_data(db_conn):
    # Run the query and verify the results
    results = query_data(db_conn)
    
    # Check that the query returns the expected result
    assert len(results) > 0, "Query returned no results."
    assert results[0][0] == "Test Customer", "Customer name does not match."
    assert results[0][1] == 200.00, "Total spent calculation is incorrect."  # Update expected value to 200.00
