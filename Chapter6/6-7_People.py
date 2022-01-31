# Use the program you wrote for Exercise 6-1
# ToDo: Make two new dictionaries representing different people, and store all three dictionaries in a list called 'people'

person_1 = {'first_name': 'Paul', 'last_name': 'Pierce', 'age': '34', 'city': 'Boston'}
person_2 = {'first_name': 'Ray', 'last_name': 'Allen', 'age': '20', 'city': 'Seattle'}
person_3 = {'first_name': 'Kevin', 'last_name': 'Garnett', 'age': '21', 'city': 'Minnesota'}

people = [person_1, person_2, person_3]

# ToDo: Loop thru the list, printing everything you know about that person
for person in people:
    print(person)
