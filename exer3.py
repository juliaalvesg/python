'''Exercício (3)
Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.'''

# Recebendo os valores inseridos pelo usuario 
eleitores = int(input("Por favor digite a quantidade de eleitores do seu municipio ->"))
votos_brancos = int(input("Por favor digite a quantidade de votos brancos do seu municipio ->"))
votos_nulos = int(input("Por favor digite a quantidade de votos nulos do seu municipio ->"))
votos_validos = int(input("Por favor digite a quantidade de votos validos do seu municipio ->"))

# Fazendo o calculo da porcentagem de cada setor 
porcentagem_brancos = (votos_brancos * 100)/eleitores
porcentagem_nulos = (votos_nulos * 100)/eleitores
porcentagem_validos = (votos_validos * 100)/eleitores

# Retorno para o usuario 
print(f"A poncentagem de votos brancos e {porcentagem_brancos}%")
print(f"A poncentagem de votos nulos e {porcentagem_nulos}%")
print(f"A poncentagem de votos validos e {porcentagem_validos}%")
