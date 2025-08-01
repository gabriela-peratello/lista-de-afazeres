#LISTA DE TAREFAS (REVISÃO)

tarefas = []
tarefas_feitas = []
cont = 0

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
            tarefas.append({"tarefa": tarefa, "concluida": False}) #tarefa é armazenada como ducionário
            perguntar_dnvo = input("Adicionar outra tarefa?").strip().lower() #strip = tira tds as "imperfeições"
            if perguntar_dnvo != "sim":   
                break       
    elif escolha == 2:
                print ("Beleza! Essas são as tarefas que você separou:")
                for item in tarefas:
                        print(item["tarefa"])
                input("\nPressione Enter para voltar ao menu...") #\n = quebra de linha
    elif escolha == 3:
               tarefa_concluir = int(input("Qual tarefa voceê concluiu?")) + "[FEITO]"
               tarefas[tarefa_concluir] = tarefas [tarefa_concluir]
    elif escolha == 4:
                tarefa_excluir = int(input("Quak tarefa você deseja excluir?"))
                tarefas.pop(tarefa_excluir)
                
    elif escolha == 0:
                print("Saindo...")
                break
    else:
                print("Essa opção não está disponível!")
                break



