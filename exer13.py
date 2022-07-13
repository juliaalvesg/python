# Exercicio(13) Criar uma funcionalidade que retorna a ultima index de um elemento dentro de uma tupla usando for bobões

# Foi criado uma tupla com series 
series = ("Stranger Things","The Umbrella Academy","Gambito da Rainha","Peaky Blinders","The Umbrella Academy")
# Delaracao do i para encontrar o indice do elemento que repete 
i = 0

# Foi criado uma estrutura de repeticao for para verificar se o elemento repete e imprimir para o usuario onden esta a posicao(indice) do ultimo elemento que repete
for serie in series:
    if series.count(serie)>1:
        posicao = i
    i += 1
print(f"A posicao em que se encontra o segundo elemento que esta repetindo e {posicao}")

