# Costa Rica tiene las fronteras cerradas para todas personas que provienen del exterior
# debido a la pandemia, salvo aquellas cuya nacionalidad es costarricense. El programa
# recibe como entrada la nacionalidad de la persona.

def aduanas(nation):
    if nation != "CostaRica":
        print("No puede pasar")
    else:
        print("Puede pasar")


aduanas(input("Cual es su nacionalidad"))
