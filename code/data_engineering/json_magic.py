# Working with JSON is essential since most APIs use this format.
# Python's `json` module makes it easy to parse and manipulate JSON data.

import json
from pprint import pprint
import pandas as pd

# Path to the JSON file
path = r"D:\Proyectos de codigo\python\code\data_sources\movies.json"

# Open and load the JSON file
with open(path, "r", encoding="utf-8") as file:
    data = json.load(file)  # Convert JSON to a Python dictionary

# Pretty-print the raw JSON data
print("Raw JSON data:")
pprint(data)

# Access the list of movies
movies = data["peliculas"]

# Print all movies
print("\nMovies in the JSON data:")
pprint(movies)

# Find and print details of "Interstellar"
print("\nDetails of 'Interstellar':")
for movie in movies:
    if movie["titulo"] == "Interstellar":
        pprint(movie)  # Pretty-print the movie details
        break
else:
    print("Movie 'Interstellar' not found.")

# Access a specific movie by index (e.g., "Fight Club")
fight_club = movies[5]  # "Fight Club" is at index 5
print("\nDetails of 'Fight Club':")
pprint(fight_club)

# Access a specific value (genre) from the movie dictionary
print("\nThe genre of 'Fight Club' is:")
print(fight_club["genero"])

# Convert the movie data to a DataFrame for better visualization
fight_club_df = pd.DataFrame.from_dict(fight_club, orient="index").T

# Print the movie data in a tabular format
print("\nData of 'Fight Club' in a tabular format:")
print(fight_club_df)
