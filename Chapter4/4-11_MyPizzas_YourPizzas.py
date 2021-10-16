# Make a copy of the list of pizzas, and call it friend_pizzas then do the following:
pizzas = ['pepperoni','meat lovers','combo','magherita','hawaiian']
friend_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append('neopolitan')
# Add a different pizza to the friend_pizzas list
friend_pizzas.append('cheese')

# Prove that both lists are separate
print(pizzas)
print(friend_pizzas)

# Final output
print("My favorite pizzas are: ")
for val in pizzas:
    print(val)
print("My friend's favorite pizzas are: ")
for val in friend_pizzas:
    print(val)