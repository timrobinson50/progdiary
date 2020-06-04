import datetime
import os
from builtins import len
from time import strftime

import database

movies = []

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the movies!"

def prompt_add_movie():
    title = input("Enter movie name: ")
    release_date = input("Enter the release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)
    os.system('clear')


def print_movie_list(heading, movies):
    os.system('clear')

    print(f"---- {heading} Movies ----")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{movie[0]:15}  (on {human_date})")
    print("--------------------------- \n")

def print_watched_movie_list(username, movies):
    os.system('clear')
    print(f"---- {username}'s watched movies ----")
    for movie in movies:
        print(f"{movie[1]}")
    print("--------------------------- \n")

def prompt_watch_movie():
    username = input("Username: ")
    movie_title = input("Enter movie title you've watched: ")
    database.watch_movie(username, movie_title)
    os.system('clear')

os.system('clear')
print(welcome)
database.create_table()

user_input = input(menu)
while user_input != "6":
    # Deal with user input here
    if (user_input == "1"):
        prompt_add_movie()
    elif (user_input == "2"):
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif (user_input == "3"):
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif (user_input == "4"):
        prompt_watch_movie()
    elif (user_input == "5"):
        username = input("Username: ")
        movies = database.get_watched_movie(username)
        print_watched_movie_list(username, movies)
    else:
        print("Invalid, please try again")

    user_input = input(menu)
