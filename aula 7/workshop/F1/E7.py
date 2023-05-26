media_secundario = float(input("media do secundario: "))
fq = float(input("nota no exame de fisico-quimica: "))
matematica = float(input("nota no exame de matematica: "))

media_final = media_secundario*0.5 + fq*0.25 + matematica*0.25
print("media final: ",media_final)