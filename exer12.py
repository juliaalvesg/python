# Exercício (12)
# Crie um script que receba 6 números e retorne quais são os números pares e quais são os ímpares

# Foi criado um array para receber os numeros digitados pelo usuario
array_par = []
array_impares = []

# Foi criado um laco de repeticao para verificar se os elementos digitados pelo usuario sao pares 
for i in range(0,6): 
    numero = int(input("Por favor digite um numero->"))
    if numero % 2 == 0:
         array_par.append(numero)
    
    else:
        array_impares.append(numero)

# Retorna para o usuario apenas os valores pares 
print(f"Numeros pares: {array_par}")
print(f"Numeros impares: {array_impares}")