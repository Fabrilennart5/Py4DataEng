# Pandas is a powerful library for data manipulation and analysis.
# It provides data structures like DataFrames, which are essential for working with structured data.

import pandas as pd

# Reading a CSV file into a DataFrame
# Note: We use double backslashes (\\) to escape the backslash character in the file path.
users_data = pd.read_csv("D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\users.csv")

# Convert columns to more specific data types
users_data["customer_id"] = users_data["customer_id"].astype("Int64")
users_data["first_name"] = users_data["first_name"].astype("string")
users_data["last_name"] = users_data["last_name"].astype("string")
users_data["email"] = users_data["email"].astype("string")
users_data["city"] = users_data["city"].astype("string")
users_data["country"] = users_data["country"].astype("string")

# Display the shape of the DataFrame (number of rows and columns)
print("=== Shape of the Dataset ===")
print(f"The dataset has {users_data.shape[0]} rows and {users_data.shape[1]} columns.")
print("\n")

# Display the first 2 rows of the DataFrame
print("=== First 2 Rows of the Dataset ===")
print(users_data.head(2))
print("\n")  # Add a newline for better readability

# Display the last 2 rows of the DataFrame
print("=== Last 2 Rows of the Dataset ===")
print(users_data.tail(2))
print("\n")

# Display a random sample of 3 rows from the DataFrame
print("=== Random Sample of 3 Rows from the Dataset ===")
print(users_data.sample(3))
print("\n")

# Display basic information about the DataFrame
print("=== Basic Information About the Dataset (Updated Dtypes) ===")
users_data.info()
print("\n")

# Display descriptive statistics for numeric columns (rounded to 2 decimal places)
print("=== Descriptive Statistics for Numeric Columns (Rounded) ===")
print(users_data.describe().round(2))
print("\n")

# Display the index of the DataFrame
print("=== Index of the Dataset ===")
print(f"The index of the dataset is: {users_data.index}")
print("\n")

# Display the column names directly using .columns
print("=== Column Names Using .columns ===")
print(f"The columns are: {users_data.columns}")
print("\n")
