'''Exercício (9)
Simule um radar de rodovia 
Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
-O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa deve indicar que a velocidade não foi fornecida
-Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o usuário deve mudar de mão
-Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor dessa multa o excesso de velocidade * 7
-Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a mecânica acima com o numero sorteado'''

#  Importando um modulo de numeros aleatorios 
import random 

# Captando a velocidade inserida pelo usuario
velocidade = input("Digite a velocidade do carro->")

# Validando se a velocidade que o usuario inserio nao esta em branco 
if velocidade == '':
    print("A velocidade nao foi fornecida")
    num = random.randint(1,120)
    if num > 90:
        valor_excesso = int(velocidade) - 90 
        multa = valor_excesso * 7 
        print(f"Voce tomou uma multa de R${multa}, por excesso de velocidade")
    elif velocidade < 30:
        print("Voce deve mudar de mao")

# Verificando se a velocidade fornecida pelo usuario esta abaixo do minimo 
elif int(velocidade) < 30:
    print("Voce deve mudar de mao")

# Se a velocidade foi acima de 90, estou aplicando a multa
elif int(velocidade) > 90:
    valor_excesso = velocidade - 90 
    multa = valor_excesso * 7 
    print(f"Voce tomou uma multa de R${multa}, por excesso de velocidade")

    
    

