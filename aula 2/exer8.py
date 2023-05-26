pf=20
pc=24.95
imp=23
spa=0.20
lucro = (pc - spa) / ( 1 + imp / 100) - pf
impostos = (pc-spa)/(pf+lucro) 								# sem a certeza de estar certo
taxas = spa
print("O lucro da livraria é de: ",lucro*500)
print("O valor coletado em impostos é de: ",impostos*500)
print("A quantia de taxas recolhida foi de: ",taxas*500)
