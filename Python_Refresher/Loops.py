##### While Loop #####
number = 7

while True:
    user_input = input('Would you would like to play (Y/n): ').lower()
    if user_input == 'n':
        break

    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    elif abs(number - user_number) == 1:
        print('You were off by one.')
    else:
        print('Sorry, it is wrong.')

##### For Loop #####
friends = ['Bob', 'Rolf', 'Anne', 'Jen']

for friend in friends:
    print(f'{friend} is my friend.')

## Average grade example - Example only, can just use average
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)