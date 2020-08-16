## Import libraries
import os
import sqlite3

## User Class
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        """
        Find a given user in the database for authentication
        :param username: String input of the username
        :return: User object, user, we will use for auth
        """
        print(os.getcwd())

        ## Setup Connection & Cursor
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        ## Find the user
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) ## Parameter must always be a tuple
        row = result.fetchone() ## Returns None if no results

        ## Create User object if we get data back
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        """
        Find a given user in the database for authentication
        :param id: INT input fo the user_id
        :return: User object, user, we will use for auth
        """
        ## Setup Connection & Cursor
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        ## Find the user
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  ## Parameter must always be a tuple
        row = result.fetchone()  ## Returns None if no results

        ## Create User object if we get data back
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user