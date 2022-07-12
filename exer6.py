'''Exercício (6)
Crie um programa que peça ao usuário um número, e retorne todos os múltiplos do número escolhido pelo usuário de 1 a 10'''

# Recebendo um numero escolhido pelo usuario 
from audioop import mul


num = int(input("Por favor difite um numero que deseja saber os multiplos->"))
x = 1

# Calculando os multiplos 
while True:
    multiplos = num * x 
    print(f"{multiplos}")
    x += 1 

    if x > 10 :
        break


