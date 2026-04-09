from grades_manager import*
print("welcome to the student Grades Manager!")
my_grades={}
while True:
                    opciones=input("""Select an option:)
                    1. Add student
                    2. Print student grade averages
                    3. Exit """)
if opciones=="1":
        my_grades=add_student(my_grades)
elif opciones=="2":
        seleccion = input("""Select an option:
                        a. Display all students
                        b. Display selected students """)
        if seleccion== "a":
            avg_by_student(my_grades)
        elif seleccion=="b":
            nombres=input("Enter student names (comma-separated):/n")
            keys = [nombre.strip().title() for nombre in nombres.split(",")]
            avg_by_student(my_grades, keys)
        else:
            print("Invalid option selected!")
elif opciones=="3":
        print("Goodbye!")
else:
    print("Invalid option selected!")