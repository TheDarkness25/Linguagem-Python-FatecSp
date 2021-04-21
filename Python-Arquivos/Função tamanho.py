def tamanho(n):
    cont = 0
    while n > 0:
        n = n // 10
        cont += 1
    return cont
