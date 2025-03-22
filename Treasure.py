# Je gaat een nieuw programma schrijven, genaamd Treasure.py. Dit programma is een spel waarbij de speler een aantal keuzes moet maken.
# Je mag zelf bepalen wat de keuzes zijn en wat de uitkomsten zijn van de keuzes. Het spel moet minimaal 4 verschillende keuzes bevatten.
# Het einde van het spel is een if elif else statement.
#
# Voorbeeld:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Rechts
#  Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.
#
# Of:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Links
# Je komt bij een meer, ga je zwemmen of wachten?
# etc...

# print("""
#                   __..-----')
#         ,.--._ .-'_..--...-'
#        '-"'. _/_ /  ..--''""'-.
#        _.--""...:._:(_ ..:"::. \\
#     .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
#    /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
#    "  / |  :' :/""\\///)  /:.'    --(       )--
#      / :( :( :(   (#//)  "       .-'\\.___./'-.
#     / :/|\\ :\\_:\\   \\#//\\            /  |  \\
#     |:/ | ""--':\\   (#//)              '
#     \\/  \\ :|  \\ :\\  (#//)
#          \\:\\   '.':. \\#//\\
#           ':|    "--'(#///)
#                      (#///)
#                      (#///)         ___/""\\
#                       \\#///\\           oo##
#                       (##///)         `-6 #
#                       (##///)          ,'`.
#                       (##///)         // `.\\
#                       (##///)        ||o   \\\\
#                        \\##///\\        \\-+--//
#                        (###///)       :_|_(/
#                        (sjw////)__...--:: :...__
#                        (#/::''':::     "" - -.._
#                   __..-'''           __;: :            "-._
#           __..--""                  `---/ ;                '\\._
#  ___..--""                             `-'                    "-..___
#    (_ ""---....___                                     __...--"" _)
#      ""--...  ___""'''-----......._______......----""'     --""
#                           ---.....   ___....----
# """)
#

# Schrijf hier je code:
print('Welkom bij de zoektocht naar de schat op het eiland.')
keuze1 = input('Je bent aangekomen op het strand. Wil je langs de kust blijven lopen of ga je het bos in? Kies kust of bos:\n')

if keuze1 == 'kust':
    print('Je blijft in rondjes langs de kust lopen en komt nooit bij de schat uit. Game Over.')

elif keuze1 == 'bos':
    keuze2 = input('Je bent het bos ingegaan. Wil je linksaf of rechtsaf? Kies links of rechts:\n')
    if keuze2 == 'rechts':
        print('Je bent in een gat gevallen. Game over.')
    elif keuze2 == 'links':
        keuze3 = input('Je gaat linksaf. Je komt nu een tempel en een brug tegen. Welke kant ga je op? Kies tempel of brug:\n')
        if keuze3 == 'tempel':
            print('Je raakt verdwaald in het donker in de tempel. Je komt er nooit meer uit. Game over.')
        elif keuze3 == 'brug':
            keuze4 = input('Je steekt de brug over. Je ziet in de verte een gestrand schip en een boomhut. Welke kies je? Kies schip of boomhut:\n')
            if keuze4 == 'boomhut':
                print('Je klimt in de boomhut. Helaas kraakt alles en val je een moment later met boomhut en al op de grond. Game over.')
            elif keuze4 == 'schip':
                print('Je betreed het schip. Binnenin vind je de schat. Je hebt gewonnen!')
else :
    print('Dat is niet de juiste keuze. Game over.')
