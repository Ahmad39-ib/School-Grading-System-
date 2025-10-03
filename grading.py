
def grade_system():
    score = int(input("enter student_score (0 - 100): "))
    if score >= 90:
        grade = "A"
    elif score >=  80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"
    print("Grade:", grade)
print(grade_system())        


    