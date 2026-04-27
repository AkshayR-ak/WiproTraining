#Day 2

#1. List

print('-------------List--------------')
fruits = ['apple','orange','pear','apple','banana']
print('List of fruits: ', fruits)

fruits.append('grapes')
fruits.append('pineapple')
fruits.remove('apple')
print('After append and remove: ', fruits)

print('Second fruit is ', fruits[1],' and fourth fruit is ',fruits[3])

print('Slicing first three fruits: ', fruits[0:3])

print('Length of the fruits list is: ', len(fruits))

#2. Tuple

print('-------------Tuple--------------')
cities1 = ('Chennai','Bangalore','Coimbatore')
print('Tuple of cities: ', cities1)

print('Printing first and last element in Tuple: ', cities1[0],' ',cities1[-1])

cities2 = ('Delhi','Mumbai')
all_cities = cities1 + cities2
print('After Concatenate two Tuples: ', all_cities)

try:
    all_cities[2] = ('Kolkata')  # tuple don't support
except TypeError as e:
    print(e)

city1, city2, city3, city4, city5 = all_cities
print('After changing Tuple into seperate variables: ')
print(city1, city2, city3, city4, city5)

#3. Set

print('-------------Set--------------')
colors1 = {'red','green','blue','yellow','pink'}
print('Set of colors: ',colors1)

colors1.add('white')
print('After adding an element: ', colors1)

colors1.remove('yellow')
print('After removing an element: ', colors1)

colors2 = {'black','green','purple'}

print('Intersection: ',colors1.intersection(colors2))
print('Union: ',colors1.union(colors2))
print('Difference: ',colors1.difference(colors2))

print('Is it there? ','white' in colors1)

fruits.append('banana') #to check duplicate
print('Adding duplicate element in List to check with Set: ', fruits)
set_fruits = set(fruits)
print('After changing List to Set:', set_fruits)

#4. Dictionary

print('-------------Dictionary--------------')
data = {
    'name' : 'John Snow',
    'age' : 23,
    'favorite_hobby' : 'Sword Fighting'
}
print('Data in Dictionary: ',data)

print('Name in Data: ',data['name'])

data['favorite_food'] = 'Vegetable stew'
print('Favorite food in Data: ' ,data['favorite_food'])

data['favorite_hobby'] = 'Coding'
print('Updated favorite hobby: ',data['favorite_hobby'])

print('Keys in Data: ', data.keys())

print('Values in Data: ', data.values())

del data['age']
print('Data in Dictionary after removing age:' ,data)