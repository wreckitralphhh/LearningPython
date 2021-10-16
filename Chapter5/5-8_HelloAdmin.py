# Make a list of five or more usernames, including the name 'admin'
# Imagine you're writing code that will print a greeting to each user after they log into a website
# Loop through the list, and print a greeting to each user

usernames = ['admin', 'coffeezilla', 'noelmiller', 'codyko', 'jarvisjohnson']
# empty list for 5-9
#usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
