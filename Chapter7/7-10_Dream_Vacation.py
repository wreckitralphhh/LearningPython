# ToDo: Write a program that polls users about their dream vacation
#   Write a prompt similar to 'If you could visit one place in the world, where would you go?'
#   Include a block of code that prints the results of the poll

responses = {}

# Set a flatg to indicate that the polling is active
polling_active = True

while polling_active:
    user = input("What is your name?")
    response = input("If you could visit one place in the world, where would you go?")

    responses[user] = response

    repeat = input("Would you like the other person to respond? (Y/N)")
    if repeat == 'N':
        polling_active = False

# Print poll results
for user, response in responses.items():
    print(f"{user.title()} would like to go to {response.title()}.")

