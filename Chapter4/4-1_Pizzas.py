# Think of 5 kinds of your favorite pizza, store these in a list and use a for loop to print the name of each pizza
pizzas = ['pepperoni', 'four cheese', "meat lover's", 'combo', 'hawaiian']
for pizza in pizzas:
    print(pizza.title())

# Modify this list to print a simple statement "I like ... pizza"
for pizza in pizzas:
    print(f"\nI like {pizza} pizza!")

print("\nI really love pizza!")