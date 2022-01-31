# Todo: make a dictionary called 'favorite_places'
#   Think of three names to use as keys in the dictionary, and store one to three favorite places
#   Ask some friends to name their favorite places. Loop thru the dictionary and print each person's name and their favorite places

favorite_places = {
    'ralph': ['san francisco', 'toronto'],
    'vlad': ['moscow', 'miami'],
    'jenna': ['vancouver', 'los angeles'],
    'sarah': ['new york', 'las vegas'],
    'ashley': ['seattle', 'tokyo'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
          print(f"\t{place.title()}")