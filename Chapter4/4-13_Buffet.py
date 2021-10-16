# Think of five simple foods, and store them in a tuple
foods = ('pizza', 'burger', 'soup', 'steak', 'mac and cheese')
print('Old menu:')
# Use a for loop to print each food the restaurant offers
for food in foods:
    print(food)
# Try to modify one of the items, and make sure that Python rejects the change
#foods[2] = 'salad'
# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a
# for loop to print each of the items on the revised menu
foods = ('pizza', 'taco', 'chowder', 'steak','mac and cheese')
print('\nNew menu:')
for food in foods:
    print(food)