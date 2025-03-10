# parquet files are a columnar storage format that is optimized for reading and writing data in bulk.
# they are very common in the big data world, and are a great way to store data for analysis.
# We need to install pyarrow in  order to read the parquet file

import pyarrow.parquet as pq

my_data = pq.read_table(
    "D:\\Proyectos de codigo\\python\\code\\data_sources\\Parquet_files\\house-price.parquet"
)
# here we are going to print the shape of the data
print(my_data.shape)

# after that we have to print the data:
print(my_data)

# As we see its a lot of data so we need to filter them
new_data = pq.read_table(
    "example.parquet",
    columns=["col1"],
    filters=[
        ("col1", ">", 5),
        ("col1", "<", 10),
    ],
)
