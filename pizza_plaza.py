# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.

print('Welkom bij de pizzeria.')
pizza_size = input('Welke maat pizza zou u graag willen? Er is keuze tussen small, medium en large:\n')
pepperoni = input('Wil u extra pepperoni op uw pizza? ja of nee: ')
kaas = input('Wil u extra kaas op uw pizza? ja of nee: ')

prijs = 0
if pizza_size == 'small':
    prijs = 15
    if pepperoni == 'ja':
        prijs = 17
elif pizza_size == 'medium':
    prijs = 20
    if pepperoni == 'ja':
        prijs = 23
elif pizza_size == 'large':
    prijs = 25
    if pepperoni == 'ja':
        prijs = 28
if kaas == 'ja':
    prijs += 1

print(f'De prijs voor deze {pizza_size} pizza is ${prijs}.')