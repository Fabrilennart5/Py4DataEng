# Melting is the process of reshaping a DataFrame from a wide format
# to a long format using the Pandas melt() function.
import pandas as pd

# Reading a CSV file that contains data into a DataFrame
# "users_data" now holds the contents of the CSV file located at the given path
users_data = pd.read_csv(
    "D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\empresas.csv"
)

# Display the first 5 rows of the dataset to check its contents
# This helps us understand the structure of the data before any transformation
print(users_data.head(5))

# Melting the DataFrame.
# This will reshape the DataFrame from wide format (multiple columns for each company) to long format
# meaning that columns will be represented as rows (unpivot)
# "id_vars" specifies the columns to keep as identifiers (in this case, the "Date").
# "value_vars" specifies the columns to melt (the companies' columns like Apple, Microsoft, Amazon, and Google).
melted_data = users_data.melt(
    id_vars=["Date"],  # 'Date' will be using as and  identificator
    value_vars=[
        "Apple",
        "Microsoft",
        "Amazon",
        "Google",
    ],  # The columns that will be melth
    var_name="Company",  # New name for the column that will have the companies name
    value_name="Price",  # New name for the column that will have the values (price)
)

# print the new df :)
print("\nMelted DataFrame:")
print(melted_data)
