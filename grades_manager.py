def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades={}):
    student_name = input("Enter student name:\n").title()
    subjects={}
    while True:
        election = input("Enter a subject and grade for the student? (y/n):\n").lower()
        if election == "exit":
                break
        subject_grade = election.find(",")
        subject=election[:subject_grade].title()
        grade=int(election[subject_grade+1:])
        subjects[subject]=grade
    student_grades[student_name]=subjects
    print(f"{student_name} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    result={}
    for student in keys:
        found = False
        for student in student_grades:
            if student.lower()==student.lower():
                result[student] = student_grades[student]
                found = False
                break
            if not found:
                print(f"{student.title()}not found!")
                return result
            def avg_by_student(student_grades, keys=None):
                if keys is None:
                    data= get_students(student_grades,keys)
                    for student in data:
                        grades=data[student].values()
                        average=sum(grades)/len(grades)
                        print(f"{student}: {average:.1f}")