#Challenge 08 - register system in the gym
#Date: 1 of june, 2025
#Statement = Create a program that register one person and give him personalized recommendations according to his age, local weather and if is raining or not
def register_name(name, age):
    if age < 0:
        return "invalid"
    elif age <= 12:
        return " Hello "+ name + ", You`re a kid." 
    elif age <= 17:
        return "Hello " + name + ", You`re a teenager."
    elif age <= 59:
        return "Hello " + name + ", You`re an adult."
    else:
        return "Hello " + name + ", You`re an older adult."
def weather_and_clothing(temperature, rain):
    if temperature > 30 and rain == False:
        return "light clothing"
    elif temperature < 15 and rain == True:
        return "coat and raincoat"
    elif 15 <= temperature <= 30 and rain == False:
        return "comfortable clothes"
    else:
        return "Prepare a change of clothe juste in case"
name_input = str(input("Enter your name:"))
age_input = int(input("Enter your age:"))
temp_input = float(input("Enter the temperature:"))
rain_input = input("Is raining? True or False:")
if rain_input == "True":
    rain_input = True
else:
    rain_input = False
print(register_name(name_input, age_input), "recommendation:", weather_and_clothing(temp_input, rain_input))