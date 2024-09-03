#calcular idade
anoAtual = 2024
cidade = input("Digite sua cidade: ").upper()
anoNascimento = int(input("Digite ano que nasceu: "))
idade = anoAtual - anoNascimento

print(f"Voce mora em: {cidade} e tem {idade} anos")