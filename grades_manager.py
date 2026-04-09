def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades={}

    name = input("Enter student name:\n").strip().title()

    subjects = {}
    user_input= input ("Enter subject and grade (or 'exit' to finish):\n").strip()
    while user_input.lower()!= "exit":

        if "," in user_input:

            subject, grade= user_input.split(",", 1)
            subject = subject.strip().title()
            grade=float(grade.strip())
            subjects[subject]=grade
        
        user_input= input ("Enter subject and grade (or 'exit' to finish):\n").strip()
    
    student_grades[name]= subjects

    print(f"Student {name} successfully added to the grades management system.\n")

    return student_grades

def get_students(student_grades, keys):

    result={}

    for name in keys:
        name_title = name.title()

        if name_title in student_grades:
            result[name_title]= student_grades[name_title]
        else:
            print(f"{name_title} not found!")

    return result
    def avg_by_student(student_grades, keys=None):

        if keys is None:
            selected = student_grades
        else:
            selected = get_students(student_grades, keys)

        result = {}

    for student, grades in selected.items():
        if len(grades) == 0:
            result[student] = 0
        else:
            avg = sum(grades.values()) / len(grades)
            result[student] = round(avg, 1)

    return result