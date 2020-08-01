##### *args Variable #####
## *args will allow a function to take in multiple unspecified arguments
## A tuple is capture when *args is supplied
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiply(2,3,5))

def apply(*args, operator): ## Operator argument stops *args collection
    if operator == "*":
        return multiply(*args) ## Pass the unpacked values to multiply
    elif operator == "+":
        return sum(args)
    else:
        return "No Valid Operator"

print(apply(1,3,6,7, operator="*"))

##### Destructure Arguments List #####
def add(x, y):
    return x + y

nums = [3, 5]
# add(nums) ## Error
## * will pass the nums variable to the two arguments
add(*nums) ## No Error

##### Destructure Arguments Dictionary  #####
nums = {"x": 15, "y": 25}
print(add(**nums)) ## ** for the dictionary

##### Unpacking Keyword Arguments #####
def named(**kwargs): ## Collect keyword arguments into a dict - Keys are name of keyword arg
    print(kwargs)