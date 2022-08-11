#given
movies = [("Wonder Woman", "Patty Jenkins", "2017", "$150 Million")]

# input user data
movie_name = input("Enter Movie Name: ")
directed_by = input("Enter director Name: ")
release_year = input("Enter release year: ")
budget = input("Enter Movie budget: ")

# create new tuple
movie = (movie_name, directed_by, release_year, budget)

# print movie name and release year using f-string
print(f'movie name: {movie[0]}, release_year: {movie[2]}')

#Add the new movie tuple to the movies collection using append.
movies.append(movie)
print(movies)

#Print both movies in the movies collection
print(f'{movies[0][0]} and {movies[1][0]}')

#Remove the first movie from movies
del movies[0]

print(movies)
