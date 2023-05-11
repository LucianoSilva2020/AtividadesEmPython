import os
os.system('cls')
lista = []
lista2 = []
verde = '\033[1;36;42m'
for var in range(1, 6):
    numero = int(input(f'{verde} Digite o {var}º numero:'))
    if numero % 2 == 0:
        lista.append(numero)
    else:
        lista2.append(numero)    


print(f'Os números pares são {lista}.')
print(f'E os numeros impares são {lista2}.')    