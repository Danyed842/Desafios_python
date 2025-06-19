#Challenge 30 - making loops
#Date: 18 of june, 2025
#Statement = create functions and loops.
i = 0
while i < 10:
    i += 1
    print(i)


number = int(input("put a number:"))
while number > 0:
    number -= 1
    print(number)


num1 = int(input("put number 1:"))
num2 = int(input("put number 2:"))
num3 = int(input("put number 3:"))
num4 = int(input("put number 4:"))
num5 = int(input("put number 5:"))
for num in [num1, num2, num3, num4, num5]:
    result = num1 + num2 + num3 + num4 + num5
    
print(f"The sum of the 5 numbers is: {result}") 

def secret_num(number):
   secret_number = 18
   while number != secret_number:
       if number < secret_number:
           return "More higher"
       elif number > secret_number:
           return "More lower"
   else:
      return "¡Congratulations!, you found the secret number" 
print(secret_num(18))

num = int(input("put a number to give her table:"))
for i in range(1, 11):
    print(num * i)

word = input("put a word to count her letters:")
contador = 0
for letter in word:
    contador += 1
    print(f"{letter} {contador}")

