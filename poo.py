class Estudante:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self): 
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Recuperação"

        return "Reprovado"

    def descrever(self):
        return (f"{self.nome:<16}{self.nota1:<7}{self.nota2:<7}"f"{self.media():<8.1f}{self.situacao():<14}")

estudantes = []

def cadastrar():
    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    estudantes.append(Estudante(nome, nota1, nota2))
    print("Estudante cadastrado.")

def listar():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    print(f"\n{'Nome':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")
    for estudante in estudantes:
        print(estudante.descrever())

def media_da_turma():
    if len(estudantes) == 0:
        print ("Nenhum estudante cadastrado.")
        return

    soma = 0

    for estudante in estudantes:
        soma = soma + estudante.media()

    print(f"\nMédia da turma: {soma / len(estudantes):.2f}")

def menu():
    while  True:
        print("\n1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Média da turma")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            media_da_turma()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

menu()