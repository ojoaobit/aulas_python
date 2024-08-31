# atribuindo novo valor a mesma variavel
'''
nome = 'Joao'
print(f"NOME INICIAL:{nome} ")

Nome = 'Victor'
print(f"NOME ATUAL: {Nome}")
'''

# verificando se numero e par ou impar
'''
numero = int(input("DIGITE UM NUMERO INTEIRO: "))
if numero % 2 == 0:
    print("NUMERO PAR")
else:
    print("NUMERO IMPAR")
'''

# concatenando nomes
'''
nome = input("DIGITE SEU NOME: ")
sobrenome = input("DIGITE SEU SOBRENOME: ")
concatenacao = nome + ' ' + sobrenome
print(f"NOME COMPLETO: {concatenacao}")
'''

# saber se e maior de idade, menor ou idoso
'''
idade = int(input("DIGITE SUA IDADE: "))

if idade >= 18 and idade <65:
    print("MAIOR DE IDADE")
elif idade >= 65:
    print("IDOSO")
else:
    print("MENOR DE IDADE")
'''

#calcular idade
'''
anoAtual = 2024
cidade = input("Digite sua cidade: ").upper()
anoNascimento = int(input("Digite ano que nasceu: "))
idade = anoAtual - anoNascimento

print(f"Voce mora em: {cidade} e tem {idade} anos")
'''

# ATIVIDADE 1 - SOMAR E DIZER QUAL NUMERO E MAIOR
'''
num1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
num2 = int(input("DIGITE O SEGUNDO NUMERO: "))
soma = num1 + num2

if num1 > num2:
    print(f"O NUMERO {num1} E MAIOR QUE {num2}")
elif num2 > num1:
     print(f"O NUMERO {num2} E MAIOR QUE {num1}")
else:
     print(f"OS VALORES {num1} E {num2} SAO IGUAIS")

print(f"\nA SOMA DOS VALORES: {soma}")
'''

#

