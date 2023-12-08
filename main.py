
class Tarefa:
    def __init__(self, descricao, data_vencimento, prioridade):
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.prioridade = prioridade

tarefas = []

def cadastrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data_vencimento = input("Digite a data de vencimento (formato YYYY-MM-DD): ")
    prioridade = int(input("Digite a prioridade da tarefa (1 a 5): "))

    # Validar prioridade
    if 1 <= prioridade <= 5:
        tarefa = Tarefa(descricao, data_vencimento, prioridade)
        tarefas.append(tarefa)
        print(f"Descrição: {tarefa.descricao}, Data de Vencimento: {tarefa.data_vencimento}, Prioridade: {tarefa.prioridade}")
        print("Tarefa cadastrada com sucesso!")
    else:
        print("Erro: Prioridade inválida. A prioridade deve estar entre 1 e 5.")

def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for idx, tarefa in enumerate(tarefas):
            print(f"{idx + 1}. Descrição: {tarefa.descricao}, Data de Vencimento: {tarefa.data_vencimento}, Prioridade: {tarefa.prioridade}")

def atualizar_tarefa():
    exibir_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1

    if 0 <= indice < len(tarefas):
        while True:
            print("Qual informação deseja atualizar?")
            print("1 - Descrição")
            print("2 - Prioridade")
            print("3 - Data de Vencimento")
            print("4 - Sair")

            opc = int(input("Digite a opção:"))
            # atualizar a descrição
            if opc == 1:
                tarefas[indice].descricao = input("Digite o novo valor: ")
                print("Tarefa atualizada com sucesso!")

            # atualizar a prioridade
            elif opc == 2:
                if 0 <= indice < len(tarefas):
                    nova_prioridade = int(input("Digite a nova prioridade (1 a 5): "))

                    # Validar nova prioridade
                    if 1 <= nova_prioridade <= 5:
                        tarefas[indice].prioridade = nova_prioridade
                        print("Tarefa atualizada com sucesso!")
                    else:
                        print("Erro: Nova prioridade inválida. A prioridade deve estar entre 1 e 5.")

            # atualizar a data de vencimento
            elif opc == 3:
                tarefas[indice].data_vencimento = input("Digite o novo valor: ")
                print("Tarefa atualizada com sucesso!")

            # sair das opções de atualização
            elif opc == 4:
                        print("Tarefa atualizada com sucesso!")
                        break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Erro: Tarefa não encontrada.")

def excluir_tarefa():
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1

    if 0 <= indice < len(tarefas):
        del tarefas[indice]
        print("Tarefa excluída com sucesso!")
    else:
        print("Erro: Tarefa não encontrada.")

def menu_principal():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            cadastrar_tarefa()
        elif escolha == "2":
            exibir_tarefas()
        elif escolha == "3":
            atualizar_tarefa()
        elif escolha == "4":
            excluir_tarefa()
        elif escolha == "5":
            print("Saindo do aplicativo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
