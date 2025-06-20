#Challenge 44 - report generator
#Date: 19 of june, 2025
#Statement = ask at the user for data and make an archive txt ordened with this
data1 = input("put your name:")
data2 = int(input("put your age:"))
data3 = input("put your city:")
data4 = input("put your ocupation/hobby:")
with open("report.txt", "a") as report:
    report.write(f"Your name is: {data1}, your age is: {data2}, your city is: {data3} and your ocupation or hobby is: {data4}.\n")