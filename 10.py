# Hugo, Paco y Luis son tres hermanos a los que les gusta jugar al fútbol. Como Hugo es el
# mayor, él debe jugar contra Paco y Luis. Haga un programa que reciba la cantidad de goles
# que anotó Hugo, la cantidad de goles que anotó Paco y la cantidad que anotó Luis, e
# indique cuál equipo de los dos equipos ganó.

def who_wins(hugo_scores, paco_scores, luis_scores):
    paco_team_score = paco_scores + luis_scores
    if paco_team_score > hugo_scores:
        print("Paco y Luis ganan")
    else:
        print("Hugo gana")


who_wins(10, 2, 10)
