##### Example - sqlite3 Interactions #####
## Import libraries
import sqlite3

## Initialize a connection
connection = sqlite3.connect('Proper_REST_API_SQL_DB/data.db') ## sqltite3 database file: Proper_REST_API_SQL_DB/data.db
cursor = connection.cursor() ## Will execute queries

## Create the users table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

## Insert a record into the users table
user1 = (1, 'bob', 'asdf') ## Tuple
insert_query = "INSERT INTO users VALUES (id, username, password)"
cursor.execute(insert_query, user1)
