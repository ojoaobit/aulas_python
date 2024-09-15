def verificar_palindromo(palavra):
    palavra_limpa = palavra.replace(" ", "").lower()
    # Verifica se a palavra é igual à sua inversa
    return palavra_limpa == palavra_limpa[::-1]

palavra = input("Digite uma palvara: ")
if verificar_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
