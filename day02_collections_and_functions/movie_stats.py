"""
✅ 📦 Project: Simple Movie Stats App
A small script that:

Stores info about movies (as dicts & lists)

Prints details nicely

Finds highest rated movie

Sums total ratings

Counts how many movies were released after 2015

Lists unique first letters of movie titles

"""

movies = [
    {'title': 'Inception', 'year': 2010, 'rating': 8.8},
    {'title': 'Interstellar', 'year': 2014, 'rating': 8.6},
    {'title': 'Tenet', 'year': 2020, 'rating': 7.3},
    {'title': 'Dunkirk', 'year': 2017, 'rating': 7.9}
]


def print_details():

    for movie in movies:
        print(
            f'Title: {movie['title']}, year: {movie['year']}, rating: {movie['rating']}')
    return


# print_details()
def highest_rated_movie():
    highest_rating = 0
    best_movie = None  # to also keep track of the movie itself

    for movie in movies:
        if movie['rating'] > highest_rating:
            highest_rating = movie['rating']
            best_movie = movie

    print(
        f"Highest rated movie is {best_movie['title']} with rating {highest_rating}")
    return


# highest_rated_movie()

def sums_total_rating():
    total_rating = 0
    for movie in movies:
        total_rating = total_rating + movie['rating']

    print(f'Total rating: {total_rating}')
    return


sums_total_rating()


def count_recent_movies():
    count = 0
    for movie in movies:
        if movie['year'] > 2015:
            count += 1

    print(count)
    return


# count_recent_movies()

def unique_first_letters():
    first_movie_letters = set()
    # first_movie_letters = {} this creates an *empty dictionary*, not a set!
    for movie in movies:
        title = movie['title']
        first_movie_letters.add(title[0])

    print(first_movie_letters)
    return


unique_first_letters()
