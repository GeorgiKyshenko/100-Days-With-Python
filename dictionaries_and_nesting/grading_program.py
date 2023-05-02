students_score = {
    "Harry": 81,
    "Ron": 78,
    "Jerry": 99,
    "Donny": 74,
    "John": 62
}

students_grade = {}

for student in students_score:
    if students_score.get(student) <= 70:
        students_grade[student] = "Fail"
    elif 71 <= students_score.get(student) <= 80:
        students_grade[student] = "Acceptable"
    elif 81 <= students_score.get(student) <= 90:
        students_grade[student] = "Exceed Expectation"
    else:
        students_grade[student] = "Outstanding"

for student in students_grade:
    print(f"{student} - {students_grade.get(student)}")
