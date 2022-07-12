'''Exercício (5)
Escreva um programa que leia os catetos oposto e adjacente de um triângulo e calcule a hipotenusa
'''

# Recebendo os valores do cateto oposto e do cateto adjacente inserido pelo usuario 
cateto_oposto = int(input("Digite o valor do cateto oposto -> "))
cateto_adjacente = int(input("Digite o valor do cateto adjacente -> "))

# Realizando o calculo da hipotenusa 
hipotenusa = ((cateto_oposto)** 2 + (cateto_adjacente)** 2)

# Retorno para o usuario 
print(f"O valor da hipotenusa e {hipotenusa}")


