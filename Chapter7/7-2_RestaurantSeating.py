# ToDo: Write a progam that asks the user how many people are in their dinner group
#   If the answer is more than eight, print a message saying they'll have to wait for a table
#   Otherwise, report that their table is ready

party_size = input("Hi welcome to Olive Garden! How many in your party? ")
party_size = int(party_size)

if party_size >= 8:
    print("\nThanks, we'll have a table ready for you soon.")
else:
    print("Great! Please follow me to your tab10le!")