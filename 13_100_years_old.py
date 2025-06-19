#Challenge 13 - when you turns 100 years old?
#Date: 17 of june, 2025
#Statement = create a function that recieve 1 value, age, with this you return when the person turns 100 years old
def old_man(age):
    actual_year = 2025
    actual_year_100 = actual_year + (100 -age)
    return actual_year_100

print("you turns 100 years old in", old_man(63))