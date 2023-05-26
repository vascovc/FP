# A set of functions to deal with bags of money.
# JMR 2017
# Face values of coins (in cents):
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def value(bag):
    valor = 0
    for moeda in bag:
        dinheiro = moeda
        quantidade = bag[moeda]
        valor += quantidade * dinheiro
    return valor
"""
Temos entao a soma como sendo zero e vamos percorrer cada um dos valores
das moedas e ver quantas sao e adicionar ao total
"""

def transfer1coin(bag1, c, bag2):
    """Try to transfer one coin of value c from bag1 to bag2.
    If possible, transfer coin and return True, otherwise return False."""
    if bag1[c] != 0:
        bag1[c] -= 1
        if c in bag2:
            bag2[c] += 1
        else:
            bag2[c] = 1
        return True
    else:
        return False
"""
Se o valor na cartareia1 existir, ou seja e diferente de 0 entao tiramos de la
1 moeda, caso ja estejam na carteira2 mais valores como esse entao acrescentamos 1
caso n estejam passa a estar 1
"""

def transfer(bag1, amount, bag2): #ESTA FUNÇAO ESTA A DAR ERRADA, NO SITE DO PYTHONTUTOR FUNCIONA PARA O PRIMEIRO MAS PARA O SEGUNDO NEM TANTO
    """Try to transfer an amount from bag1 to bag2.
    If possible, transfer coins and return True,
    otherwise, return False and leave bags with same values."""
    if amount == 0:
        return True
    if value(bag1) < amount:
        return False
    for valor in bag1:
        if valor not in bag2:
            bag2[valor] = 0
        for numero in range(bag1[valor]):
            if amount > 0:
                transfer1coin(bag1,valor,bag2)
                amount -= valor
            if amount == 0:
                return True
    if amount < 0:
        for valor in bag2:
            for numero in range(bag2[valor]):
                transfer1coin(bag2,valor,bag1)
                amount += valor
                if amount == 0:
                    return True
        
    

