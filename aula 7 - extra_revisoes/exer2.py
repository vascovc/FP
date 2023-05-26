
# Define the function containsDoubles here,
# so that it passes all the tests below.
def containsDoubles(palavra):
    for a in range(1,len(palavra)):
        if palavra[a] == palavra[a-1]:
            return True
    else:
        return False
"""Este programa pega então num caracter e verifica se é igual ao anterior,
se for então devolve True se isso n acontecer devolve falso, o porque de começar o
range no 1 é porque se fosse no 0 então iria ver o ultimo caracter o que se enontra na
posição -1 e isso não se quer veja-se o ultimo assert antes do print"""

# Test function
assert containsDoubles("pool") == True
assert containsDoubles("polo") == False
assert containsDoubles("erro") == True
assert containsDoubles("connosco") == True
assert containsDoubles("banana") == False
# more tests
assert containsDoubles("mississipi") == True
assert containsDoubles("arvore") == False
assert containsDoubles("anana") == False

print("All tests passed!")

#3########

# This function should read lines from the given file
# and return a list of lines that contain doubles (consecutive repeated chars).
def findLinesWithDoubles(fname):
    with open(fname, "r", encoding='ISO-8859-1') as ficheiro:
        palavras = []
        for l in ficheiro:
            linha = ficheiro.readline()
            lst = ""
            for c in linha:
                if c in lst:
                    palavras.append(linha)
                    break
                lst += c
        return palavras
"""Este programa vai ler o ficheiro linha por linha e converte para uma string
e ent temos uma lista para onde meter as palavras que queremos, depois lemos linha
a linha o ficheiro e vemos cada palavra uma a uma, se a letra já la estiver ent acabamos por
aí e adicionamos à lista se n\ao estiver ent adicionamos essa letra à string que vai percorrer
a palavra que deixa ver se a letra já la esta"""

###Program:

# This should show a list of all English words with double letters.
lst = findLinesWithDoubles("wordlist-ao-latest.txt")
print(lst)
