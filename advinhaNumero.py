import random

vidas = 5
sorteio = random.randint(1, 40)
sorteio = 9
print("------ADIVINHE O NÚMERO------\n")
print("O programa escolheu um número de 1 a 40!\n")

for vidas in range(5, 0, -1):
  numero = int(input("Digite um numero: "))

  if numero == sorteio:
    print("PARABENS, voce acertou o numero!")
    break
 
  elif numero < sorteio:
    print(f"O numero ta entre {numero +1} e {sorteio +2}")
  else:
     print(f"O numero ta entre 1 e {numero - 1}")
     print(f"Voce tem {vidas -1} vidas restantes\n")

else:
     print(f"FIM DO JOGO. Você não acertou. O número sorteado era {sorteio}!")