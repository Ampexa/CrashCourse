#################################
# Chapter 5 #####################
#################################

"""
This chapter contains examples for the following things:
- conditional statements (incl. case sensitivity)
- if-statements:


"""
# Conditional tests
#-------------------

# example case sensitivity
car = "Audi"
print(car == "audi")
print(car.lower() == "audi")

# multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

# checking for a value in a list
list1 = ['cheese', 'pepperoni', 'onions']
print('cheese' in list1)
print('salad' in list1)

if 'salad' not in list1:
    print('Not in list')

# if-statements
#---------------

alien_color1 = 'green'
alien_color2 = 'yellow'
alien_color3 = 'red'

if alien_color2 == 'green':
    print('5 points')
else:
    print('10 pints')

if alien_color1 == 'green':
    print('5 points')
else:
    print('10 pints')

# if-elif-else chain
if alien_color3 == 'green':
    print('5 points')
elif alien_color3 == 'yellow':
    print('10 pints')
else:
    print('15 points')


# check if a list is empty before using it
users = ['admin', 'christina', 'frank', 'paul', 'simon']

#test if list is empty
if users:
    # loop over users
    for user in users:
        # print different statement for admin
        if user == 'admin':
            print('Hello ' + user.title() + ', do you want a report?')
        else:
            print('Hello ' + user.title())
else:
    print('There are no users')

new_users = ['john', 'maria', 'peter', 'paul', 'julia']

for user in new_users:
    if user in users:
        print('Sorry ' + user + ', this name is already taken')
    else:
        print('Your chosen username is available.')


# if statement for all options:
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in list2:
    if number == 1:
        print(str(number) + 'st')
    if number == 2:
        print(str(number) + 'nd')
    if number == 3:
        print(str(number) + 'rd')
    if number >= 4:
        print(str(number) + 'th')