n = int(input('Número: '))
x = 0
for i in range(n+1):
    x += i
    i += 1
    if x != 0:
        print('/{}/' .format(x), end= ' ')
    
    
    
