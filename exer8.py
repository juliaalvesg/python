# Exercício (8)
# Use a estrutura de loop for para que o programa retorne todos números pares de 0 até um número especificado por terminal

# Recebendo um numero especifico que sera inserido pelo usuario 
num = int(input("Por favor digite um numero ->"))

# Utiliza-se o range para criar um array onde inicia no zero e finaliza no numero depois do digitado pelo usuario
numeros = range(0,num + 1)

# Foi criado o laco de repeticao for e verificado se o numero e impar ou par 
for numeros in numeros:
    if numeros % 2 == 0:
        print(numeros)