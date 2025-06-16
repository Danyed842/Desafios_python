#Challenge 01 - Number Classifier
#Date: 26 of may, 2025
#Statement = Classify a list in negative, neutral and positive
def sorter_of_numbers(list):
    positive = []
    negative = []
    neutral = []
    for n in list:
        if n < 0:
            negative.append(n)
        elif n > 0:
            positive.append(n)
        else:
            neutral.append(n)
    return negative, neutral, positive

print(sorter_of_numbers([1, 7, -5, -7, 0, 5]))
