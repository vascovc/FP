#Se sair de casa às 6:52 a passo e percorrer 1 km (ao ritmo de 10 min por km), depois fizer
#um treino rápido de 3km (a 6 min por km) e voltar a casa a passo, a que horas chego a
#casa para o pequeno almoço?
v1 = 1/10
v2 = 1/6
d1 = 1
d2 = 3
t1 = d1/v1
t2 = d2/v2
t3 = 4/v1
thoras = (t1+t2+t3+52)//60
th1 = thoras + 6
tminutos = (t1+t2+t3+52)%60
th1 = int(th1)
tminutos =int(tminutos)

print("Chega às: ",th1, ":",tminutos, "a casa para o pequeno almoço")
