# Nothing here yet!

CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movie (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES = ("INSERT INTO movies (title, release_timestamp, watched)"
  "VALUES (?, ?, 0);")

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM moives WHERE watched = 1;"

