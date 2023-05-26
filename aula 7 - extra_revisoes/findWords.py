
# This function reads a file and returns a list with every line stripped.
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst


def filterPattern(lst, pattern):
    ...


# matchesPattern should return True iff string s matches the given pattern.
# Each ? in pattern should match any character in the same position in s.
# Other characters must match exactly, but case-insensitive.
def matchesPattern(s, pattern):
    ...


# Uncomment these lines to test the matchesPattern function:
#assert matchesPattern("secret", "s?c??t") == True
#assert matchesPattern("socket", "s?c??t") == True
#assert matchesPattern("soccer", "s?c??t") == False
#assert matchesPattern("SEcrEt", "?ecr?t") == True, "should be case-insensitive"


def main():
    englishWords = load("/usr/share/dict/words")

    lst = filterPattern(englishWords, "s?c??t")
    print(lst)

    assert isinstance(lst, list),  "result lst should be a list"
    assert "secret" in lst,  "result should contain 'secret'"

    # Solution to "?YS???Y"
    lst = filterPattern(englishWords, "?ys???y")
    print(lst)


# Call main function:
main()

