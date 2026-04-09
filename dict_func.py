def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    other_info = employee_info.copy()
    other_info.pop("Name", None)
    other_info.pop("Salary", None)
    other_info.pop("Role", None)

    if len(other_info) == 0:
        print("No other info!")
    else:
        for key, value in other_info.items():
            print(f"{key}: {value}")