# now lets talk about lambdas, they are reall  useful when you have to work
# in python in general, but lets check how we can use them in a program.

import pandas as pd

users_data = pd.read_csv(
    "D:\\Proyectos de codigo\\python\\code\\data_sources\\Csv_data\\users.csv"
)

# first lets read the csv file:
print(users_data.head(5))
