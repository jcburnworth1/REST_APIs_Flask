## File will help with proper authentication
## Import libraries
from Proper_REST_API_SQL_DB.user import User
from werkzeug.security import safe_str_cmp ## Safe string comparison

## Setup users table
users = [
    User(1, 'bob', 'asdf'),
    User(2, 'jc', 'lala')
]

## These will allow us to quickly find a user based on name or id rather than looping every user
username_mapping = {u.username: u for u in users}
userid_mapping =  {u.id: u for u in users}

## Authenticate Function
def authenticate(username, password):
    """
    Simple method to find user data rather than looping
    :param username: The user's login
    :param password: The user's password
    :return: user object if found, None if not found
    """
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Simple method to find user data rather than looping
    :param payload:
    :return: user object if found, None if not found
    """
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
