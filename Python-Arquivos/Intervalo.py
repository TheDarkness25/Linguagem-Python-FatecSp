a = int(input('a: '))
b = int(input('b: '))
x = int(input('x: '))
if a <= x <= b:
    print('{} esta entre o intervalo [{}, {}]' .format(x, a, b))
    if x - a < b - x:
        print('{} esta mais próximo de {}' .format(x, a))
    else:
        print('{} esta mais próximo de {}' .format(x, b))
else:
    print('{} não pertence ao intervalo de [{}, {}]' .format(x, a, b)) 
