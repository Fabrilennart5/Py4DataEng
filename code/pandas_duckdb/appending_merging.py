import pandas as pd

# APPENDING
# Reading a CSV file into a DataFrame
print("Loading users data...")
users_data = pd.read_csv("D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\users.csv")

# Appending new rows to the DataFrame
print("Loading additional users data...")
users_data2 = pd.read_csv("D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\users2.csv")

# Check if both DataFrames have the same columns
if set(users_data.columns) == set(users_data2.columns):
    # Combine the two datasets using pd.concat()
    complete_data = pd.concat([users_data, users_data2], ignore_index=True)

    # Display the combined dataset
    print("\nComplete dataset after appending:")
    print(complete_data)
    print("\nShape of the complete dataset:", complete_data.shape)
else:
    print("Error: The columns in users_data and users_data2 do not match.")
    print("Columns in users_data:", users_data.columns)
    print("Columns in users_data2:", users_data2.columns)

# MERGING
# Merging DataFrames based on a common column
print("\nLoading orders data...")
orders_data = pd.read_csv("D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\orders.csv")

# Perform the merge
print("\nMerging users data with orders data...")
users_data_with_orders = pd.merge(users_data, orders_data, on="customer_id", how="inner")

# Select specific columns for clarity
selected_columns = users_data_with_orders.loc[:, ["customer_id", "order_id", "order_date", "total_amount", "city"]]

# Display the result of the merge
print("\nResult of the merge (selected columns):")
print(selected_columns)
print("\nNumber of rows in the merged dataset:", len(selected_columns))
