def mdc(a,b):
    if a <= b:
      r = a
      b = a
      a = b
    r = a%b	
    if r == 0:
      return b
    else:
      mdc(b,r)

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
print("O menor divisor comum entre",a,"e",b,"é",mdc(a,b))
