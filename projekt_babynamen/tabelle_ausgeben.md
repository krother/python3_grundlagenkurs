
# Tabellen ausgeben

In diesem Kapitel werden wir unsere Ergebnisse in eine **Datei schreiben**. Nicht nur das, wir möchten sie auch **als Tabelle formatieren**.


## Dateien Schreiben

### Aufgabe 1

Bilde Paare aus Python-Anweisungen und deren Bedeutungen.

![file exercise](../exercises/files.png)


### Aufgabe 2

Führe das folende Programm aus. Erkläre was passiert.

    namen = ['Adam', 'Bob', 'Charlie']

    with open('jungs.txt', 'w') as f:
        for name in namen:
            f.write(name + '\n')

Welche Aussagen sind korrekt?

* Es werden drei Zeilen in die Datei geschrieben
* Die Datei entsteht im aktuellen Arbeitsverzeichnis
* Es werden zwei Dateien geschrieben: "jungs.txt" und "w"
* Am Ende des <code>with</code>-Blocks wird die Datei automatisch geschlossen
* An jeden Namen wird der Buchstabe 'n' angehängt


### Aufgabe 3

Lösche das `+ '\n'` aus dem Programm und führe es noch einmal aus. Was passiert?


## Tabellen

Daten treten häufig in Form von Tabellen auf. Da eine Liste andere Listen enthalten kann, können wir diese **verschachtelte Listen** als einfaches Tabellenformat nutzen:

    # Name, Babys Kalifornien, Babys New York
    tab = [
      ["Emily", 2269, 881],
      ["Amy", 542, 179],
      ["Penny", 54, 12],
      ["Bernadette", 21, 11]
    ]

Technisch ist an verschachtelten Listen nichts besonderes. Man muss allerdings die richtigen eckigen Klammern für die Indizierung finden, z.B. für die zweite Spalte der dritten Zeile:

    print(tab[2][1])


### Aufgabe 4

Gib alle Namen aus der obigen Tabelle mit einer `for`-Schleife aus.

### Aufgabe 5

Um Tabellen und andere Daten hübsch auszugeben, benötigen wir **String-Formatierung**.

Probiere folgende Ausdrücke in der Python Shell aus:

    "{}".format("Hallo")
    "{} {}".format("Hallo", "Welt")
    "{:10}".format("Hallo")
    "{:>10}".format("Hallo")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "Ergebnis: {:6.3f}".format(3.14159)

Welche Aussagen sind korrekt?

* Die geschweiften Klammern dienen als Platzhalter
* Die Argumente der Funktion `format()` werden in die Platzhalter eingesetzt
* Außer den Platzhaltern darf der String keinen Text enthalten
* `{:xd}` ist ein Platzhalter für eine ganze Zahl mit x Stellen
* correct>Strings lassen sich rechts- und linksbündig ausgeben
* `{:4.1f}` ist ein Platzhalter für eine Fließkommazahl mit vier Stellen vor und einer nach dem Komma
* Die geschweiften Klammern werden mit ausgegeben


### Aufgabe 6

Gib die Tabelle aus Aufgabe 3 formatiert aus.


### Aufgabe 7

Schreibe die formatierte Tabelle in eine Datei.


## Hilfsfunktionen zum Arbeiten mit Listen

In Python gibt es zahlreiche Funktionen, die eine die Arbeit mit Listen erleichtern. Neben `len()` und `range()` sind vor allem die Funktionen `enumerate()`, `sum()` und `zip()` sind in der Praxis unentbehrlich.


### Aufgabe 8

Das folgende Programm soll Namen und dazugehörige Anzahlen paarweise ausgeben.
Leider enthält das Programm **drei Defekte**. Finde und behebe diese.

    namen = ["Emma", "Olivia" "Sophia", "Isabella",
             "Ava", "Mia", "Emily"]

    anzahlen [20799, 19674, 18490, 16950,
               15586, 13442, 12562]

    if len(namen) == len(anzahlen):
       print("Achtung: die Listen sind unterschiedlich lang!")
       print(len(namen), len(anzahlen))

    for name, anzahl in zip(namen, anzahlen):
        print("{:10s} {:6d}".format(namen, anzahl))


### Aufgabe 9

Vereinfache das folgende Programm:

    anzahlen = [356, 412, 127, 8, 32]

    gesamt = 0
    for anz in anzahlen:
        gesamt += anz
    print(gesamt)


Die Funktion `sum(x)` akzeptiert eine Liste mit Zahlen als Argument.


### Aufgabe 10

Vereinfache das folgende Programm:

    namen = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']
    anzahlen = [356, 412, 127, 8, 32]

    tabelle = []
    i = 0
    while i < len(namen):
        row = (namen[i], anzahlen[i])
        tabelle.append(row)
        i += 1
    print(tabelle)


Die Funktion `zip(x, y)` führt zwei (oder mehr) Listen elementweise zusammen. Verwende eine `for`-Schleife oder `list()`, um das Ergebnis als Liste zu erhalten.


### Aufgabe 11

Vereinfache das folgende Programm:

    namen = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']

    i = 0
    for name in namen:
        print(i, name)
        i += 1

Die Funktion `enumerate(x)` generiert einen Zähler zu einer Liste. Eine übliche Schreibweise ist `for i, elem in enumerate(x)`


### Aufgabe 12

Sortiere die Tabelle nach der zweiten Spalte. Verwende folgenden Codeschnipsel:

    from operator import itemgetter

    tab.sort(key=itemgetter(spaltennr))


#### Anmerkung:

Spätestens an dieser Stelle werden verschachtelte Listen etwas schwerfällig. Mit den Bibliotheken `numpy` und `pandas` werden diese Sachen leichter.
