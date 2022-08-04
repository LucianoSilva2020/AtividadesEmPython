from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}º pessoa nasceu?'))
    idade = atual - nascimento
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.')
print(f'E também tivemos {totalMenor} pessoas menores de idade.')            