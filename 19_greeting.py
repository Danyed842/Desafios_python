#Challenge 19 - Greeting
#Date: 17 of june, 2025
#Statement = create a function that recieve a name and return a greeting customized. 
def greeting(name):
    return "Hello," + " " + name + ". " + "Welcome to the system."

print(greeting("Jose"))

hours_per_day = int(input("put your hous of job in a day:"))
money_per_hour = float(input("put your salary per hour:"))
days_worked = int(input("put the number of days that you job:"))
salary = (hours_per_day * money_per_hour) * days_worked
print(f"your salary per month is {salary}")

name = input("put your name:")
gender = input("put your gender:")
if gender == "Masculino":
    saludo = "Bienvenido"
elif gender == "Femenino":
    saludo = "Bienvenida"
print(f"{saludo} {name}")

name = input("put your name:")
age = int(input("put your age:"))
city = input("put your city:")
print(f"Hello {name}, you have {age} years old and you live in {city}. ")

