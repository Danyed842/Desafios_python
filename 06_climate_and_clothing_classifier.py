#Challenge 06 - climate and clothing classifier
#Date: 1 of june, 2025
#Statement = Create a function that recieve 2 inputs: temperature (in ºC) and rain (Boolen: True or False) and return a message how: It`s hot and dry, wear light clothing, It`s cold and is raining, wear a coat and raincoat, pleasent temperature, it`s not raining, dress comfortably and etc.
def climate_and_clothing(temperature, rain):

    if temperature > 36 and rain == False:
        return "It`s hot and dry, wear light clothing"
    elif temperature < 20 and rain == True:
        return "It`s cold and is raining, wear a coat and a raincoat"
    elif temperature == 30 and rain == False:
        return "Pleasure temperature, it`s not raining, dress comfortably"
    else:
        return "etc."
temp_input = int(input("enter temperature in ºC:"))
rain_input = input("Is it raining? (True or False): ")
if rain_input.strip() == "True":
    rain_bool = True
else:
    rain_bool = False
print(climate_and_clothing(temp_input, rain_bool))