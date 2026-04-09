def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    student_name = input("Enter student name:\n").title()
    subjects = {}

    while True:
        election = input('Enter subject and grade (or "exit" to finish):\n').lower()
        if election == "exit":
            break

        if "," not in election:
            print("Invalid format. Use: subject,grade")
            continue
        subject_grade = election.find(",")
        subject = election[:subject_grade].title()
        grade = float(election[subject_grade + 1:])
        subjects[subject] = grade

    student_grades[student_name] = subjects
    print(f"Student {student_name} successfully added.")
    return student_grades

def get_students(student_grades, keys):
    result = {}
    for student in keys:
        found = False
        for student_name in student_grades:
            if student_name.lower() == student.lower():
                result[student_name] = student_grades[student_name]
                found = True
                break
        if not found:
            print(f"{student.title()} not found!")
    return result

def avg_by_student(student_grades, keys=None):
    if keys is None:
        data = student_grades
    else:
        data = get_students(student_grades, keys)

    def avg_by_student(student_grades, keys=None):
        if keys is None:
            data = student_grades
        else:
            data = get_students(student_grades, keys)

    result = {}

    for student in data:
        grades = data[student].values()
        if len(grades) == 0:
            result[student] = 0
        else:
            average = sum(grades) / len(grades)
            result[student] = round(average, 1)

    return result
                                