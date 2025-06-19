#Challenge 15 - who is higher, lower or equal?
#Date: 17 of june, 2025
#Statement = create a function that recieve 2 values, num1 and num2, with this you return who number is higher, lower or equal
def higher_lower_equal(num1, num2):
    if num1 > num2:
        return num1, "is higher", "and", num2, "is lower"
    elif num1 == num2:
      return num1, "and", num2, "are equal"
    else:
       return num1, "is lower", "and", num2, "is higher"
print(higher_lower_equal(10, 11))