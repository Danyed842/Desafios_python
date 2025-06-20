#Challenge 42 - reverse text
#Date: 19 of june, 2025
#Statement = reverse a archive txt
with open("text2.txt", "r") as text:
        lines = text.readlines()
        for revers in reversed(lines):
            print(revers)