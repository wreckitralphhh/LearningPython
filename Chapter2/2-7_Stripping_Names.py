# use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure to use each character combination "\t" and "\n" at lease once
# print the name once, so the whitespace around the name is displayed
# then print the name using each of the three stripping functions

name = "Ralph"
nametab = "\tRalph"
namenewline = "\nRalph"
nameboth = "\n\tRalph"
print(name)
print(nametab)
print(namenewline)
print(nameboth)

namewhitespace = "\tRalph\t"
print(namewhitespace)
print(namewhitespace.rstrip())
print(namewhitespace.lstrip())
print(namewhitespace.strip())