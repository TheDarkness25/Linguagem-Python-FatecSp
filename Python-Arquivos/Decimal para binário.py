n = int(input('n: '))
cont = 1
b = 0
while(n / 2 > 0):
    r = n - (n // 2) * 2
    b = r * cont + b
    cont *= 10
    n = n // 2
print(b)

    
