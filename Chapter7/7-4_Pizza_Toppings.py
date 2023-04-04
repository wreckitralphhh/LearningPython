#ToDo: Write a loop that prompts the user to enter a series o pizza toppings until they hear a 'quit' value. As the enter each topping, print a message saying you'll add that topping to their pizza

prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        print("Thanks!")
        break
    else:
        print(f"We'll add {topping.lower()} to your pizza")