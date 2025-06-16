#Challenge 10 - prime number in range classifier
#Date: 2 of june, 2025
#Statement = Create a program that recieve 2 numbers, start and end and return a list with all the prime numbers on this range
def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, n):
      if n % i == 0:
         return False
   return True
print(is_prime(4))

def prime_in_range(start, end):
    result = [ ]
    for n in range(start, end+1):
        if is_prime(n):
           result.append(n)
    return result
print(prime_in_range(10, 20))