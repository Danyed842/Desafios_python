#Challenge 18 - without multiples of 4
#Date: 17 of june, 2025
#Statement = create a for function that recieve a number for the user and count from 1 to the number that the user give without multiples of 4
num = int(input("put a number to arrive:"))
for i in range(0, num):
    result = [ ]
    i += 1
    result.append(i)
    if i % 4 == 0:
        result.remove(i)
    print(result)

