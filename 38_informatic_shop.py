#Challenge 38 - informatic shop
#Date: 19 of june, 2025
#Statement = create a system that simule a basic shop
while True:
   print(1, "add products")
   print(2, "look products")
   print(3, "buy")
   print(4, "exit")
   option = int(input("choose that you need to do:"))
   if option == 1:
      list1 = [ ]
      product = input("add a product:")
      price = float(input("add the price of the product:"))
      if price <= 0:
         print(f"isn't a valid price")
      else:
         list1.append(product)
         list1.append(price)    
   elif option == 2:
      print(list1)
   elif option == 3:
      buyed = [ ]
      buy = input("put the name of the product that you want to buy:")
      if buy == product:
         buyed.append(list1)
         print(buyed)
      elif buy != product:
         print(f"The product isn't here")
         
   elif option == 4:
      print(f"You purchase: {product},the total price is: {price}")
      break
