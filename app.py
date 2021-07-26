import datetime
import sys
import database as db


menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user.
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)

def prompt_add_movie():
    title = input("movie title: ")
    release_date = input("release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    db.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d, %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("--- \n")

def prompt_watch_movie():
    user = input("Username: ")
    movie_id = input("Movie ID: ")
    db.watch_movie(user, movie_id)

def prompt_add_user():
    username = input("Username: ")
    db.add_user(username)

def prompt_show_watched_movies():
    username = input("username: ")
    movies = db.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("user has not watched any movies yet")

db.create_table()

while (user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = db.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = db.get_movies(False)
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    else:
        print("Invalid input, please try again!")
