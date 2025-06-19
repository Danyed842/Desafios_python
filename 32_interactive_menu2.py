#Challenge 32 - Interactive menu 2
#Date: 18 of june, 2025
#Statement = create a function that make a Interactive menu in the who only can quit with exit.
def interct_menu2(add_task, tasks, remove_task, exit):
    tasks2 = [ ]
    while True:
        print(1," Add task")
        print(2," Tasks")
        print(3," remove task")
        print(4," exit")
        option2 = int(input("Choose an option:"))
        if option2 == 1:
            task = input("add a new task:")
            tasks2.append(task)
        elif option2 == 2:
            for i, t in enumerate(tasks2):
                print(f"number({i+1}. {t})")
        elif option2 == 3:
            remove = int(input("put the number of the task to remove:"))-1
            if 0 <= remove < len(tasks2):
                tasks2.pop(remove)
            else:
                print("Invalid number")
        else:
            print("Goodbay")
            break
print(interct_menu2(1, 2, 3, 4))