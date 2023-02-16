# Felipe es un programador que debe marcar todos lo días la hora de entrada y la hora de
# salida. Si Felipe trabajó más de ocho horas, hay que pagarle un costo por hora extra que es
# igual a 1.5 el monto de la tarifa por hora. Haga un programa que, recibiendo la tarifa por
# hora, la hora de entrada y la hora de salida, imprima el total de dinero que Felipe recibió en
# ese día.

# def daily_gains(entrance, exit, salary):
#     hours_worked = exit - entrance
#     gains = hours_worked * salary
#     if hours_worked - 8 != 0:
#         extra_work = hours_worked - 8
#         gains = gains + (extra_work * (salary * 1.5))
#         print(f"Flipe gano {gains} con extras")
#     else:
#         print(f"Flipe gano {gains}")


# daily_gains(8, 20, 1000)

hora_entrada = int(input("Introduzca la hora de entrada (formato 24 horas): "))
minutos_entrada = int(input("Introduzca los minutos de entrada: "))
hora_salida = int(input("Introduzca la hora de salida (formato 24 horas): "))
minutos_salida = int(input("Introduzca los minutos de salida: "))
tarifa_hora = float(input("Ingrese su salario por hora: "))
salario_normal = (8 * tarifa_hora)
if hora_salida > hora_entrada:
    horas_trabajadas = abs(int(
        ((hora_salida * 60 + minutos_salida) + 24) - (hora_entrada * 60 + minutos_entrada)) / 60)
else:
    horas_trabajadas = abs(int(
        ((hora_entrada * 60 + minutos_entrada) - (hora_salida * 60 + minutos_salida)) / 60) - 24)
if horas_trabajadas > 8:
    horas_extras = horas_trabajadas - 8
    pago_horas_extras = (tarifa_hora * 1.5) * horas_extras
    salario = salario_normal + pago_horas_extras
    print(f"Su salario de hoy corresponde a: {salario:.2f}")
elif horas_trabajadas == 0:
    horas_extras = 24 - 8
    pago_horas_extras = (tarifa_hora * 1.5) * horas_extras
    salario = (8 * tarifa_hora) + pago_horas_extras
    print(f"Su salario de hoy corresponde a: {salario:.2f}")
else:
    salario = horas_trabajadas * tarifa_hora
    print(f"Su salario de hoy corresponde a: {salario:.2f}")
