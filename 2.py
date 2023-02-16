# Determinar si un ciudadano puede votar. Un ciudadano puede votar si ya cuenta con 18
# años cumplidos. El programa recibe la edad del ciudadano.
def aviable_for_vote(age):
    if age >= 18:
        print("Puede votar")
    else:
        print("No puede votar")


aviable_for_vote(int(input("Cual es su edad?")))
