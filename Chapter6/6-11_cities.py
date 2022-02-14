# ToDo: make a dictionary called 'cities'
#   use the names of three cities as keys in your dictionary
#   create a dictionary of information about each city and about that city
#   the keys for each city's dictionary should be something like 'country', 'population', and 'fact'
#   print the name of each city and all of the information you have stored about it

cities = {
    'new york city': {
        'state': 'new york',
        'population': '8.8 million',
        'fact': "It's home to the second highest number of billionaires of any city in the world"
    },

    'los angeles': {
        'state': 'california',
        'population': '3.9 million',
        'fact': "Hosted the 1932 and 1984 Summer Olympic games"
    },

    'chicago': {
        'state': 'illinois',
        'population': '2.7 million',
        'fact': "O'Hare International Airport is one of the busiest airports in the world"
    },

}

for city, city_info in cities.items():
    print(f"\n {city.title()}")
    state = city_info['state']
    pop = city_info['population']
    fact = city_info['fact']

    print(f"\tState: {state.title()}")
    print(f"\tPopulation: {pop.title()}")
    print(f"\tFact: {fact}")

