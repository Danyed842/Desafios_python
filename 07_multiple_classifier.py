#Challenge 07 - multiple classifier with people
#Date: 1 of june, 2025
#Statement = Create a systen that clasify one person according to age, outside temperature and if is raining or not
def multiple_classifier1(age):
    if age < 0:
        return "invalid age", 
    elif age <= 12:
        return "kid"
    elif age <= 17:
        return "teenager"
    elif age <= 59:
        return "adult"
    else:
        return "older adult" 
def multiple_classifier2(temperature, rain):
    if temperature > 35 and rain == False:
        return "it`s really hot, wear light clothing"
    elif temperature < 15 and rain == True:
        return "it`s cold and is raining, wear a coat and a raincoat"
    elif temperature >= 15 and temperature <= 35 and rain == False:
        return "pleasent temperature, dress comfortably"
    else:
        return "prepare for changing weather"
age_input = int(input("Enter your age:"))
temp_input = int(input("Enter the temperature:"))
rain_input = input("Is raining? enter True or False:")
if rain_input == "True":
    rain_input = True
else:
    rain_input = False
print(multiple_classifier1(age_input), multiple_classifier2(temp_input, rain_input)) 