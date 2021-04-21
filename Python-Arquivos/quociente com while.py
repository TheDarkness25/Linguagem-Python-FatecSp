n1 = int(input('n1: '))
n2 = int(input('n2: '))
q = 0
while n1 >= n2:
    n1 -= n2
    q += 1
print('O quociente dessa divisão é igual a: ', q)
