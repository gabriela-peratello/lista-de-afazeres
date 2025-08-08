#LISTA DE TAREFAS (REVISÃO)
from manipulacao import Manipulacao

tarefas = []
dever = []
cont = 0
manipulacao = Manipulacao
while True:

    print("""
            ...............................
            |                             |
            |       LISTA AFAZERES        |
            |                             |
            |.............................|
            | 1 - INSERIR TAREFA          |
            |.............................|
            | 2 - LISTAR TAREFA           |
            |.............................|
            | 3 - MARCAR COMO CONCLUÍDO   |
            |.............................|
            | 4 - REMOVER TAREFA          |
            |.............................|
            | 0 - SAIR                    |
            ...............................
            """)

    escolha = int(input("O que você quer fazer agora? Escolha um número:")) #pedir para o usuario a opção que ele quer

    if escolha == 1:
        while True: #enquanto escolha um for verdadeiro
            tarefa = input("Digite a tarefa que você tem para hoje: [ ]").lower()
            tarefas.append({"tarefa": tarefa}) #tarefa é armazenada como dicionário
            perguntar_dnvo = input("Adicionar outra tarefa?").strip().lower() #strip = tira tds as "imperfeições"
            if perguntar_dnvo != "sim":   
                break 

    elif escolha == 2:
                print ("Beleza! Essas são as tarefas que você separou:")
                for item in tarefas: #percorre a lista tarefas 
                        print(item["tarefa"])
                input("\nPressione Enter para voltar ao menu...") #\n = quebra de linha

    elif escolha == 3:
           len (tarefas)
           dever_feito = input("Qual tarefa você concluiu?")
           tarefas[dever_feito] = tarefas[dever_feito] + "[Concluído]"
                        
    elif escolha == 4:
        tarefa_feita = int(input("Qual tarefa você deseja excluir?"))
        tarefas.pop(tarefa_feita)          
                          
    elif escolha == 0:
                print("Saindo...")
                #manipulacao.salvar_dever(tarefas.)
                break
    else:
                print("Essa opção não está disponível!")
                break

#tarefa_feita = int(input("Qual tarefa você deseja excluir?"))
                #tarefas.pop(tarefa_feita)               