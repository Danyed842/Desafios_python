#Challenge 28 - Area of a triangle and convertion of kilometers to meters
#Date: 18 of june, 2025
#Statement = recieve the base and height of a triangle and calculate the area of the triangle. And convertion of kilometers to meters
base = float(input("put the base of the triangle:"))
height = float(input("put the height of the triangle:"))
area = (base * height)/2
print(f"The area is {area}")

km_distance = int(input("Put a distance in kilometers:"))
meters = str(km_distance * 1000) +" meters"
print(f"The kilometers in meters are {meters}")