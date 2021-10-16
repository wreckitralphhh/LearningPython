# 3-4
# Make a list that includes at least 3 people you would invite to your wedding
# Use the list to print a message to each person inviting them to your wedding

guests = ['steph curry', 'elon musk', 'jeff bezos']
print(f"Hey {guests[0].title()}, you're invited to my wedding!")
print(f"Hey {guests[1].title()}, you're invited to my wedding!")
print(f"Hey {guests[2].title()}, you're invited to my wedding!")

# 3-5: It seems like a guest can't make it
# (A) Start with a print call stating the name of the guest who can't make it
# (B) Modify your list, replace the name of the guest who can't make it with someone else
# (C) Print a second set of invitations

#(A)
wont_attend = guests.pop()
print(f"Oh no! It seems like {wont_attend.title()} can't make it!")
#(B)
guests.append('bill gates')
#(C)
print(f"Hey {guests[0].title()}, you're invited to my wedding!")
print(f"Hey {guests[1].title()}, you're invited to my wedding!")
print(f"Hey {guests[2].title()}, you're invited to my wedding!")

# 3-6: More space is available at the wedding, so you need to add 3 more guests to the list
# (A)Use insert() to add one new guest to the beginning of the list
# (B)Use insert() to add one new guest the middle of the list
# (C)Use append() to add one new guest to the end of the list

#(A)
guests.insert(0,'Kwame Brown')
#(B)
guests.insert(2,'Dad')
#(C)
guests.append('Mom')
# Check the guest list
print(guests)
# Printing an invitation to each person
print(f"Hey {guests[0].title()}, you're invited to my wedding!")
print(f"Hey {guests[1].title()}, you're invited to my wedding!")
print(f"Hey {guests[2].title()}, you're invited to my wedding!")
print(f"Hey {guests[3].title()}, you're invited to my wedding!")
print(f"Hey {guests[4].title()}, you're invited to my wedding!")
print(f"Hey {guests[5].title()}, you're invited to my wedding!")

# 3-7
# (A) Start with list from 3-6, print a message saying you can only invite two people to dinner
# (B) Use pop() to remove guests, print a message letting them know you can't invite them to dinner
# (C) Print a message to each of the two people still on the list, letting them know they're still invited
# (D) Use del to remove the last two names, print the list to check that it's actually empty

print("I can only invite two people to dinner")
# pop everyone besides Mom & Dad
uninvite1 = guests.pop(0)
uninvite2 = guests.pop(1)
uninvite3 = guests.pop(3)

# message to let them know you can't invite them to dinner
print(f"I'm sorry {uninvite1.title()}, but you can't come to dinner")
print(f"I'm sorry {uninvite2.title()}, but you can't come to dinner")
print(f"I'm sorry {uninvite3.title()}, but you can't come to dinner")
#print(f"I'm sorry {uninvite4.title()}, but you can't come to dinner")

# This is tricky because it shifts the index of each value of the array. So, be very careful and make sure to note how the indices shift


