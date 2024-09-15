def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in vogais:
            contador += 1
    
    return contador

palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra}' contém {contar_vogais(palavra)} vogais.")
