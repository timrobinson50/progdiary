import sqlite3
import datetime

CREATE_MOVIES_TABLE = """
    --sql
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
    );
"""

CREATE_USERS_TABLE = """
    --sql
    CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
    );
"""

CREATE_WATCHED_TABLE = """
    --sql
    CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
    );
"""

INSERT_MOVIES = """
    --sql
    INSERT INTO movies (title, release_timestamp) VALUES (?, ?);
"""

INSERT_USER = """
    --sql
    INSERT INTO users (username) VALUES (?);
"""

DELETE_MOVIE = """
    --sql
    DELETE FROM movies where title = ?;
"""
SELECT_ALL_MOVIES = """
    --sql
    SELECT * FROM movies;
"""
SELECT_UPCOMING_MOVIES = """
    --sql
    SELECT * FROM movies WHERE release_timestamp > ?;
"""
SELECT_WATCHED_MOVIES = """
    --sql
    SELECT movies.* 
    FROM movies
    JOIN watched ON movies.id = watched.movie_id
    JOIN users ON users.username = watched.user_username
    WHERE users.username = ?;
"""
INSERT_WATCHED_MOVIE = """
    --sql
    INSERT INTO watched (user_username, movie_id) VALUES (?, ?);
    """
SET_MOVIE_WATCHED = """
    --sql
    UPDATE movies SET watched = 1 WHERE title = ?;
"""

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

def add_user(username):
    with connection:
        connection.execute(
            INSERT_USER, (username,))
            
def add_movie(title, release_timestamp):
    with connection:
        connection.execute(
            INSERT_MOVIES, (title, release_timestamp,))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
    return cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id,))

def get_watched_movie(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
    return cursor.fetchall()