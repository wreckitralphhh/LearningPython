# ToDo: sign the list 'sandwich_orders' in the previous exercise, make sure the sandwich 'pastrami' appears in the list at least three times
#   Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while lop to remove all occurrences of 'pastrami' from 'sandwich_orders'
#   Make sure no pastrami sandwiches end up in 'finished_sandwiches'

sandwich_orders = ['grilled cheese', 'pastrami', 'ham and turkey', 'pastrami', 'philly cheesesteak', 'pastrami', 'BLT']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Sorry we're out of Pastrami")
while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)

print("\nHere are the sandwiches made: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())

