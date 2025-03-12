# DuckDB is a high-performance, in-memory database optimized for analytical queries.
# It enables direct querying of structured data from CSV files
# without requiring a traditional database setup.

import duckdb

# Define the path to the JSON file
path = r"D:\Proyectos de codigo\python\code\data_sources\Json_data\transacciones.json"

# Run the SQL query to read the JSON file
query = f"SELECT * FROM read_json_auto('{path}')"

# Execute the query and fetch results
data = duckdb.sql(query)

# Print the results
print(data)
