#Challenge 41 - word counter in txt
#Date: 18 of june, 2025
#Statement = create a system that count the words in a archive txt
with open("text.txt", "r") as text:
 for word in text:
    print("The archive have", len(word.split()), "words")