#Challenge 09 - prime number classifier
#Date: 2 of june, 2025
#Statement = Create a program that recieve a number and return if is prime or not
def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, n):
      if n % i == 0:
         return False
   return True
print(is_prime(4))