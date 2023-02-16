def aviable_for_vote(age):
    if age >= 18:
        print("Puede votar")
    else:
        print("No puede votar")


aviable_for_vote(int(input("Cual es su edad?")))
