class Manipulacao:

    def salvar_dever (self, tarefas):
        with open ("manipulacao.txt", "w") as arquivo:
            for dever in tarefas:
                arquivo.write(dever + "\n")
        print("Lista salva!")
