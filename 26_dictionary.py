#Challenge 26 - Dictionary
#Date: 18 of june, 2025
#Statement = create a dictionary and interact with him
person1 = {
    "name": "Luis",
    "age": 25,
    "city": "Bogotà"
}
print(person1)

person1["city"] = "Chinacota"
print(person1)

person1["job"] = "engineer"
print(person1)

print(person1.keys())

print(person1.values())

prices = {
    "Apple": 2,
    "Watermelon": 7,
    "Orange": 3,
    "Pencil": 1
}

def product_needed(product):
        if product in prices.keys():
            price = prices[product]
            return "The price of" + " " + product + " is " + str(price)
        else:
            return "We don't have this"
             
product = str(input("What product do you need?:"))
print((product_needed(product)))

student1 = {
     "name": "Emilio",
     "age": 17,
     "note": 4.5
}

student2 = {
     "name": "Jorge",
     "age": 14,
     "note": 3.6
}

student3 = {
     "name": "Laura",
     "age": 15,
     "note": 4.2
}

for student in (student1, student2, student3):
     if student["note"] >= 4.0:
          print(student["name"], "You pass with ", student["note"])
     else:
          print(student["name"], "You didn't pass with ", student["note"])
