student_marks={
    "lokesh":95,
    "kong":35,
    "silly":67,
    "milly":78,
    "bill":2
}
student_grade={}
for i in student_marks:
    print(i)
    marks=student_marks[i]
    print(marks)
    if marks>=90:
        student_grade[i]="A+"
    elif marks>=60 and marks<90:
        student_grade[i]="A"
    elif marks>=35 and marks<60:
        student_grade[i]="B"
    else:
        student_grade[i]="Fail"
print(student_grade)       