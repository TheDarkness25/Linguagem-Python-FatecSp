x = input('Caractere: ')
if x == '0' or x == '2' or x == '4' or x == '6' or x == '8':
    print('{} é um dígito par' .format(x))
elif x == '1' or x == '3' or x == '5' or x == '7' or x == '9':
    print('{} é um dígito ímpar'.format(x))
elif x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print('{} é uma letra vogal minúscula' .format(x))
elif 'a' <= x <= 'z' and(x!='a' and x!='e' and x!='i' and x!='o' and x!='u'):
    print('{} é uma letra consoante minúscula' .format(x))
elif x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
    print('{} é uma letra vogal maiúscula' .format(x))
else:
    print('{} é uma letra consoante maiúscula' .format(x))

    
    
