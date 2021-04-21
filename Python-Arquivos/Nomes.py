n1 = input('Nome: ')
n2 = input('Nome: ')
if n1 == n2:
    print('Os nomes são iguais')
else:
    if n1 < n2:
        print('{}\n{}' .format(n1, n2))
    else:
        print('{}\n{}' .format(n2, n1))
