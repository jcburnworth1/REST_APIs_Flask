##### First Class Functions Example #####
## Functions that are just variables
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

## Use calculate function with divide
## Example Only - Issue is that divide only take two positional args
output = calculate(10, 5, operator=divide)

