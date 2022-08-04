print('''Exemplos de palíndromo:
        APOS A SOPA
        A SACADA DA CASA
        A TORRE DA DERROTA
        O LOBO AMA O BOLO
        ANOTARAM A DATA DA MARATONA''')
frase = str(input('Digite uma frase:'))
frase = frase.strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
