import mysql.connector

# Connect to the MySQL database in the Docker container
connection = mysql.connector.connect(
    host="localhost",     
    user="user",          
    password="password",  
    database="mydatabase" 
)

cursor = connection.cursor()

# Create or update your tables here if needed
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    total_amount_spent DECIMAL(10, 2) NOT NULL
);
""")

query = "YOUR_COMPLEX_QUERY_HERE"  # Replace this with the actual query logic
cursor.execute(query)

# Fetch and display the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
cursor.close()
connection.close()



