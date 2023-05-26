def primesUpTo(n):
    nums = range(2,n+1)
    primes = [a for a in nums if a not in [b for c in nums for b in nums if c != b and b%c==0]]
    return primes
"""
Tem-se todos os numeros até ao valor pretendido e depois vamos retirar.
Vamos ter depois duas listas, a mais à direita, cria uma em que temos os multiplos
de cada numero, tirando o multiplo por 1, daí a diferença, mas para ser multiplo então
a divisão dá resto 0.
Depois só queremos os valores que não estiverem nessa lista

Se mesmo assim a explicação não servir
https://wiki.portugal-a-programar.pt/algoritmo:crivo_de_eratosthenes

http://pythontutor.com/live.html#code=def%20primesUpTo%28n%29%3A%0A%20%20%20%20nums%20%3D%20range%282,n%2B1%29%0A%20%20%20%20primes%20%3D%20%5Ba%20for%20a%20in%20nums%20if%20a%20not%20in%20%5Bb%20for%20c%20in%20nums%20for%20b%20in%20nums%20if%20c%20!%3D%20b%20and%20b%25c%3D%3D0%5D%5D%0A%20%20%20%20return%20primes%0A%0Aprint%28primesUpTo%2810%29%29&cumulative=false&curInstr=856&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""
print(primesUpTo(100))