"""
Se a transferencia for de zero entao e possivel
Mas se se vir que a transferencia e maior que o valor que se encontra
no saco entao podemos acabar logo ai

ESTA FUNÇAO NAO E A MELHOR NO ENTANTO ESTA A FUNCIONAR MAIS OU MENOS, NO ENTANTO TEM DEMASIADOS CILCLOS

Mesmo assim o que aqui acontece e que vamos ver cada moeda do saco 1 e vemos se existem moedas dessas
no saco 2 se nao existirem cria se com o valor 0. Depois vamos ao numero de moedas que ha no saco 1
e usamos a funcao que ciramos antes para fazer a transferencia mas so se o montante for positivo, se for
zero entao maravilha acabamos ai o trabalho, ate se podem trocar os if que torna se uma programaçao mais
correta porque obtem se logo a resposta por assim dizer. No final o que pode acontecer e termos passado
dinheiro a mais para o saco 2 assim o montante sera negativo e voltamos a passa lo para o saco 1, a mesma
logica de como fizemos antes.

O porque de o montante passado ser mais do que o que devia deve se ao facto de a ordem de moedas nao ser
a mais eficaz, pela propria natureza, tem que se fazer a combinaçao delas. mais facil de ver aqui 

http://pythontutor.com/live.html#code=def%20value%28bag%29%3A%0A%20%20%20%20valor%20%3D%200%0A%20%20%20%20for%20moeda%20in%20bag%3A%0A%20%20%20%20%20%20%20%20dinheiro%20%3D%20moeda%0A%20%20%20%20%20%20%20%20quantidade%20%3D%20bag%5Bmoeda%5D%0A%20%20%20%20%20%20%20%20valor%20%2B%3D%20quantidade%20*%20dinheiro%0A%20%20%20%20return%20valor%0A%0Adef%20transfer1coin%28bag1,%20c,%20bag2%29%3A%0A%20%20%20%20%22%22%22Try%20to%20transfer%20one%20coin%20of%20value%20c%20from%20bag1%20to%20bag2.%0A%20%20%20%20If%20possible,%20transfer%20coin%20and%20return%20True,%20otherwise%20return%20False.%22%22%22%0A%20%20%20%20if%20bag1%5Bc%5D%20!%3D%200%3A%0A%20%20%20%20%20%20%20%20bag1%5Bc%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20if%20c%20in%20bag2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20bag2%5Bc%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20bag2%5Bc%5D%20%3D%201%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%0Adef%20transfer%28bag1,%20amount,%20bag2%29%3A%20%23ESTA%20FUN%C3%87AO%20ESTA%20A%20DAR%20ERRADA,%20NO%20SITE%20DO%20PYTHONTUTOR%20FUNCIONA%20PARA%20O%20PRIMEIRO%20MAS%20PARA%20O%20SEGUNDO%20NEM%20TANTO%0A%20%20%20%20%22%22%22Try%20to%20transfer%20an%20amount%20from%20bag1%20to%20bag2.%0A%20%20%20%20If%20possible,%20transfer%20coins%20and%20return%20True,%0A%20%20%20%20otherwise,%20return%20False%20and%20leave%20bags%20with%20same%20values.%22%22%22%0A%20%20%20%20if%20amount%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20if%20value%28bag1%29%20%3C%20amount%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20for%20valor%20in%20bag1%3A%0A%20%20%20%20%20%20%20%20if%20valor%20not%20in%20bag2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20bag2%5Bvalor%5D%20%3D%200%0A%20%20%20%20%20%20%20%20for%20numero%20in%20range%28bag1%5Bvalor%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20amount%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20transfer1coin%28bag1,valor,bag2%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20amount%20-%3D%20valor%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20amount%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20if%20amount%20%3C%200%3A%0A%20%20%20%20%20%20%20%20for%20valor%20in%20bag2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20numero%20in%20range%28bag2%5Bvalor%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20transfer1coin%28bag2,valor,bag1%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20amount%20%2B%3D%20valor%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20amount%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%0Adef%20strbag%28bag%29%3A%0A%20%20%20%20%22%22%22Return%20a%20string%20representing%20the%20contents%20of%20a%20bag.%22%22%22%20%0A%20%20%20%20%23%20You%20may%20want%20to%20change%20this%20to%20produce%20a%20more%20user-friendly%0A%20%20%20%20%23%20representation%20such%20as%20%224x200%2B3x50%2B1x5%2B3x1%3D958%22.%0A%20%20%20%20valor%20%3D%200%0A%20%20%20%20representacao%20%3D%20%22%22%0A%20%20%20%20for%20moeda%20in%20bag%3A%0A%20%20%20%20%20%20%20%20dinheiro%20%3D%20moeda%0A%20%20%20%20%20%20%20%20representacao%20%2B%3D%20str%28moeda%29%20%2B%20%22x%22%0A%20%20%20%20%20%20%20%20quantidade%20%3D%20bag%5Bmoeda%5D%0A%20%20%20%20%20%20%20%20representacao%20%2B%3D%20str%28quantidade%29%20%2B%20%22%2B%22%0A%20%20%20%20%20%20%20%20valor%20%2B%3D%20quantidade%20*%20dinheiro%0A%20%20%20%20representacao%20%3D%20representacao%5B%3A-1%5D%20%2B%20%22%3D%22%20%2B%20str%28valor%29%0A%20%20%20%20return%20representacao%0A%0Adef%20main%28%29%3A%0A%20%20%20%20%0A%20%20%20%20bag1%20%3D%20%7B1%3A%204,%202%3A%200,%205%3A1,%2010%3A%200,%2020%3A%205,%2050%3A%204,%20100%3A%202,%20200%3A%201%7D%20%23%20serve%20so%20para%20irmos%20mantendo%20os%20valores%20dos%20dicionarios%20porque%20eles%20foram%20alterados%20antes%0A%20%20%20%20bag2%20%3D%20%7B%7D%0A%0A%20%20%20%20print%28transfer%28bag1,%20157,%20bag2%29%29%20%20%20%20%20%20%20%20%23%20True%20%28should%20be%20easy%29%0A%20%20%20%20print%28%22bag1%3A%22,%20strbag%28bag1%29%29%20%20%20%20%23%20bag1%3A%201x200%2B1x100%2B3x50%2B3x20%2B2x1%3D512%20%20%20%20%20%20%20%20%20EU%20ACHO%20QUE%20ESTE%20VALOR%20ESTA%20ERRADO%20QUE%20FAZENDO%20AS%20CONTAS%20709-157%20DA%20552%20NAO%20512%0A%20%20%20%20print%28%22bag2%3A%22,%20strbag%28bag2%29%29%20%20%20%20%23%20bag2%3A%201x100%2B1x50%2B2x20%2B1x5%2B2x1%3D197%20%20%20%20%20%20%20%20%20%20%20ASSIM%20COMO%200%20MAIS%20157%20DA%20157%20NAO%20197%0A%20%20%20%20%0A%20%20%20%20bag1%20%3D%20%7B1%3A%204,%202%3A%200,%205%3A1,%2010%3A%200,%2020%3A%205,%2050%3A%204,%20100%3A%202,%20200%3A%201%7D%20%23%20serve%20so%20para%20irmos%20mantendo%20os%20valores%20dos%20dicionarios%20porque%20eles%20foram%20alterados%20antes%0A%20%20%20%20bag2%20%3D%20%7B%7D%0A%0A%20%20%20%20print%28transfer%28bag1,%2060,%20bag2%29%29%20%23%20not%20easy,%20but%20possible...%0A%20%20%20%20print%28%22bag1%3A%22,%20strbag%28bag1%29%29%0A%20%20%20%20print%28%22bag2%3A%22,%20strbag%28bag2%29%29%0A%0Amain%28%29%0A%0A%0A&cumulative=false&curInstr=746&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Agora pensando bem, caso tivessemos criado uma lista a partir do dicionario e tivessemos
posto a andar dos valores maiores para os menores isto talvez ficasse mais facil, simples e correto
"""

