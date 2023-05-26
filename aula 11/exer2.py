
# Generates all length-3 words with symbols taken from the given alphabet.
def genWords3(symbols):
    return [ x+y+z for x in symbols for y in symbols for z in symbols ]


# Generates all length-n words with symbols taken from the given alphabet.
def genWords(symbols, n):
    if n==0:
        return [""]
    lst1 = genWords(symbols,n-1)
    return [ n+c for n in lst1 for c in symbols]
"""
http://pythontutor.com/live.html#code=%0Adef%20genWords%28symbols,%20n%29%3A%0A%20%20%20%20if%20n%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%20%5B%22%22%5D%0A%20%20%20%20lst1%20%3D%20genWords%28symbols,n-1%29%0A%20%20%20%20return%20%5B%20n%2Bc%20for%20n%20in%20lst1%20for%20c%20in%20symbols%5D%0A%0AlstB%20%3D%20genWords%28%22abc%22,%203%29%20%20%23%20should%20return%20the%20same%20words,%20maybe%20in%20other%20order%0Aprint%28lstB%29&cumulative=false&curInstr=83&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""
lstA = genWords3("abc")
print(lstA)

lstB = genWords("abc", 3)  # should return the same words, maybe in other order
print(lstB)
assert sorted(lstA) == sorted(lstB)

lstC = genWords("01", 4)  # should return all length-4 binary words
print(lstC)

