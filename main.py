from tarefas import adicionar_tarefa, listar_tarefas

print("=== Sistema de Tarefas ===")

tarefa = input("Digite uma tarefa: ")

adicionar_tarefa(tarefa)
listar_tarefas()