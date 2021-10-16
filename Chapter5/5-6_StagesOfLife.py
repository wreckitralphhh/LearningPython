# Write and if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
age = 65

# If a person is less than 2 years old, print a message that the person is a baby
if age < 2:
    print("You are a baby")
# If a person is at least 2 years old but less than 4, print a message that the person is a toddler
elif age < 4:
    print("You're a toddler")
# If a person is at least 4 years old but less than 13, print a message that the person is a kid
elif age < 13:
    print("You're a kid")
# If a person is at least 13 years old but less than 20, print a message that the person is a teenager
elif age < 20:
    print("You're a teenager")
# If a person is at least 20 years old but less than 65, print a message that the person is a adult
elif age < 65:
    print("You're an adult")
# If a person is age 65 or older, print a message that the person is a elder
elif age >= 65:
    print("You old AF!!")
