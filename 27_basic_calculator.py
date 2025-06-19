#Challenge 27 - Basic calculator
#Date: 18 of june, 2025
#Statement = recieve 2 numbers from the user and an operation (+, -, *, /) according to the operation, make and show the result.
num1 = int(input("Put a number:"))
operation = input("Put a operation(+-*/):")
num2 = int(input("Put other number:"))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else:
    result = num1 / num2    
   
print(f"The result of the operation is {result}")