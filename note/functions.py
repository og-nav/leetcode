# BUILT-IN FUNCTIONS
"""
abs(x)
Return the absolute value of a number
print(abs(3 - 5))


all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty)
a = []
b = [1, 2, 3]
c = [1, 0, 3]
print(all(a), all(b), all(c)) -> True, True, False

any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False.






"""

# STRING FUNCTIONS
s = "abcdefg"
s.capitalize() # converts the first character to upper case
s.casefold() # converts a string to lower case
s.isalnum() # returns True if all characters in the string are alphanumeric
s.isalpha() # Returns True if all characters in the string are in the alphabet
s.isdigit() # Returns True if all characters in the string are digits
s.islower() # Returns True if all characters in the string are lower case
s.isnumeric() # Returns True if all characters in the string are numeric
s.isupper()	# Returns True if all characters in the string are upper case
s.lower() # Converts a string into lowercase
s.split(',') # Splits the string at separator, returns a list
s.upper() # Converts a string to upper case

# SET FUNCTIONS
visit = set()
visit2 = set()

visit.add(5) # add an element to the set
visit.clear() # remove all elements from the set
visit.copy() # returns a copy of the set
visit.discard(5) # removes an element, but does NOT throw an error if element does not exist in set
visit.intersection(visit2) # returns a set that is the intersection of two sets
visit.isdisjoint(visit2) # returns whether two sets have an intersection or not
visit.issubset(visit2) # returns whether another set contains this set or not
visit.issuperset(visit2) # returns whether this set contains another set or not
visit.remove(3) # removes an element, but throws an error if it does not exist