def strbag(bag):
    """Return a string representing the contents of a bag.""" 
    # You may want to change this to produce a more user-friendly
    # representation such as "4x200+3x50+1x5+3x1=958".
    valor = 0
    representacao = ""
    for moeda in bag:
        dinheiro = moeda
        representacao += str(moeda) + "x"
        quantidade = bag[moeda]
        representacao += str(quantidade) + "+"
        valor += quantidade * dinheiro
    representacao = representacao[:-1] + "=" + str(valor)
    return representacao
"""
vamos a cada moeda do saco e vemos o seu valor e entao juntamos a nossa string
o valor dessa moeda e o sinal para mostrar que vamos fazer a multiplicaçao.
Depois vemos quantas vezes ela aparece e entao juntamos esse numero a string
pomos entao o sinal mais porque ja acabamos com esse item do dicionario e temoa
que passar ao proximo
no fim juntamos o valor
"""

def main():
    # A bag of coins is represented by a dict of {coin: number} items
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1}
    bag2 = {}

    # Test the value function.
    assert value({}) == 0
    assert value({1:7, 5:2, 20:4, 100:1}) == 197

    # Test the strbag function.
    print( strbag({1:7, 5:2, 20:4, 100:1}) )        # 1x100+4x20+2x5+7x1=197
    print( strbag({1:7, 5:2, 10:0, 20:4, 100:1}) )  # 1x100+4x20+2x5+7x1=197

    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0
    
    print(transfer1coin(bag1, 10, bag2))    # False!
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+4x20+1x5+4x1=689
    print("bag2:", strbag(bag2))    # bag2: 1x20=20

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+3x20+1x5+4x1=669
    print("bag2:", strbag(bag2))    # bag2: 2x20=40
    
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1} # serve so para irmos mantendo os valores dos dicionarios porque eles foram alterados antes
    bag2 = {}

    print(transfer(bag1, 157, bag2))        # True (should be easy)
    print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512         EU ACHO QUE ESTE VALOR ESTA ERRADO QUE FAZENDO AS CONTAS 709-157 DA 552 NAO 512
    print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197           ASSIM COMO 0 MAIS 157 DA 157 NAO 197
    
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1} # serve so para irmos mantendo os valores dos dicionarios porque eles foram alterados antes
    bag2 = {}

    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

main()


