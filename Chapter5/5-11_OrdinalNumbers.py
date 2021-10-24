# Store numbers 1 thru 9 in a list
# Use if-elif-else chain inside the loop to print the proper ordinal ending for each number "1st 2nd 3rd ... 9th"
numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")


