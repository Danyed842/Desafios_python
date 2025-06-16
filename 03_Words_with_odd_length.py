#Challenge 03 - Words with odd length
#Date: 26 of may, 2025
#Statement = Create a function called filter_odd_length that recieve a list of strings and return a new list only with the words that have a odd length of characters

def filter_odd_lenght(list):
    odd_words = [ ]

    for n in list:
        if len(n) % 2 != 0:
            odd_words.append(n)
        
    return odd_words

print((filter_odd_lenght(["tres", "cuatro", "uno", "palabra", "carro", "avion", "jamon" "cinco"])))
