
# Define the function containsDoubles here,
# so that it passes all the tests below.
...


# Test function
assert containsDoubles("pool") == True
assert containsDoubles("polo") == False
assert containsDoubles("erro") == True
assert containsDoubles("connosco") == True
assert containsDoubles("banana") == False
# Add a few more tests below
...

# If the program reaches this point...
print("All tests passed!")


# This function should read lines from the given file
# and return a list of lines that contain doubles (consecutive repeated chars).
def findLinesWithDoubles(fname):
    ...

# Program:

# This should show a list of all English words with double letters.
lst = findLinesWithDoubles("/usr/share/dict/words")
print(lst)

# You may download files with Portuguese words from:
# http://natura.di.uminho.pt/download/sources/Dictionaries/wordlists/LATEST/
# But you may need to open them with the argument: encoding="latin1".

