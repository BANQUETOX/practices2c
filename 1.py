# Determinar si una persona tiene fiebre. Una persona tiene fiebre si la temperatura es mayor
# a 37 grados. El programa recibe como información la temperatura de la persona.
def cold(temperature):
    if temperature >= 38:
        print("Tiene fiebre bro")
    else:
        print("Estamos sanos")


temperature = int(input("Cual es su temperatura en Celcius?"))

cold(temperature)
