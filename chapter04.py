#################################
# Chapter 4 #####################
#################################

"""
This chapter contains examples for the following things:
- iteration with for loops over lists
- use of the range() function
- basic stats on lists, like min(), max() and sum()
- Working with slices of lists and copying
- Tuples
"""


# Iterate over list with for-loops
#---------------------------------
pizzas = ['funghi', 'pepperoni', 'cheese', 'anchovis', 'onion and tuna']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(pizza.title())

# range function
#---------------
# a. stores values 1 to 5
numbers = list(range(1,6))
print(numbers)

# b. steps of 3
numbers = list(range(2,10,3))
print(numbers)

# c. safe squares of number 1-11
squares = []
for value in range(1,12):
    squares.append(value**2)

print(squares)

# simple stats for lists
#-----------------------
numbers = list(range(1,1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Slicing and coopying list
#--------------------------

# Slice
print('\nThe first three items on Pizza list are:')
for pizza in pizzas[:3]:
    print(pizza.title())

# Copy list
# important: both point to the same list when just using equality
friends_pizzas = pizzas[:]
friends_pizzas.append('ham')
friends_pizzas.append('white')

print('\nFriends least favorite Pizzas:')
for pizza in friends_pizzas[4:]:
    print(pizza.title())

# Tuples
#--------
# important: values in a tuple can't be changed after creation
# but: the variable holding the tuple can be changed

# example: setting fixed dimensions for a rectangle
dimensions = (200,50)
print(dimensions[0])

for dimension in dimensions:
    print(dimension)








