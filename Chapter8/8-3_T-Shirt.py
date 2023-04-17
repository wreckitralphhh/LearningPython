# ToDo: Write a function called 'make_shirt()' that accepts size and the text of a message that should be printed on the shirt
#   The function should print a sentence summarizing the size of the shirt and the message printed on it.
#   Call the function once using positional arguments to make a shirt
#   Call the function again using keyword arguments


def make_shirt(shirt_size, message):
    print(f"This shirt is size {shirt_size} and will have {message} written on it")


make_shirt('L', 'Have a nice day!')

make_shirt(shirt_size='L', message='Have a nice day!')
    