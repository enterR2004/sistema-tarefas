tarefas = []


def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")


def listar_tarefas():
    print("\n=== Lista de Tarefas ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")