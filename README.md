# IDS706_Complex_SQL_Query_for_A_MySQL_Database

![CI](https://github.com/therealzella/IDS706-python-github-template/actions/workflows/ci.yml/badge.svg)

## Project Overview
This repository is for an IDS706 course assignment that demonstrates a complex SQL query executed on a MySQL database set up using Docker. The query involves joining multiple tables, aggregating data, and sorting results to display total amounts spent by each customer.

A CI/CD pipeline is implemented using GitHub Actions to automate the setup, testing, and execution of the query.

## How It Works
- **SQL Query**: The query joins the `customers`, `orders`, and `order_items` tables to calculate the total value of orders placed by each customer, displaying results sorted in descending order of total spending.
- **Docker**: The MySQL database is set up in a Docker container, allowing for easy deployment and isolation of the database environment.
- **CI/CD Pipeline**: The pipeline is configured to automatically run on every push to the repository. It sets up the MySQL environment, runs the tests, executes the SQL query, and logs the output.

## Project Files
- `main.py`: The main script that connects to the MySQL database, sets up tables, inserts sample data, and executes the complex SQL query.
- `main_test.py`: Test script to validate the database connection, table creation, data insertion, and query functionality.
- `complex_query.sql`: Contains the SQL logic executed within `main.py`.
- `.github/workflows/ci.yml`: Defines the GitHub Actions CI/CD pipeline, which automates the MySQL setup, testing, and query execution.


## Steps to Run the Project

1. **Clone the Repository**:
```bash
git clone https://github.com/your-username/IDS706_Complex_SQL_Query_for_A_MySQL_Database.git
cd IDS706_Complex_SQL_Query_for_A_MySQL_Database
```

2. **Set Up Docker and MySQL**:
- Make sure Docker is installed and running.
- Start the MySQL database container:
  docker-compose up -d

3. **Run the Main Script**:
  python main.py

4. **Expected Output**:
- The output should display a list of customers and their total spending, sorted in descending order. For example:

  ""Customer: Test Customer, Total Spent: $200.00""
  
This result shows the total amount spent by each customer, based on the sample data added during the setup.


## CI/CD Documentation
This project utilizes GitHub Actions for continuous integration, ensuring that all code pushed to the main branch is automatically tested and validated.

  - ### Continuous Integration and Deployment
  - **CI/CD Process**: This project uses GitHub Actions for continuous integration. Our CI pipeline automatically runs on every push or pull request to the `main` branch.
  - **Setup**: The workflow sets up the Python environment based on the matrix configuration.
  - **Dependency Installation**: Dependencies are installed using the requirements file.
  - **Linting**: Code is linted with flake8 to ensure it meets our coding standards.
  - **Testing**: Tests are executed using pytest to validate functionality.

    - Automated Testing: On every push or pull request to the main branch, the CI pipeline runs linting, testing,         and other checks defined in the ci.yml file.
        - Steps Included in the Workflow:
        - Setup of the specified Python environment using actions/setup-python@v3.
        - Installation of dependencies via make install.
        - Linting with flake8 to maintain code quality.
        - Running unit tests with pytest.
