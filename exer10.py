'''Exercício (10)
Crie um jogo RPG por turnos de console
-O programa deve permitir o usuário à escolher entre dois personagens (mago ou guerreiro)
Caso o usuário escolha guerreiro o programa deve sortear um valor aleatório entre 5 e 10 que será a barra de poder do guerreiro 
Caso o usuário escolha mago o programa deve sortear um valor aleatório entre 7 e 15 que será a barra de poder do mago
-Dentro do jogo o usuário terá 4 opções:
Atacar (sorteia um valor de 3 a 10 de dano caso o usuário tenha escolhido guerreiro ou sorteia um valor entre 0 e 8 caso o usuário tenha escolhido um mago, 
independente do personagem escolhido o jogador gasta 2 de poder por ataque)
Defender (cancela 1 ataque do inimigo, caso o usuário seja um mago o jogador gasta 1 de poder de ataque), 
Curar (cura 1 de vida no caso do guerreiro e 2 de vida no caso do mago)
Descansar (sorteia um valor entre 1 e 5 e usa este valor para recuperar pontos de poder)
-Monstros
Os monstros são gerados com 20 de vida
Para atacar o monstro em seu turno escolhe aleatoriamente entre atacar dando 3 de dano ou se defender
Quando algum monstro é morto, o usuário tem a opção de sair do jogo ou continuar
Caso o usuário após matar um monstro queira continuar jogando, toda a sua vida é recuperada e o próximo monstro gerado terá 10 de vida e 3 de ataque a mais 
que o último e o jogador ganhará mais 3 de probabilidade de ataque e mais 5 de vida'''

import random 

# Permitindo que o usuario escolha entre dois personagens 
personagem = input("Escolha entre o personagem MAGO ou GUERREIRO -> ")

# Para o usuario saber que o jogo comecou sera printado na tela 
print("O JOGO FOI INICIADO")

vida_monstro = 20
ataque_inimigo = 10 

if personagem == "mago":
    poder_mago = random.randint(7,15)
    acao = input("Voce tera 4 opcoes: \n 1- Atacar \n 2- Defender \n 3- Curar \n 4- Descansar")
    if acao == "1":
        # Execucao caso o usuario escolha mago
        poder_final = poder_mago - 2
        dano_mago = random.randint(0,8)
    if acao == "2":
        ataque_inimigo = ataque_inimigo - 1
        poder_mago = poder_mago - 1
    if acao == "3":
        dano_mago = dano_mago - 2 
    if acao == "4":
        recuperacao = random.randint(1,5)
        porder_mago = poder_mago + recuperacao
    print(f"Ótima partida, até o momento voce está com {poder_final} de poder e {dano_mago} de danos")

if personagem == "guerreiro":
    poder_guerreiro = random.randint(5,10)
    dano_guerreiro = random.randint(3,10)
    acao = input("Voce tera 4 opcoes: \n 1- Atacar \n 2- Defender \n 3- Curar \n 4- Descansar")
    if acao == "1":
        # Execucao caso o usuario escolha guerreiro 
        if personagem == "guerreiro":
            poder_guerreiro = poder_guerreiro - 2 
    if acao == "2":
        ataque_inimigo = ataque_inimigo - 1 
    if acao == "3":
        dano_guerreiro = dano_guerreiro - 1
    if acao == "4":
        recuperacao = random.randint(1,5)
        poder_guerreiro = poder_guerreiro + recuperacao
    print(f"Ótima partida, até o momento voce está com {poder_guerreiro} de poder e {dano_guerreiro} de danos")

print("Monstros gerados!!")

while True:
    if vida_monstro > 0:
        acao_monstro = random.randint("Atacar","Defender")
        if acao_monstro == "Atacar":
            if personagem == "mago":
                dano_mago = dano_mago + 3
            else:
                dano_guerreiro = dano_guerreiro + 3 
        else: 
            vida_monstro = 20
    else: 
        i = input("O mostro morreu, deseja continuar ou sair do jogo? Aperte 2 para continuar e 2 para sair ->")
        if i == "1":
            break
        else:


