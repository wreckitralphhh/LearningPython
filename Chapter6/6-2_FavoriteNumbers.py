# Use a dictionary to store people's favorite numbers
# Think of five names, and use them as keys in your dictionary
# Think of a favorite number for each person, and store each as a value in your dictionary
# Print each person's name and their favorite number

favorite_number = {'Jen': '1', 'Derrick': '2', 'Noel': '3', 'Eliza': '4', 'Anna': '5'}

for person in favorite_number:
    number = favorite_number[person]
    print(f"{person.title()}'s favorite number is {number}")


