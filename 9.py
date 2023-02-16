# Calcule la nota final de un estudiante para un curso de fundamentos de programación. La
#  Calcule la nota final de un estudiante para un curso de fundamentos de programación. La
# rúbrica de evaluación del curso determina que hay solamente tres exámenes y que la nota
# del curso se calcula por medio de un promedio ponderado el(el primer examen vale un 30
# %, el segundo un 20% y el último un 50%). El estudiante aprueba si el promedio es igual o
# mayor a 70.

def calc_final_grade(first_exam, second_exam, third_exam):
    first_exam = first_exam * 0.30
    second_exam = second_exam * 0.20
    third_exam = third_exam * 0.50
    average = (first_exam + second_exam + third_exam)
    print(first_exam)
    print(second_exam)
    print(third_exam)
    print(average)
    if average >= 70:
        print("Paso")
    else:
        print("No paso")


first_exam = float(input("Cual fue su nota en el primer examen"))
second_exam = float(input("Cual fue su nota en el segundo examen"))
third_exam = float(input("Cual fue su nota en el tercer examen"))
calc_final_grade(first_exam, second_exam, third_exam)
