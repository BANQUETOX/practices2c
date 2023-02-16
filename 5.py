# Definir si una persona debe pagar impuesto al valor agregado por su consumo mensual de
# electricidad. El programa recibe el consumo mensual de la persona. Se deduce un
# impuesto del 13% si el consumo es mayor a 200 kWh.

def electricity_tax(consume):
    if consume < 200:
        print("No paga impuesto")
    else:
        print("Debe pagar impuesto sobre consumo")


electricity_tax(
    int(input("Cual es su consumo mensual de electricidad en Kwh")))
