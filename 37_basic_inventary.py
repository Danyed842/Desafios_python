#Challenge 37 - basic inventary
#Date: 18 of june, 2025
#Statement = create a system like a menu where the user can add products, look products, search products and exit
while True:
    
    print(1," Add product")
    print(2," Look products")
    print(3," Search products")
    print(4," exit")
    option = int(input("choose the option that you need:"))
    if option == 1:
        products = [

        ]
        products2 = [ ]
        product = str(input("add the product(name):"))
        product2 = float(input("add the product(price):"))
        products2.append(product)
        products2.append(product2)
        products.append(products2)
        if product2 <= 0:
            print(f"Isn't a valid price")
            products2.remove(product2)
            products2.remove(product)
    elif option == 2:
             print(products)

    elif option == 3:
        name_product = input("put the product to search:")
        if name_product == product:
            print(products2)
        else:
            print(f"It isn't here")
    elif option == 4:
        print("Good bye")
        break
    else:
        print(f"that's not a valid option")
