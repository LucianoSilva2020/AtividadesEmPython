from aluno import Aluno

listaCursos = ['Dev. Full Stack','Python','Banco de dados']

matricula = int(input("Digite a matricula"))
nome = input("Digite o nome")
while(True):
    curso = input("Digite o curso")
    if curso in listaCursos:    
        break
    else:
        print("Curso não cadastrado. Digite novamente")
        
aluno1 = Aluno(matricula,nome,curso,[])
for i in range(4):
    nota = float(input(f"Digite a {i + 1} nota"))
    aluno1.cadastrarNota(nota)
    

media = aluno1.media()
aluno1.mostrarResultado()