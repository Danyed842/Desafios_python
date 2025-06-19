#Challenge 25 - list with 5 fruits
#Date: 18 of june, 2025
#Statement = create a list with 5 fruits and add, count, search, and travel with for
fruits = ["apple", "orange", "strawberry", "peach", "banana"]

print("The first is:", fruits[0], "The last is:", fruits[-1])

fruits.append("lemon")
print(fruits)

print(len(fruits))

def search_fruit(fruit_searched):
    result = [ ]
    for fruit in fruits:
        if fruit_searched == fruit:
            result.append(fruit_searched)    
    return result

print("The fruit you search is here?:", search_fruit("apple"))

for i in fruits:
    fruits_upper = i.capitalize()
    print(fruits_upper)