length_pista=10 #milhas
tempo = 43.5#minutos
milha_km = 1.61

tempo_medio = (tempo/60)/(length_pista*milha_km)
velocidade = (length_pista*milha_km)/(tempo/60)
print("tempo medio:",tempo_medio,"velocidade",velocidade)