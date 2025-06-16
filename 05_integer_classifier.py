#Challenge 05 - integer classifier
#Date: 1 of june, 2025
#Statement = Create a function that ask the user for a integer and say if: is positive, negative or zero.  And too if is even or odd
def integer_classifier(integer):
   

    if integer % 2 == 0 and integer < 0:
        return "The number is negative and even"
    elif integer % 2 != 0 and integer < 0:
        return "The number is negative and odd"
    elif integer % 2 == 0 and integer > 0:
        return "The number is positive and even"
    elif integer % 2 != 0 and integer > 0:
        return "The number is positive and odd"
    else:
        return "The number is zero"
user_input = int(input("Enter a number:"))
print(integer_classifier(user_input))