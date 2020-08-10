##### Errors in Python #####
## Basic Error Handling
def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") ## Raise the error
    return dividend / divisor


grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
else:
    print(f"There average grades is {average}.")
finally:
    print("Thank you!")

## More Advance Error Handling
students = [
    {"name": "Bob", "grades": [75,90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100,90]}]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} average {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades.")
else:
    print("-- All student averages calculated --")
finally:
    print("Thank You!")