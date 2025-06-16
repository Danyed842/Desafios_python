#Challenge 12 - extended academic analysis
#Date: 6 of june, 2025
#Statement = create a function that recieve a list of [name, score] for some students and return: The name of the student with higher score, name of student with lower score, number of students passed (note >= 60) and a new list with their respective cualifications in letters(A, B, etc).
def grade_letter(score):
         if score >= 90:
            return "A"
         elif score >= 80:
            return "B"
         elif score >= 70:
            return "C"
         elif score >= 60:
            return "D"
         elif score < 60:
            return "F" 
def academic_analysis(data):
    highest = ""
    lower = "" 
    approved = 0
 
    for student in data:
        name, score = student
        if score == max(scores):
            highest = name
        if score == min(scores):
            lower = name
        if score >= 60:
            approved += 1
    return highest, lower, approved, graded     
data = [["Ana", 95], ["Luis", 82], ["Carlos", 58], ["Marta", 77]]  
graded = [[student[0], grade_letter(student[1])] for student in data]  
scores = [student[1] for student in data]    
print(academic_analysis(data))