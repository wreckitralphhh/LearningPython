# make a dictionary containing three major rivers and the country each reiver runs through. One key-value pair might be 'nile' : 'egypt'
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yangtze': 'china',
}

# Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt'
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
