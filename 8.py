# Calcule la nota final de un estudiante para un curso de fundamentos de programación. La
# rúbrica de evaluación del curso determina que hay solamente tres exámenes y que la nota
# del curso se calcula por medio de un promedio simple (la suma de las notas de los tres
# exámenes dividido entre tres).
# El estudiante aprueba si el promedio es igual o mayor a 70.

# def calc_final_grade(first_exam, second_exam, third_exam):
#     average = (first_exam + second_exam + third_exam) / 3
#     if average >= 70:
#         print("Paso")
#     else:
#         print("No paso")


# first_exam = float(input("Cual fue su nota en el primer examen"))
# second_exam = float(input("Cual fue su nota en el segundo examen"))
# third_exam = float(input("Cual fue su nota en el tercer examen"))
# calc_final_grade(first_exam, second_exam, third_exam)


# Una empresa que vende flores sacó una promoción, si el cliente compra tres flores, le
# aplica un descuento del 10%. El programa recibe la cantidad de flores y el precio de cada
# flor. Se debe imprimir el total a pagar.

def calc_discount(flowers_array_prices):
    totalPrice = 0
    for i in flowers_array_prices:
        totalPrice = totalPrice + i

    if len(flowers_array_prices) >= 3:
        discount = totalPrice * 0.1
        discount_price = totalPrice - discount
        print("Ha recibido un descuento del 10 porciento en su compra!!! ")
        print(f"El precio de sus flores es de {discount_price}")
    else:
        print(f"El precio de sus flores es de {totalPrice}")


flowers_array_prices = []
flower_amount = int(input("Cuantas flores compro? "))
for i in range(0, flower_amount):
    flower_price = int(input(f"Cuanto le costo la flor #{i + 1}  "))

    flowers_array_prices.append(flower_price)

calc_discount(flowers_array_prices)
