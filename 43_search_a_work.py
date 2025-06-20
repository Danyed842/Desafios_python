#Challenge 43 - searcher of a word
#Date: 19 of june, 2025
#Statement = read an archive line for line and if the archive contain the word "error" return this word
while True:
 with open("error.txt", "r") as text:
  print(1, "search a word")
  print(2, "show the text")
  print(3, "exit")
  option = int(input("choose an option:"))
  if option == 1:
    search = input("put a word to search:")
    for word in text:
      if search in word:
        print(search)
      else:
        print("this word isn't here")

  elif option == 2:
   print(text.read())
  elif option == 3:
    print("Bye")
    break
  else:
      print("isn't a valid number")