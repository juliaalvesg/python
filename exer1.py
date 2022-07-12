'''Exercício (1)
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.'''


'''Criando variaveis para receber os dados do aniversario do usuario '''
meses = int(input("Por favor digite sua idade em meses ->"))
anos = int(input("Por favor digite sua idade em anos ->"))
dias = int(input("Por favor digite sua idade em dias ->"))

'''Calculos para verificar qual sera a idade em dias'''
niver_mes = meses * 30
niver_anos = anos * 365 
total_dias = niver_anos + niver_mes + dias

'''Retorno para o usuario'''
print(f"O aniversario do usuario em dias e {total_dias}")