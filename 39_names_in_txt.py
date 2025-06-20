#Challenge 39 - ennumerating txt
#Date: 19 of june, 2025
#Statement = ennumerate names in a txt
with open("names.txt", "r") as names:
    n = 0
    for name in names:
        n += 1
        print(n, name.strip())
        
    
    