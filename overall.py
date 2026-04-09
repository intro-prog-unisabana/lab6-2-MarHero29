def student_averages(data):
    result = {}
    
    for student, grades in data.items():
        if len(grades) == 0:
            result[student] = 0
        else:
            total = sum(grades.values())
            count = len(grades)
            average = round(total / count)
            result[student] = average
            
    return result

def assignment_averages(data):
    totals = {}
    counts = {}
    
    for student, grade in data.items():
        for assignment, score in grade.items():
            
            if assignment not in totals:
                totals[assignment] = 0
                counts[assignment] = 0
                
            totals[assignment] += score
            counts[assignment] += 1
    result = {}
    for assignment, total in totals.items():
        result[assignment] = round(total / counts[assignment])
    return result
