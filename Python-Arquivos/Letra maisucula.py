def letra(n):
    if 1 <= n <= 26:
        return chr(64 + n) # chr transforma o número no iten correspondente da tabela unicode
                                     # letras 64 pois as letras maisuculas começam no 64
