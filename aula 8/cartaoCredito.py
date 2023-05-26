# 1. Função que remove carateres extra de um nº de cartão de crédito (CC).
#    Ex: 4388 5760 1840 2626 -> 4388576018402626
#        4388-5760-1840-2626 -> 4388576018402626
def limparCC(s):
	num = ""
	for a in s:
		if a.isdigit():
			num += a
	return num
"""
Vamos caracter a caracter e vemos se é um digito, se for entao adicionamos
a nossa string e depois devolvemo la
"""

# 2. Função p/ validar um nº de CC usando o algoritmo de Luhn.
#    Ex, para verificar se 4388 5760 1840 2626 é válido, deve:
# -> Somar dígitos nas posições pares (3+8+7+0+8+0+6+6) = 38
# -> Multiplicar os dígitos nas posições ímpares por dois 
#    (8, 16, 10, 12, 2, 8, 4, 4) e quando > 9 somar os dígitos 
#    (8, 7, 1, 3, 2, 8, 4, 4). Somar os 8 valores resultantes:  37
# -> Somar os valores obtidos nos passos anteriores: 37 + 38 = 75.
#    O número CC  é válido se o resultado final for múltiplo de 10. 

def validarCC(nCC):
	numero = limparCC(nCC)
	soma_pares = 0
	impares = ""
	soma_imp = 0
	val = 0
	for a in range(len(numero)):
		if a % 2 != 0:
			soma_pares += int(numero[a])
		else:
			impares += str(int(numero[a])*2)
			soma_imp += int(numero[a])*2
	if soma_imp > 9:
		for b in impares:
			val += int(b)
		soma_imp = val
	total = soma_imp + soma_pares
	if total % 10 == 0:
		return True
	else:
		return False
		
"""
Primeiro limpamos o numero para so termos os digitos
Os numeros que estavam nas posiçoes pares passaram a estar nas impares porque o for
vai começar a contagem em 0
Se for impar entao multiplica se por dois
Caso a soma das posiçoes impares seja maior que 9 entao somam se os digitos
(se um dos digitos for o 16 então faz se 1 + 6 = 7) ou seja podemos somar
todos os numeros da lista

Faz se entao o total e caso seja entao multiplo de 10 é valido
"""

# 3. Função ler ficheiro de texto com nºs de CC e devolver uma lista com 
#    Os nºs de CC válidos e outra lista com os inválidos. 
#    Os nºs de CC na lista dos válidos não devem ter carateres extra.
#    Passar o nome do ficheiro como parâmetro

def lerFicheiroCC(fname):
	val = []
	inval = []
	with open(fname) as ficheiro:
		for line in ficheiro:
			numero = limparCC(line)
			if validarCC(numero):
				val.append(numero)
			else :
				inval.append(numero)
	return val, inval

#~ print(limparCC('4388 5760 1840 2626'))
assert limparCC('4388-5760-1840-2626') == '4388576018402626'

#~ print(validarCC('4388 5760 1840 2626'))
#~ print(validarCC('4888 5760 1840 2626'))
assert validarCC('4388 5760 1840 2626') == False

validos, invalidos = lerFicheiroCC('cartoes.txt')
print(validos)
print(invalidos)
assert len(validos) == 4
assert len(invalidos) == 2

print('Sucesso!')
