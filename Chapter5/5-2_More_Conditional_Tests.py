# Have at least one True and False result for each of the following:

# Tests for equality and inequality with strings
print("Tests for equality and inequality with strings")
player = 'Giannis'
print(player == 'Giannis')
print(player == 'Middleton')

# Tests using the lower() method
print("Tests using the lower() method")
car = 'Ferrari'
print(car.lower() == 'ferrari')
print(car.lower() == 'lamborghini')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print("Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to")
print(19 == 19)
print(19 > 18)
print(18 > 19)
print(28 >= 19)
print(28 <= 19)

# Tests using the and keyword and the or keyword
print("Tests using the and keyword and the or keyword")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

# Test whether an item is in a list
print("Test whether an item is in a list")
guest_list = ['ralph', 'charlotte', 'kayley', 'diana', 'brie']

print('ralph' in guest_list)
print('connor' in guest_list)

# Test whether an item is NOT in a list
print("Test whether an item is NOT in a list")
print('ralph' not in guest_list)
print('connor' not in guest_list)
