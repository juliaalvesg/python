'''Exercício (2)
 O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
 Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, 
 escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

Recebendo o custo de fabrica, descrito pelo usuario'''
custo_fabrica = float(input("Por favor digite o valor do custo de fabrica ->"))

porcentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45 

# Realizando o calculo para saber quanto sera retornado para o usuario 
total = porcentagem_distribuidor + impostos + custo_fabrica

# Retorno para o usuario 
print(f"O valor total que o usuario tera que pagar e R${total}")
