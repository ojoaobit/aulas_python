# saber se e maior de idade, menor ou idoso
idade = int(input("DIGITE SUA IDADE: "))

if idade >= 18 and idade <65:
    print("MAIOR DE IDADE")
elif idade >= 65:
    print("IDOSO")
else:
    print("MENOR DE IDADE")