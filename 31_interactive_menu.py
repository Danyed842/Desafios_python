#Challenge 31 - Interactive menu
#Date: 18 of june, 2025
#Statement = create a function that make a Interactive menu in the who only can quit with exit.
def interact_menu(greeting, age, exit):
    greeting = "Hi, welcome to the interactive menu"
    age = int(input("put your age:"))
    while True:
        print(1," Greeting")
        print(2," Show age")
        print(3," Exit")
        option = int(input("choose an option:"))
        if option == 1:
            print(greeting)
        elif option == 2:
            print(age)
        else:
            print("Goodbay"), 
            break
print(interact_menu(1, 2, 3))