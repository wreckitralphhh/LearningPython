# Create a program that simulates how websites ensure that everyone has a unique username

# Make a list of five or more usernames called current_users
current_users = ['drewgooden', 'coffeezilla', 'noelmiller', 'codyko', 'jarvisjohnson']

# Make another list called new_users
new_users = ['jontron', 'codyko', 'noelmiller', 'dannygonzalez', 'bermpeak']

# Loop thru new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username
# If a username has not been used, print a message saying that the username is available

# make sure its case insensitive so "John" and "JOHN" can't be two different usernames
current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]

for new_user in new_users:
    if new_user in current_users:
        print("Sorry that username is taken, enter a new username")
    else:
        print(f"Welcome {new_user}!")
