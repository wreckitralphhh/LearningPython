# A number raised to the third power is called a cube
# Make a list of the first 10 cubes (the cube of each integer from 1 thru 10)
# Use a for loop to print the numbers

# Start with an empty list
cubes = []
# For loop 1 --> 10
for value in range(1,11):
    # Each value is cubed and appended to the empty list "cubes"
    cubes.append(value**3)
print(cubes)

# List comprehension version
cubes2 = [num**3 for num in range(1,11)]
print(cubes2)