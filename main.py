print("Olá! Este é meu primeiro projeto em Python!")

tasks = []

while True:
    choice = int(input("Digite uma opção (0 a 3): "))
    if choice == 0:
        break

    elif choice == 1:
        new_task = input("Digite uma tarefa para ser adicionada: ")
        tasks.append(new_task)

    elif choice == 2:
        task = input("Digite uma tarefa para ser removida: ")
        tasks.remove(task)

    elif choice == 3:
        for task in tasks:
            print(task)

# TODO:
# Add colors for different priorities;
# Switch choice 2 to an indexed version;
# Create a menu;
# Create functions for each choice;
# Fix errors with try-except;