#Challenge 34 - search on matrix
#Date: 18 of june, 2025
#Statement = ask the user for the name of a product, if exist, show her price. If not exist, return "product not founded"
product = [
    ["pineapple", 3000],
    ["lemon", 2000],
    ["watermelon", 7000]
]
fruit_requested = input("fruit that you search:")
for value, price in product:
        if value == fruit_requested:
            print(price)
        else:
           print("isn't here")

