#imprime items das chaves e puxa valor de cada item
# chaves: items/elementos iniciais ex> nome: (sem string)
# valor: valor de cada item da lista
pessoa = {"nome": "joao", "idade": 30, "cidade": "sao paulo"}
#atribui item "nome": com valor "joao" por exemplo
for chave, valor in pessoa.items(): #chave foi criada pra puxar todos os items da mesma
#valor e o item criado pra sequencia pessoa
#pessoa recebe o metodo .items() pra puxar valor de cada item
    print(f"{chave}: {valor}") #imprimo chave: pra que o valor que vai ser puxado a seguir, tenha : antes dele