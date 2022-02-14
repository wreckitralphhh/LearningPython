# ToDo: Ask the user for a number, then report whether the number is a multiple of 10 or not

number = input("Enter a number, and I'll tell you if it's divisible by 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is divisible by 10.")
else:
    print(f"\nThe number {number} isn't divisible by 10.")