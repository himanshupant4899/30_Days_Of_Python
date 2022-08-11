#Provided Data

movies = [("Eternal Sunshine of the Spotless Mind", 20000000),
          ("Memento", 9000000), ("Requiem for a Dream", 4500000),
          ("Pirates of the Caribbean: On Stranger Tides", 379000000),
          ("Avengers: Age of Ultron", 365000000),
          ("Avengers: Endgame", 356000000), ("Incredibles 2", 200000000)]

#allow users to add more movies to the data set before running the calculations.

num = int(
    input("Enter number of new movies you want to add to existing dataset: "))
for n in range(num):
    movie_name = input("Enter movie name: ")
    movie_budget = int(input("Enter movie budget: "))
    new_movie = (movie_name, movie_budget)
    movies.append(new_movie)

#Calculate the average budget of all movies in the data set.
total_budget = 0
for movie in movies:
    total_budget += movie[1]

avg = total_budget / len(movies)
print(avg)

#Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
#Print out how many movies spent more than the average you calculated.

count = 0
for movie in movies:
    if movie[1] > avg:
        print(f"{movie[0]} exceeds the average budget by: {movie[1]-avg}")
        count += 1
print(f"{count} movies have more than average budget")
