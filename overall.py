def student_averages(datos):
    resultado = {}
    
    for student, grades in datos.items():
        if len(notas)==0:
            resultado[student] = 0
        else:
            total = sum(notas.values())
            count = len(notas)
            average = round(total / count)
            resultado[student] = average
            
    return resultado

def assignment_averages(datos):
    totales = {}
    counts = {}
    
    for student, notas in datos.items():
        for assignment, score in notas.items():
            if assignment not in totales:
                totales[assignment] = 0
                counts[assignment] = 0
                
                totales[assignment] += score
                counts[assignment] += 1
    resultado = {}
    for assignment, total in totales.items():
        count = counts[assignment]
        if count > 0:
            resultado[assignment] = round(total / count)
        else:
            resultado[assignment] = 0
    return resultado