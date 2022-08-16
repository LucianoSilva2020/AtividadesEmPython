import os
from traceback import print_tb
os.system('cls')
nomeEnota = {}
tamanho = int(input('Quantos alunos deseja resgistrar?'))
for var in range(1, tamanho + 1):
    nome = input(f'Digite o nome do {var}° aluno:')
    nota = float(input('Digite a nota:'))
    nomeEnota[nome] = nota
ver = input('Deseja visualizar a note de quem ?')
print(f'Você solicitou a nota de {ver} que foi {nomeEnota[ver]}.')