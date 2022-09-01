class Aluno:
    
    def __init__(self,matricula,nome,curso,listaNotas):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.listaNotas = listaNotas
        
    def cadastrarNota(self,nota):
        if(len(self.listaNotas) >=3):
            print("Só é permitido cadastrar ate 3 notas")
        else:
            self.listaNotas.append(nota)
    
    def media(self):
        media = sum(self.listaNotas) / len(self.listaNotas)
        return media
    
    def mostrarResultado(self):
        media = self.media()
        if(media >= 7):
            print("Aluno aprovado")
        else:
            print("Aluno não aprovado")   