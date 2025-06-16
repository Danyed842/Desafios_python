#Challenge 11 - twin prime number
#Date: 2 of june, 2025
#Statement = create a program that recieve 2 numbers (start, end) and return a lis of couple of twin prime numbers above this range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def twin_primes(start, end):
    primes = [i for i in range(start, end + 1) if is_prime(i)]
    twins = [ ]
    for i in range((len(primes)) - 1):
        if primes[i + 1] - primes[i] == 2:
            twins.append((primes[i], primes[i + 1]))
    return twins

print(twin_primes(1, 30))