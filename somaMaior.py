# ATIVIDADE 1 - SOMAR E DIZER QUAL NUMERO E MAIOR
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
