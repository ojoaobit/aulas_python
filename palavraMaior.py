# VERIFICANDO QUAL PALAVRA E MAIOR
palavras = ["python", "html", "css", "js", "c"]

maiorPalavra = palavras[0]
menorPalavra = palavras[0]

for palavra in palavras:
  if len(palavra) > len(maiorPalavra):
    maiorPalavra = palavra
  if len(palavra) < len(menorPalavra):
    menorPalavra = palavra

    print(f"MAIOR PALAVRA: {maiorPalavra}")
    print(f"MENOR PALAVRA: {menorPalavra}")
