acu = 0
cont = 0
x = float(input('Valor: '))
while x != 11.0:
    acu += x
    cont += 1
    x = float(input('Valor: '))
print('A média é: {:.2f}'.format((acu/cont)))
