from tkinter import messagebox
import sqlite3 as sql

class Corpo_Escolar:
    def __init__(self, nome, matricula,senha):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha


class Aluno (Corpo_Escolar):
    def __init__(self, nome, turma, matricula, senha):
        super().__init__(nome, matricula, senha)
        self.turma = turma
        self.senha = senha

    def cadastros_de_aluno (self):
        novo_aluno = Aluno(self.nome, self.matricula, self.turma, self.senha)
        with open ('Alunos_cadastrados.txt', 'a') as cadastrar:
            cadastrar.write(str(novo_aluno))
    
    def mensagem_de_erro (titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def inserir_dados(self):
        banco = sql.connect("Banco_JICS.db")
        cursor = banco.cursor()
        cursor.execute(" INSERT INTO Alunos VALUES(:nome,:turma,:matricula,:senha)",{
            'nome': self.nome,
            'turma': self.turma,
            'matricula': self.matricula,
            'senha': self.senha,
        })
        banco.commit()
        banco.close()

    def verificar_dados(self):
        banco = sql.connect("Banco_JICS.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM Alunos WHERE matricula= ? AND senha= ?", (self.matricula,self.senha) )
        tabela = cursor.fetchone()
        if tabela is not None:
            print("Login feito com sucesso")
        else:
            print("Matricula ou senha incorretas")