# Import pandas to work with DataFrames
import pandas as pd

# Load the CSV file containing user data
users_data = pd.read_csv(
    "D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\users.csv"
)

# Filter users from the USA using a lambda function
# Lambdas are great for quick, one-time operations like filtering or transforming data.
usa_users = users_data[users_data["country"].apply(lambda x: x == "usa")]
print(usa_users)

# Add a new column: full_name by combining first_name and last_name
# Lambdas are perfect for simple row-wise operations.
users_data["full_name"] = users_data.apply(
    lambda row: f"{row['first_name']} {row['last_name']}", axis=1
)
print(users_data)

# Clean data: Convert emails to lowercase
# Lambdas are ideal for quick data cleaning tasks.
users_data["email"] = users_data["email"].apply(lambda x: x.lower())
print(users_data)

# When to use lambdas:
# - For quick, one-time operations (filtering, transforming, cleaning).
# - When the logic is simple and doesn't need a full function.

# When NOT to use lambdas:
# - For complex logic (use a defined function instead).
# - If you need to reuse the function multiple times.
