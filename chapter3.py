guests = ['thomas', 'christina', 'paula', 'klaus']
for guest in guests:
    print(guest + ', you are invited to a great party')

print(guests[2])

guests[2] = 'tina'
for guest in guests:
    print(guest + ', you are invited to a great party')

print('Hey everyone, I found a bigger table :-)')

guests.insert(0, 'Dieter')
guests.insert(3, 'Fiona')
guests.append('Fernando')

for guest in guests:
    print(guest + ", bigger table, you're in!")

print('Sorry guys, my new table did not arrive')

uninvited = guests.pop()
print(uninvited + ', sorry!')
uninvited = guests.pop()
print(uninvited + ', sorry!')
uninvited = guests.pop()
print(uninvited + ', sorry!')
uninvited = guests.pop()
print(uninvited + ', sorry!')
uninvited = guests.pop()
print(uninvited + ', sorry!')

del guests[0]
del guests[0]

print(guests)



