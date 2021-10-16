# Think of five locations in the world you'd like to visit
# Store the locations in a list. Make sure the list is not alphabetical order
places = ['new york', 'austin', 'los angeles', 'boston', 'miami']
# Print your list in original order
print("Places I would like to visit")
print(places)
# Use sorted() to print your list in alphabetical order without modifying the actual list
print("\nAlphabetical order list")
print(sorted(places))
# Show that your list is still in its original order by printing it
print("\nOriginal list order")
print(places)
# Use sorted() to print the list in reverse alphabetical order without changing original list
print("\nReverse order")
print(sorted(places, reverse=True))
# Show that your list is still in its original order by printing it
print("\nOriginal list order")
print(places)
# Use reverse() to change the order of the list --> print it
print("\nPermanent reverse order:")
places.reverse()
print(places)
# Use reverse() to change it back to original order --> print it
print("\nBring back to original order:")
places.reverse()
print(places)
# Use sort() to change list and to store it in alphabetical order --> print it
print("\nPermanent alphabetical order:")
places.sort()
print(places)
# Use sort() to change list and store it in reverse alphabetical order --> print it
print("\nPermanent reverse alphabetical order:")
places.sort(reverse=True)
print(places)

