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
6) Add user
7) Exit.

Your selection: """
welcome = "Welcome to the movies!"

def prompt_add_movie():
    title = input("Enter movie name: ")
    release_date = input("Enter the release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)
    os.system('clear')

def prompt_add_user():
    username = input("Enter new user name: ")
    database.add_user(username)
    os.system('clear')

def print_movie_list(heading, movies):
    os.system('clear')

    print(f"---- {heading} Movies ----")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{_id}: {title:15}  (on {human_date})")
    print("--------------------------- \n")

def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Enter movie id for the one you've watched: ")
    database.watch_movie(username, movie_id)
    os.system('clear')

def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movie(username)
    if movies:
        print_movie_list(f"Watched", movies)
    else:
        os.system('clear')
        print("That user has not watched a movie yet.\n")

os.system('clear')
print(welcome)
database.create_table()

user_input = input(menu)
while user_input != "7":
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
        prompt_show_watched_movies()
    elif (user_input == "6"):
        prompt_add_user()
    else:
        print("Invalid, please try again")

    user_input = input(menu)
