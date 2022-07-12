'''Exercício (11)
Simule uma tentativa de criar uma conta em uma plataforma digital
-O programa deve conferir se a conta do usuário que está sendo criado possui no mínimo 12 caracteres e tenha uma senha que possua de no mínimo 8 caracteres e caracteres numéricos 
-O programa também deve barrar a entrada de caracteres especiais na criação do nome de usuário
-O programa só deve criar a conta caso todas as condições tenham sido concluídas, se não o programa deve reiniciar voltando para o primeiro processo
-Quando a conta for criada o programa deve printar a frase: "conta criada!"'''

# Verificando a quantidade de caracteres da conta e da senha 

from curses.ascii import isalpha
from lzma import is_check_supported


while True:
    # Recebendo os acessos que o usuario esta criando para conta e senha
    conta = (input("Digite a conta que deseja criar ->"))
    senha = (input("Digite a senha que deseja criar ->"))

    if len(conta) < 12 or len(senha) < 8:
        print("Por favor digite uma senha e uma conta valida")
        continue

    elif not any(chr.isdigit() for chr in senha):
        print("A sua senha deve conter pelo menos um numero")
        continue

    elif not conta.isalpha():
        print("O nome do usuario nao deve conter caracteres especiais")
        continue 

    else:
        print("Conta criada, Parabens!!")
        break

