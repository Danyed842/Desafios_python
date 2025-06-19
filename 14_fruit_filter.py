#Challenge 14 - Identificator of fruits
#Date: 17 of june, 2025
#Statement = create a function that recieve 2 values, fruits and filter, with this you return the fruit in the number filter
def fruits_ident(fruits, filter):
    fruit_filtered = [ ]
    fruit_filtered.append(fruits[filter]) 
    return fruit_filtered
print(fruits_ident(("Apple", "Watermelon", "Grape", "Orange", "Lemon"), 4))