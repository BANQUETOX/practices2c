# Haga un programa que reciba dos números e imprima si el primer número es divisible entre
# el segundo, o no.
def divisible(first_number, second_number):
    if first_number % second_number == 0:
        print("Si es divisible")
    else:
        print("No es divisible")


divisible(10, 70)
