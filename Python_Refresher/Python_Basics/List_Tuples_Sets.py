##### List - Define by square brackets #####
## Most standard
## Can be modified
## Keep the order
list = ['Bob', 'Rolf', 'Anne']

## Add an item
list.append('Smith')

## Remove an item
list.remove('Smith')

##### Tuple - Cannot add or remove elements #####
## Cannot be modified
## Keep the order
tuple = ('Bob', 'Rolf', 'Anne')

##### Set - Can add or remove elements but cannot have dupes #####
## Does not keep order
## Not subscriptable
set = {'Bob', 'Rolf', 'Anne'}

## Add item to set
set.add('Smith')

##### Advanced Set Operations #####
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

## Using functions to operate on sets
## Calculate Difference
local_friends = friends.difference(abroad)

## Union two sets
friends = local_friends.union(abroad)

##### More Set Operations #####
art = {'Bob','Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)

