#ToDo: Write a loop in which the ask users their age, and then tell the cost of their movie ticket
#   If person is age < 3, ticket is free
#   If 3 < age < 12, ticket is $10
#   If age > 12, ticket is $15

prompt = "\nHow old are you?:"

while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("\nOk, your ticket is free today")
    if (age >= 3) and (age <= 12):
        print("\nOk, you ticket is $10 today")
    if age > 12:
        print("\nOk, you ticket is $15 today")