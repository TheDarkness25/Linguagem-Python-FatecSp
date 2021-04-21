n1 = int(input('n1: '))
n2 = int(input('n2: '))
op = input('Operador: ')
if op == '+':
    print('{} {} {} = {}' .format(n1, op, n2, (n1+n2)))
elif op == '-':
    print('{} {} {} = {}' .format(n1, op, n2, (n1-n2)))
elif op == '*':
    print('{} {} {} = {}' .format(n1, op, n2, (n1*n2)))
elif n2 == 0:
    print('Divisão por zero!!!!!')
else:
    print('{} {} {} = {}' .format(n1, op, n2, (n1/n2)))
    
