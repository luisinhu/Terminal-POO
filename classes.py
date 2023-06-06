from tkinter import messagebox


class Corpo_Escolar:
    def __init__(self, nome, matricula,senha):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha


class Aluno (Corpo_Escolar):
    def __init__(self, nome, matricula, turma, senha):
        super().__init__(nome, matricula, senha)
        self.turma = turma
        self.senha = senha


    
    def __str__(self):
        return f"Nome: {self.nome}\nMatricula: {self.matricula}\nTurma: {self.turma}\n"

    def cadastros_de_aluno (self):
        novo_aluno = Aluno(self.nome, self.matricula, self.turma, self.senha)
        with open ('Alunos_cadastrados.txt', 'a') as cadastrar:
            cadastrar.write(str(novo_aluno))
    
    def mensagem_de_erro (titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)



       
        