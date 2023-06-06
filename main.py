from classes import *


login_ou_cadastro = int(input("Você deseja fazer:\n[1] - Login \n[2]- Cadastro\n"))
while login_ou_cadastro != 1 and login_ou_cadastro !=2:
    login_ou_cadastro = int(input("Você deseja fazer:\n[1] - Login \n[2]- Cadastro\n"))
if login_ou_cadastro == 1:
    nomecadastro = input("Digite seu nome:")
    print("Ex:2 INFO V")
    turmacadastro = input("Digite sua turma:")
    matriculacadastro = input("Digite sua matricula")
    senha_cadastro = input("Digite sua senha")
    aluno_cadastro = Aluno(nomecadastro, matriculacadastro, turmacadastro, senha_cadastro)
    if len(matriculacadastro) != 13:
        aluno_cadastro.mensagem_de_erro('Erro')

    else:
        aluno_cadastro.cadastros_de_aluno()