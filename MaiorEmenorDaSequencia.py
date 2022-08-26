import os 
os.system('cls')
maior = 0
menor = 0
tamanho = int(input('Quantas pessoas deseja adicionar o peso?'))
for var in range(1, tamanho + 1):
    peso = float(input(f'Digite o peso da {var}º pessoa:'))
    if var == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior =peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi o de {maior}KL')
print(f'E o menor peso foi o de {menor}KL')