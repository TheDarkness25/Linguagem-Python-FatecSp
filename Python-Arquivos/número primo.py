n = int(input('n: '))
cont = 0
for i in range(1, n+1):
    if n % i ==0:
        cont += 1
if cont == 2:
    print('O número {} é primo!' .format(n))
else:
    print('O número {} não é primo!'.format(n))
    
        
