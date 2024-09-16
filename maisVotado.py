votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]
# iniciando lista vazia
contagem_votos = {}

for produto in votos:
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(contagem_votos)