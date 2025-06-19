#Challenge 36 - password
#Date: 18 of june, 2025
#Statement = create a function with a password setted, you have 3 trys if you're right return "acces allowed" if you're not right return "account bloqued"
tray = 0
max = 3 
while tray < max:  
      password = "python321"
      pass_try = input("put your password:")     
      if pass_try == password:
        print("acces allowed")
        break 
      else:
          tray += 1
          if tray == max: 
             print(f"account bloqued")
             break
    
    