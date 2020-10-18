
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

----

### Aufgabe 6: Methoden von Listen

Als nächstes werden wir einige Namen in einer Liste sammeln. Das ist eine gute Gelegenheit, diesen wichtigen Datentyp etwas näher kennen zu lernen.

Finde in IPython heraus, was die Ausdrücke mit der Liste in der Mitte anstellen.

![Übung zu Listen](../images/lists.png)

----

### Aufgabe 7

Verwende die angegebenen Ausdrücke, um die Liste wie angegeben zu verändern. Verwende jeden Ausdruck genau einmal.

![list funcs exercise2](../images/list_funcs2.png)

----

### Aufgabe 8

Verwende die angegebenen Ausdrücke, um die Liste wie angegeben zu verändern. Verwende jeden Ausdruck genau einmal.

![list funcs exercise1](../images/list_funcs1.png)
