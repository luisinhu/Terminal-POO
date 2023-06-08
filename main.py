from classes import *

import sqlite3 as sql

banco = sql.connect("Banco_JICS.db")

cursor = banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Alunos(
    nome TEXT NOT NULL,
    turma TEXT NOT NULL,
    matricula INT PRIMARY KEY NOT NULL,
    senha TEXT NOT NULL
)
''')
banco.commit()
banco.close()




login_ou_cadastro = int(input("Você deseja fazer:\n[1] - Cadastro \n[2]- Login\n"))
while login_ou_cadastro != 1 and login_ou_cadastro !=2:
    login_ou_cadastro = int(input("Você deseja fazer:\n[1] - Login \n[2]- Cadastro\n"))
if login_ou_cadastro == 1:
    nomecadastro = input("Digite seu nome:")
    print("Ex:2 INFO V")
    turmacadastro = input("Digite sua turma:")
    matriculacadastro = input("Digite sua matricula")
    senha_cadastro = input("Senha")
    aluno_cadastro = Aluno(nomecadastro, turmacadastro, matriculacadastro, senha_cadastro)
    if len(matriculacadastro) != 13:
        print("Numero de matricula inserido incorretamente")
    else:
        aluno_cadastro.inserir_dados()

elif login_ou_cadastro == 2:
    matriculalogin = input("Digite sua matricula")
    senhalogin = input("Digite sua senha")
    loginaluno = Aluno('', '', matriculalogin, senhalogin)
    loginaluno.verificar_dados()