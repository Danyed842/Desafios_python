#Challenge 17 - Fizzbuzz
#Date: 17 of june, 2025
#Statement = create a for function that numbers in range 1-20 and return if is multiple of 3 "Fizz", if is multiple of 5 "Buzz" or if is multiple of both "FlizzBuzz"
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "=", "FizzBuzz")
    elif i % 3 == 0:
        print(i, "=","Fizz")
    elif i % 5 == 0:
        print(i, "=", "Buzz")
    else:
        print(i)