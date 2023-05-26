def printStocks(stocks):
    for a in stocks:
        val = 100 - ((a[2]/a[3])*100) # acho que isto n esta completamente correto
        print("{:5s} {:10s} {:7.2f} {:7.2f} {:7.0f} {:4.1f}".format(a[0],a[1],a[2],a[3],a[4],val))



# Cada tuplo = (empresa, cidade, abertura, fecho, volume)
stocks = [
    ('INTC', 'London', 34.249, 34.451, 1792860),
    ('TSLA', 'London', 221.33, 229.63, 398520),
    ('EA', 'Paris', 72.63, 68.98, 1189510),
    ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
    ('TSLA', 'Paris', 217.35, 217.75, 252500),
    ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
    ]

print("\na)")
printStocks(stocks)

print("\nb)")
stocks2 = sorted(sorted(stocks, key = lambda x:(x[-1]),reverse = True),key = lambda x:(x[0]))
printStocks(stocks2)

print("\nc)")
stocks3 = [tuplo for tuplo in stocks if tuplo[1] == "Paris" ]
printStocks(stocks3)
def load(nome):
    with open(nome) as ficheiro:
        lst = []
        for line in ficheiro:
            empresa, cidade, abertura, fecho, volume = line.split("\t")
            tuplo = empresa, cidade, float(abertura), float(fecho), int(volume)
            lst.append(tuplo)
    return lst
    
print("\nd)")
stocks4 = load("stocks.txt")
printStocks(stocks4)
# As condições seguintes devem ser verdadeiras
assert type(stocks4)==list
assert type(stocks4[0])==tuple
assert len(stocks4[0])==5
assert type(stocks4[0][2])==float
assert type(stocks4[0][4])==int
print("FIM")

