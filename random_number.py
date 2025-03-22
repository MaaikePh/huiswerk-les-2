# In deze opdracht ga je een script schrijven waarbij de gebruiker een geheim getal moet raden.
#
# Stappenplan:
#
# 1. Maak een variable "random_getal" en geef deze een willekeurige integer waarde tussen 1 en 10.
# 2. Vraag de gebruiker om het getal te raden
# 3. Gebruik een while-loop die blijft draaien zolang de gebruiker het verkeerde getal raadt.
# 4. Geef feedback of de ingevoerde waarde te hoog of te laag is.
# 5. Wanneer de gebruiker het juiste getal raadt, beëindig de loop en print een felicitatiebericht.
#
# BONUS: Gebruik `import random` en `random.randomInt(1, 10)` om je geheime getal mee te maken
# en deze zo ook voor jezelf geheim te houden.

import random

random_getal = random.randint(1, 10)

nummer = int(input('Raad het getal. Welk getal kies je: '))

while nummer < random_getal:
    print('helaas je nummer is te laag. Probeer het opnieuw.')
    nummer = int(input('Welk getal kies je: '))
while nummer > random_getal:
    print('Helaas je nummer is te hoog. Probeer het opnieuw.')
    nummer = int(input('Welk getal kies je: '))
if nummer == random_getal:
    print('Gefeliciteerd, dat is het juiste nummer!')