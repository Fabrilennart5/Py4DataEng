# Most APIs are based on JSON (JavaScript Object Notation)
# so you need to learn how to work with this format
import json
from pprint import pprint
import pandas as pd

# Declare a variable with the path to the JSON file
path = r"D:\Proyectos de codigo\python\code\data_sources\movies.json"

# Open the file in read mode
with open(path, "r", encoding="utf-8") as file:
    # Load the JSON file into a dictionary
    data = json.load(file)  # json.load() reads the file and converts it to a Python dictionary

# Print the raw JSON data in a pretty format
print("Raw JSON data:")
pprint(data)

# Access the list of movies
movies = data["peliculas"]

# Print all movies in the JSON data
print("\nMovies in the JSON data:")
pprint(movies)

# Find and print details of "Interstellar"
print("\nDetails of 'Interstellar':")
for movie in movies:
    if movie["titulo"] == "Interstellar":
        pprint(movie)  # Pretty-print the movie details
        break  # Exit the loop once the movie is found
else:
    print("Movie 'Interstellar' not found.")

# Access a specific movie by index (e.g., "Fight Club")
fight_club = movies[5]  # "Fight Club" is at index 5
print("\nDetails of 'Fight Club':")
pprint(fight_club)  # Pretty-print the movie details

# Access a specific value from the movie dictionary
print("\nThe genre of the movie 'Fight Club' is:")
print(fight_club["genero"])  # Print the genre directly

# Convert the movie data to a tabular format using pandas
# This is useful for better visualization and manipulation
fight_club_df = pd.DataFrame.from_dict(fight_club, orient="index").T

# Print the movie data in a tabular format
print("\nThe data of the movie 'Fight Club' in a tabular format:")
print(fight_club_df)  # This is not magic, just Python and pandas!
