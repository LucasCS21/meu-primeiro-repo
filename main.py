print("Olá! Este é meu primeiro projeto em Python!")

tasks = []

def menu():
    print("=" * 20)
    print("====    MENU    ====")
    print("=" * 20)
    print("\n[0] Sair do programa")
    print("[1] Adicionar tarefa")
    print("[2] Remover tarefa")
    print("[3] Listar tarefas")
    print("[4] Limpar lista de tarefas\n")

while True:
    menu()
    choice = int(input("Digite uma opção (0 a 3): "))

    if choice == 0:
        break

    elif choice == 1:
        new_task = input("Digite uma tarefa para ser adicionada: ")
        tasks.append(new_task)

    elif choice == 2:
        for i in range(len(tasks)):
            print(f"{i} - {tasks[i]}")
        task = int(input("Digite uma tarefa para ser removida: "))
        tasks.pop(task)

    elif choice == 3:
        for task in tasks:
            print(task)

    elif choice == 4:
        tasks.clear()

# TODO:
# Add colors for different priorities;
# Create functions for each choice;
# Fix errors with try-except;