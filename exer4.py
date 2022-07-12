'''Exercício (4)
Escreva um programa que leia um valor em reais e passe para dólares'''

# Recebendo o valor em reais digitado pelo usuario 
reais = float(input("Digite o valor em reais que quer saber convertido para dolar ->"))

# Convertendo o valor em reais para dolares 
valor_convertido = reais * 5.42

# Retornando o valor para o usuarios 
print(f"O valor em dolares e ${valor_convertido}")