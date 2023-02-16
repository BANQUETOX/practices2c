#  El Gobierno ha decidido que todas aquellas personas que tienen un salario igual a superior
# a un millón de colones deben pagar un impuesto del 10%. Calcule el salario neto de un
# trabajador. El sistema recibe el salario del trabajador como entrada.

def calc_salary(salary):
    if salary >= 1000000:
        tax = salary * 0.1
        netSalary = salary - tax
        print("Debe pagar impuestos")
        print("Su salario neto es de: %f" % netSalary)
    else:
        print("No paga impuesto")
        print("Salario neto: %f" % salary)


calc_salary(
    int(input("Cual es su Salario en colones?")))
