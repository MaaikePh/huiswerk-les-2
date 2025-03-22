
# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.

# Voorbeeld:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.

nummer1 = float(input('Voer je eerste nummer in: '))
nummer2 = float(input('Voer je tweede nummer in: '))
operatie = input('Wat wil je met deze nummers doen, bijvoorbeeld +, -, * of /: ')

if operatie == '+':
    print(f'het resultaat is: {nummer1 + nummer2}')
elif operatie == '-':
    print(f'het resultaat is: {nummer1 - nummer2}')
elif operatie == '*':
    print(f'het resultaat is: {nummer1 * nummer2}')
elif operatie == '/':
    print(f'het resultaat is: {nummer1 / nummer2}')
else :
    print('Invoer ongeldig.')