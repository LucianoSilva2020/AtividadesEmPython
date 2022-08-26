import os
os.system('cls')

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0

tamanho = int(input('Quantas pessoas deseja cadastra?\n'))
for var in range(1, tamanho + 1):
    print(f'------ {var}º PESSOA ------')
    nome = input('Digite seu nome:')
    idade = int(input('Digite sua idade:'))
    sexo = input('Digite seu sexo [M/F]:')
    somaIdade += idade
    if var == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
mediaIdade = somaIdade / tamanho
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo são {totalMulher20} mulheres com menos de 20 anos.')        