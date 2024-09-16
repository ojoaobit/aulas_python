def indice_do_alfabeto(indice):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= indice <= 26:
        return alfabeto[indice - 1]
    else:
        return ''

print(indice_do_alfabeto(1))
print(indice_do_alfabeto(3))
print(indice_do_alfabeto(26)) # letra z