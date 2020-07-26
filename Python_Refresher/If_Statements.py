##### If statements #####
day_of_week = input('What day of the week is it today?')

## Check Monday
# print(day_of_week == 'Monday')

if day_of_week == 'Monday':
    print('Have a great start to your week!')
elif day_of_week == 'Tuesday':
    print('It is Tuesday!')
else:
    print('Full speed ahead!')

print('This always runs.')

##### The 'in' keyword #####
friends = ['Rolf', 'Bob', 'Jen']
print('Jen' in friends) # True

movies_watched = {'The Matrix', 'Green Book', 'Hei'}
user_movie = input('Enter something you have watched recently: ')
print(user_movie in movies_watched)

##### If statements with 'in' #####
if user_movie in movies_watched:
    print(f'I have watched {user_movie} too!')
else:
    print(f'I have not watched {user_movie} yet.')

##### Magic Number Game #####
number = 7
user_input = input('Enter (y) if you would like to play: ').lower()

if user_input == 'y':
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    else:
        print('Sorry, it is wrong.')