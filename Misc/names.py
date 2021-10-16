# Makes the proper capitalizations for a name
name = "ada lovelace"
print(name.title())

# Methods that caps lock, and lower case lock
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# using f-string to compose full message
print(f"Hello, {full_name.title()}!")
# f-strings inside a variable
message = f"Hello, {full_name.title()}!"
print(message)


















