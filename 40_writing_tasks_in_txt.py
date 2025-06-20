#Challenge 40 - write a task in txt
#Date: 18 of june, 2025
#Statement = create a system that ask the user for tareas, and put in a txt.

while True:
    print(1, "add a task")
    print(2, "look the tasks")
    print(3, "exit")
    option = int(input("choose an option:"))
    if option == 1:
        with open("tasks.txt", "a") as task:
            task.write(input("agrega lo que quieras agregar a tareas.txt:"))
    elif option == 2:
        with open("tasks.txt", "r") as task:
            content = task.read()
            print(content)

    elif option == 3:
        break