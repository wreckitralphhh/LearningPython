# ToDo: Modify the program in exercise 6-2 so each person can have more than one favorite number
#   Then print each person's name along with their favorite numbers

favorite_numbers = {
    'jen': ['1', '10'],
    'derrick': ['9', '2'],
    'noel': ['3', '8'],
    'eliza': ['7', '6'],
    'anna': ['4', '5'],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for number in numbers:
          print(f"\t{number}")