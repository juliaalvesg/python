'''Exercício (7)
Use a estrutura de loop para que o programa retorne todos os múltiplos de 6 de 0 a 500.'''

x = 1 

# Resolvendo os multiplos de 6
while True:
    multiplos = x * 6 
    x += 1 

    # Fazendo um filtro para exibir apenas os multiplos de 6 
    if 0 < multiplos and multiplos < 500:
        print(multiplos)
        continue

    