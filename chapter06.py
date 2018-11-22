#################################
# Chapter 6 #####################
#################################

"""
This chapter contains examples for the following things:
- Dictionaries
- Looping through dictionaries
- Nesting of dictionaries
"""

# 1. Dictionaries
#----------------

# simple dictionary
person0 = {
    'firstname': 'Klaus',
    'lastname': 'Mueller',
    'age': 22,
    'city': 'Berlin',
    }

print(person0)
print('\nFirstname: ' + person0['firstname'])
print('\nLastname: ' + person0['lastname'])
print('\nAge: ' + str(person0['age']))

# add key-value pairs
person0['sports'] = 'Football'
print(person0)

# change key-value pairs
person0['sports'] = 'Tennis'
print(person0)

# remove key-value pairs
del person0['sports']
print(person0)


# 2. Looping through a dictionary
#--------------------------------
fav_numbers = {
    'paul': 12,
    'chris': 4,
    'john': 20,
    'julia': 2,
    }

# to loop through python stores the key in var name and the value in var number
for name, number in fav_numbers.items():
    print('\nName: ' + name.title())
    print('number: ' + str(number))

# looping either only through keys or values
for number in fav_numbers.values():
    print(str(number))

if 'james' not in fav_numbers.keys():
    print('\nJames, please tell us about your favorite number')

# examples:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

participants = ['paul', 'jen', 'chris', 'julia', 'john', 'sarah']

for participant in participants:
    if participant in favorite_languages.keys():
        print('\nThanks you, ' + participant.title() + ' for your participation')
    else:
        print('\n' + participant.title() + ', please take part in the poll.')


# 3. Nesting
# ------------

# dictionaries inside of lists
persons = []
persons.append(person0)

person1 = {
    'firstname': 'Peter',
    'lastname': 'Kuhn',
    'age': 46,
    'city': 'Dortmund',
    }
persons.append(person1)

person2 = {
    'firstname': 'Clara',
    'lastname': 'Peters',
    'age': 32,
    'city': 'Karlsruhe',
    }
persons.append(person2)

for person in persons:
    print('\n' + person['firstname'] + ' ' + person['lastname'])
    print('\t' + str(person['age']))
    print('\t' + person['city'])

# lists inside of dictionaries
favorite_places = {
    'paul': ['Rome', 'Mailand', 'Madrid'],
    'simon': ['St. Petersburg', 'London'],
    'clara': ['Berlin'],
    }

for person, places in favorite_places.items():
    if len(places) > 1:
        print('\n' + person.title() + "'s favorite places are:")
        for place in places:
            print('\t' + place)
    else:
        print('\n' + person.title() + "'s favorite place is:")
        for place in places:
            print('\t' + place)

