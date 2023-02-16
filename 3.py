# Determinar si un estudiante ganó o perdió un curso, si pierden el curso todos los
# estudiantes cuya nota es menor a 70.
def passes(grade):
    if grade >= 70:
        print("Paso")
    else:
        print("No paso")


passes(int(input("Cual es su nota")))
