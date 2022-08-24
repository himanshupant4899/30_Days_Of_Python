
# Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user
# to provide information for each of these fields and create an instance of the Movie tuple you defined.
from collections import namedtuple

Movie = namedtuple("Movie", ["title", "director", "release_year"])

movie = Movie(
    input("Enter movie title: "),
    input("Enter director: "),
    input("Enter the release year: ")
)

print(f"{movie.title} ({movie.release_year}) directed by {movie.director}")
