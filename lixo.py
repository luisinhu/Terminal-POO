
def verificar_matri (self,matricula_verifica, turma_verifica):
    with open ('Alunos_cadastrados.txt','r') as rodar:
        if rodar != matricula_verifica:
            print("Erro")
        else:
            print("Login feito com sucesso")

        with open('Alunos_cadastrados.txt', 'r') as rodar2:
            if rodar2 != turma_verifica:
                print("Erro")
            
            else:
                pass