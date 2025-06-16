#Challenge 02 - sorter of multiples
#Date: 26 of may, 2025
#Statement = Create a function called filter_of_multiples(list, divider) that recieves a list of integers and a divisor number. The function should reeturn a new list only with the numbers that are multiples of divisor
def filter_of_multiples(list, divisor):
    result = [ ]
    for n in list:
        if n % divisor == 0:
            result.append(n)
    return result
print(filter_of_multiples([5, 12, 7, 20, 30, 8], 5))

