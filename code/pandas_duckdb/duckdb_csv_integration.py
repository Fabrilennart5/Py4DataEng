# DuckDB is a high-performance, in-memory database optimized for analytical queries.
# It enables direct querying of structured data from CSV files
# without requiring a traditional database setup.

import duckdb

# Define the path to the CSV file
csv_path = r"D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\electronics_store_sales.csv"

# Example 1: Load and display the entire CSV file
print("Full CSV Data:")
print(duckdb.read_csv(csv_path))

# Example 2: Query to count customers per country
query = f"""
    SELECT customer_country, COUNT(order_id) 
    FROM read_csv_auto('{csv_path}') 
    GROUP BY customer_country
"""

print("\nCustomer count per country:")
print(duckdb.sql(query))

# Exmaple 3: Query that returns the data for a especif user
query2 = f"""
    SELECT * FROM read_csv_auto('{csv_path}')
    WHERE product_category = 'Laptops'
"""

print("\nAll products related to the laptop category:")
print(duckdb.sql(query2))

# Example 3: Query to group the data by year.
query3 = f"""
    SELECT EXTRACT(YEAR FROM order_date) AS Year, COUNT(order_id) AS Order_Count
    FROM read_csv_auto('{csv_path}')
    GROUP BY Year
    ORDER BY Year;
"""

print("\nQuantity of orders by year:")
print(duckdb.sql(query3))
