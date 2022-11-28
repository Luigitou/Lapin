from entities.Garden import Garden
from datetime import date, timedelta
from utils.Graphs import printPlot, logRabbit, logCarrot

print('hi py !')

startDate = date.today()
currentDate = startDate
endDate = startDate
endDate = endDate.replace(year=startDate.year + 1)

garden = Garden()


def calcNbDayFromStart(current, start):
    return (current - start).days


def calcGraphPoints(currentGarden):
    print(currentGarden)


# Boucle principale de la simulation
# Elle fait avancer la date actuelle chaque jour jusque la date de fin de simulation
while currentDate < endDate:
    currentDate = currentDate + timedelta(days=1)

    # Ici on appelle les différentes actions pouvant survenir

    # Les lapins grandissent tous les jours
    garden.growRabbits()

    # Les lapins mangent tous les 7 jours
    if calcNbDayFromStart(currentDate, startDate) % 7 == 0:
        garden.eat()

    # Le 1er juin les carottes sont prètes et ajoutées au stock
    if currentDate.month == 6 and currentDate.day == 1:
        garden.growCarrots()

    # Tous les 180 jours (6 mois) les lapins se reproduisent ( 2 fois par an )
    if calcNbDayFromStart(currentDate, startDate) % 180 == 0 and currentDate != startDate:
        garden.reproduce()

    logRabbit(len(garden.rabbits), currentDate.strftime("%d/%m/%Y"))
    logCarrot(garden.carrots, currentDate.strftime("%d/%m/%Y"))


printPlot()
