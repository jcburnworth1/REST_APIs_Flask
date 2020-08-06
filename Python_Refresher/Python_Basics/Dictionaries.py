##### Dictionaries #####
## Key Value Pairs - {key: value}
## Keys must be hashable types - int or strings

## Basics
friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}
print(friend_ages['Rolf'])

## Adding element to dict
friend_ages['Adam'] = 31
print(friend_ages)

## Changing element
friend_ages['Adam'] = 32

##### List of Dicts #####
## Must now used indexes to print a given dict
friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27}
]

##### Looping Dicts #####
student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

## Looping syntax
## This prints keys only
for student in student_attendance:
    print(student)

## This prints student and attendance percentage
## This works but isn't ideal
for student in student_attendance:
    print(f'{student}: {student_attendance[student]}%')

## This is ideal by using .items()
for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}%')

##### Dicts & in function #####
## Cannot check if value is in a dict, keys only
if 'Bob' in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")

##### Return values only #####
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))