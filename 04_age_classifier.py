#Challenge 04 - Age classifier
#Date: 30 of may, 2025
#Statement = Create a function called age_classifier that recieve the age of a person and return a mensagge according to these ranges: "<0 invalid age", "0-12 kid", "13-17 teenager", "18-64 adult" and "65+ older adult"

def age_classifier(age):
    if age < 0:
        return "invalid age"
    elif age <= 12:
        return "kid"
    elif age <= 17:
        return "teenager"
    elif age <= 64:
        return "adult"
    elif age > 120:
        return "Maybe you`re dead"
    else:
        return "older adult"
print(age_classifier(57))

