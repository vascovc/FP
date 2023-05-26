def compareFiles(file1,file2):
    with open(file1,"rb") as ficheiro1,open(file2,"rb") as ficheiro2:
        line1 = "something"
        while line1:
            line1 = ficheiro1.read(1024)
            line2 = ficheiro2.read(1024)
            if line1 != line2:
                return "Files are different"
        else:
            return "Files are the same"
            
assert compareFiles("nums.txt","nums.txt") == "Files are the same"
assert compareFiles("nums.txt","mystery.txt") == "Files are different"

"""
Abrem se os dois ficheiros como ficheiros binários e depois lêm se os bytes que
diz no enunciado para ler e então se eles forem diferentes acaba logo ali caso não 
o sejam então continua a tentar quando chegar ao fim do ficheiro vemos que a linha
e nula e então o while torna se falso e diz que os ficheiros são iguais, enquanto
que se forem diferentes acaba logo ali se forem iguais então tem que se ler todo até
ao fim
"""
