#LISTA DE TAREFAS (REVISÃO)
from manipulacao import Manipulacao
confere = []
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
        print("---Marcar como Concluído!---")
        conferir = input("Qual tarefa você concluiu?")
        confere.append(f"[x]{conferir}")
        print(f"Tarefa '{conferir}' concluída com sucesso.")

    elif escolha == 4:
        pergunta = input("Qual tarefa você quer remover?")
        tarefas.remove(pergunta)
        print(f"Tarefa {pergunta} removida.")
    elif escolha == 0:
                with open("main.txt", "w") as arquivo:
                       for tarefa in tarefas :
                        arquivo.write(tarefa + "\n")
                        print("lista salva!")
                break
    else:
                print("Essa opção não está disponível!")
                break
