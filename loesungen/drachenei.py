
print("""
Finde das Drachenei
===================

Du begibst dich auf die Suche.
""")

beschreibungen = {
    "Heimatstadt": """Du befindest Dich in Deiner Heimatstadt...""",
    "Eiswüste": """...""",
}

raum = "Heimatstadt"

while raum != "Lichtung":

    if raum == "Heimatstadt":
        print("""
Du befindest Dich in Deiner Heimatstadt.
Ein kleine Handelsstadt am Rande der Wüste.
""")

    raum = input("Wohin möchtest Du gehen? ")

print("""
Auf einer verborgenen Lichtung entdeckst Du das Drachenei.

Deine Suche war erfolgreich!
""")
