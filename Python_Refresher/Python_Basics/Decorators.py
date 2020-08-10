##### Decorators to easily modify functions #####
## Some guest user who cannot access the get_admin_password()
user = {"username": "jose",
        "access_level": "guest"}

## This should be restricted to admins only but nothing prevents that currently
def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function

## Can protect a given call like this:
# if user["access_level"] == "admin":
#     print(get_admin_password())

## This is still not protected - Need to check function on call rather that at definition
# print(get_admin_password())

## This is now our secure decorator
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())