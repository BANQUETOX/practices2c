def cold(temperature):
    if temperature >= 38:
        print("Tiene fiebre bro")
    else:
        print("Estamos sanos")


temperature = int(input("Cual es su temperatura en Celcius?"))

cold(temperature)
