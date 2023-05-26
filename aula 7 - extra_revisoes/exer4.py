
# This function reads a file and returns a list with every line stripped.
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst

def filterPattern(lst, pattern):
    listafinal = []
    for a in lst:
        if len(a) == len(pattern):
            if matchesPattern(a,pattern):
                listafinal.append(a)
    return listafinal

"""
Aqui a funçao vai ver cada palavra e ve se alguma delas corresponde ao padrao.
Mas para que isso aconteça a palavra da lista e o padrao tem que ter o mesmo
numero de caracteres, se esse for o caso entao adicionamos a uma lista e depois 
ela e devolvida
"""

# matchesPattern should return True if string s matches the given pattern.
# Each ? in pattern should match any character in the same position in s.
# Other characters must match exactly, but case-insensitive.
def matchesPattern(s, pattern):
    for x in range(len(s)):
        if s[x].lower() != pattern[x]:
            if pattern[x] != "?":
                return False
    else:
        return True
"""
primeiro ler bem o enunciado, apenas se o caracter for diferente de um ? ou da
propria letra é que é problema, tanto seja minuscula como maiuscula

Entao temos uma string, e vamos analisar caracter a caracter, converte-se para
minuscula por causa do ultimo assert que assim já nao chateia. Entao se esse
caracter for diferente daquele que é a palavra já temos que nos preocupar.
No entanto só é falso se no padrao esse caracter for diferente de um ?
"""
            

# Uncomment these lines to test the matchesPattern function:
assert matchesPattern("secret", "s?c??t") == True
assert matchesPattern("socket", "s?c??t") == True
assert matchesPattern("soccer", "s?c??t") == False
assert matchesPattern("SEcrEt", "?ecr?t") == True, "should be case-insensitive"


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

