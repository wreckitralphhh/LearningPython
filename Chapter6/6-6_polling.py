# Use the same code as 'favorite_languages.py'
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'anna': 'matlab',
    'kiana': 'r',
    'eric': 'ruby',
}

# ToDo: Make a list of people who should take the favorite languages poll. Include some names that are already in the dicitonary and some that are not
should_take_poll = ['ralph', 'brian', 'kiana', 'sarah', 'anna']

# ToDo: Loop thru the list of ppl who should take the poll. If they already took it, print a msg thanking them. If they haven't taken the poll, print a msg inviting them to take the poll
for person in should_take_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll {person.title()}!")
    else:
        print(f"Fuck you {person.title()}, take the goddamned poll")

