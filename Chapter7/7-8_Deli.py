# ToDo: make a list called 'sandwich_orders' and fill it with the names of various sandiches. Then make an empty list called 'finished_sandwiches'
#   Loop through the list of sandwich orders and print a message for each order, such as 'I made your tuna sandwich.'
#   As each sandwich is made, move it to the list of finished sandiwiches
#   After all the sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = ['grilled cheese', 'ham and turkey', 'philly cheesesteak', 'BLT']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order.title()}.")
    finished_sandwiches.append(order)

# print(finished_sandwiches)

print("\nHere are the sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())


