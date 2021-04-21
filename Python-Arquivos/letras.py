c = input ('Caractere: ')
if  'a'<=c<='z' or 'A'<=c<='Z' :
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
       c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        print('vogal')
    else:
        print('consoante')
else:
    print('Esse caractere (%s) não é uma letra!' %c)
    
