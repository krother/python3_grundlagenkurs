
# Listen

In diesem Kapitel wirst Du mehrere Variablen in einer **Liste** zusammenfassen.

Um größere Datenmengen zu verarbeiten, können wir nicht für jeden Eintrag einen neuen Variablennamen ausdenken. Irgendwie muß es möglich sein, mehrere Datensätze in einer Variable zu speichern. In Python treten an dieser Stelle **Listen** auf die Bühne.

Listen sind eine einfache Abfolge von Elementen. Allerdings zählt Python anders als Menschen:

![Indizierung](../images/indexing.png)

### Aufgabe 1

Probiere einige Befehle zum Erstellen von Listen aus:

    :::python3
    zahlen = [1, 2, 4, 8, 16, 32]
    zahlen = zahlen + [64, 128, 256]

    filme = ["Star Wars", "Star Trek", "Ratatouille"]
    filme += ["Arrival"]

----

### Aufgabe 2

Was ergeben folgende Anweisungen?

    :::python3
    zahlen[4]
    filme[0]
    filme[-1]
    zahlen[-3]

----

### Aufgabe 3

Was ergeben folgende Anweisungen?

    :::python3
    filme[2:]
    filme[:2]
    zahlen[2:-2]
    zahlen[::2]

----

### Aufgabe 4

Welche Anweisungen sind korrekt?

* `daten = ["Tilda", "Swinton"]`
* `daten = ["Darth Vader" "Yoda"]`
* `daten = [1, 2 + 3, 4]`
* `daten = [1, 2] + [3, 4]`
* `daten = [1, 2] + 3, 4]`
* `daten = [1, 2.0, "drei"]`

----

### Aufgabe 5

Was tut das folgende Programm?

    :::python3
    filme = ["Star Wars", "Star Trek", "Ratatouille"]
    for f in filme:
        print(f)
