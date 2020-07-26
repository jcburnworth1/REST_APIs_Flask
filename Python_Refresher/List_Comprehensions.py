##### Basic List Comprehension #####
## Integers
numbers = [1,2,3,4,5]
doubled = [num * 2 for num in numbers]

## Text
friends = ['Rolf', 'Sam', 'Samantha', 'Jen']
starts_s = [friend for friend in friends if friend[0].lower() == 's']