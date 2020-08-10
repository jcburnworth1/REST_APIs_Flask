##### Decorators to easily modify functions #####
import functools

## Some guest user who cannot access the get_admin_password()
user = {"username": "jose",
        "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func) ## Will keep name and documentation of the passed function
        def secure_function(*args, **kwargs): ## Parameterize the decorator
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function
    return decorator

## Can protect a given call like this:
# if user["access_level"] == "admin":
#     print(get_admin_password())

## This is still not protected - Need to check function on call rather that at definition
# print(get_admin_password())

## This is now our secure decorator
# get_admin_password = make_secure(get_admin_password)
# print(get_admin_password())

##### At, @, syntax for decorators #####
@make_secure("admin") ## This syntax doe the same thing as line 25
def get_admin_password(): ## This function will no longer register as a function which can be an issue
    return "1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())