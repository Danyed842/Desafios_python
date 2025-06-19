#Challenge 22 - higher number
#Date: 18 of june, 2025
#Statement = create a function that recieve 2 numbers and return the higher
def higher_num(num1, num2):
    if num1 > num2:
        return num1, "is higher."
    elif num1 == num2:
        return "they're equal"
    else:
        return num2, "is higher."

print(higher_num(10, 12))