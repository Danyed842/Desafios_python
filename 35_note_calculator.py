#Challenge 35 - note calculator
#Date: 18 of june, 2025
#Statement = ask the user for give 5 notes in range (0.0-5.0) check if is in this range, and get the media and say if pass or no pass
note1 = float(input("put a note:"))
if 5.0 >= note1 >= 0.0:
    print(note1)
else:
    print("isn't a valid date")
note2 = float(input("put a note:"))
if 5.0 >= note2 >= 0.0:
    print(note2)
else:
    print("isn't a valid date")
note3 = float(input("put a note:"))
if 5.0 >= note3 >= 0.0:
    print(note3)
else:
    print("isn't a valid date")
note4 = float(input("put a note:"))
if 5.0 >= note4 >= 0.0:
    print(note4)
else:
    print("isn't a valid date")
note5 = float(input("put a note:"))
if 5.0 >= note5 >= 0.0:
    print(note5)
else:
    print("isn't a valid date")
media = (note1+note2+note3+note4+note5)/5
if media > 3.5:
    print(f"Your media is {media}. ¡You pass!")
else:
    print(f"Your media is {media}. You didn't pass")

    