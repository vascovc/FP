def genFibonacci(n):
    """Generate list of first n Fibonacci numbers: [F0, F1, ... Fn-1]."""
    lst = [0,1]
    a = lst[0]
    b = lst[1]
    soma=0
    if n <= 2:
        return lst
    else:
        for i in range (2,n):
            soma = a + b
            a = b
            b = soma
            lst.append(soma)
        return lst
"""Então começamos com aqueles dois valores da lista, coisa que também se altera,
sabemos que uma seuqencia destas e gerada atraves de recorrência, com os elementos
anteriores e em vez de termos a fazer por recorrencia que demora mais e gasta mais 
recursos aproveitamos e vamos fazendo a soma e depois alteramos as variáveis para que 
estas passem a ser as anteriores e depois adiciona-se à lista

O segredo passa por ao termo atual -2 se atribuir o valor de n-1 e ao valor que
era n-1 passa a ter o valor de n e assim sucessivamente
Exemplo: o quinto elemento é dado pela soma do terceiro elemento com o quarto elemento
        lst[5] = lst[4] + lst[3] isto é um erro escrever assim mas torna a compreensão
        mais acessivel
""" 


def main():
    # Do tests:
    lst = genFibonacci(10)
    print(lst)      #-> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Check the results we expect.
    # (If a condition fails, the assert statement raises an AssertionError!)

    assert isinstance(lst, list), "lst should be a list"
    assert lst == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert genFibonacci(2) == [0, 1]
    assert genFibonacci(6) == [0, 1, 1, 2, 3, 5]

    # If the program reaches this point...
    print("All tests passed!")

    # Let the user try it:
    n = int(input("N? "))
    print("genFibonacci({}) -> {}".format(n, genFibonacci(n)))


# Call main function:
main()

