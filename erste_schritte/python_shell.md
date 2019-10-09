
# Python als Taschenrechner

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Mit Zahlen rechnen |
| ⚙ | Arithmetische Operatoren verwenden |
| ⚙ | Datentypen unterscheiden |
| 💡 | Die Datentypen `int` und `float` verwenden |
| 💡 | Datentypen ineinander umwandeln |
| 🐞 | Laufzeitfehler erkennen |

----

## Arithmetik

Es gibt mehrere Möglichkeiten, Python zu verwenden. Im Editor **Anaconda Spyder** findest Du rechts unten die interaktive *Python-Shell*.

In diesem Kapitel werden wir die Python-Shell als Taschenrechner verwenden. Du solltest folgende Eingabeaufforderung sehen:

    In [1]

### Aufgabe 1

Führe einige Berechnungen in Python durch, indem Du die fehlenden Zeichen in die Lücken einsetzt:

    In [1]: 1 + ___
    Out[1]: 3

    In [2]: 12 ___ 8
    Out[2]: 4

    In [3]: ___ * 5
    Out[3]: 20

    In [4]: 21 / 7
    Out[4]: ___

    In [5]: ___ ** 2
    Out[5]: 81

Gib die Befehle ein und beobachte was passiert. Gib den ersten Teil (`In [1]` etc.) **nicht** ein, dieser erscheint automatisch.


### Aufgabe 2

Was ist der Unterschied zwischen folgenden Anweisungen?

    10 / 3
    10.0 / 3
    10.0 / 3.0
    10 // 3
    round(10 / 3, 2)
    abs(-10 / 3)


### Aufgabe 3

Welche Operationen ergeben 8?

    0 + 8
    4 - -4
    65 // 8
    17 % 9
    2 * 4
    64 ** 0.5    

----

## Neue Befehle und Begriffe

### Zahlen in Python

Es gibt zwei Arten Zahlen in Python:

* **integer** – ganze Zahlen mit beliebiger Länge
* **float** – Fließkommazahlen mit einer Genauigkeit von 16 Ziffern

### Operatoren

Die Rechenzeichen zwischen den Zahlen nennt man **Operatoren**. Python kennt sieben arithmetische Operatoren:

| Operator | Beschreibung |
|----------|--------------|
| `+`      | Addition |
| `-`      | Subtraktion |
| `*`      | Multiplikation |
| `/`      | Division |
| `//`      | Division mit Abrunden |
| `%`      | Modulo (Rest der Division) |
| `**`      | Potenz |

----

## Variablen

### Aufgabe 4

Um Zahlen und Rechenergebnisse für spätere Berechnungen aufzuheben, können wir sie in **Variablen** speichern.

Ergänze die Lücken:

    In [1]: aepfel = 25
    In [2]: bananen = 7
    In [3]: kirschen = 5
    In [4]: aepfel
    Out[4]: ______
    In [5]: bananen + 1
    Out[5]: ______
    In [6]: 3 * kirschen
    Out[6]: ______

### Aufgabe 5

Ändere den Inhalt der Variablen:

    In [7]: aepfel = aepfel + 1
    In [8]: aepfel
    Out[8]: _____

    In [9]: obst = _____ + _____ + _____
    In [10]: obst
    Out[10]: 38

Setze die korrekten Werte und Variablennamen ein.

### Aufgabe 6

Probiere aus, ob folgende Variablennamen in Python erlaubt sind:

    YODA
    darth vader
    luke99
    2000imperator
    obi_wan_kenobi
    darth.maul


### Aufgabe 7

Welche Zuweisungen an Variablen sind korrekt?

    a = 1 * 2
    2 = 1 + 1
    5 + 6 = y
    sieben = 3 * 4

----

## Mathematische Funktionen

### Aufgabe 8

Führe folgende Befehle aus:

    abs(-8)
    round(4/3, 2)

### Aufgabe 9

Führe folgende Befehle aus:

    import math

    math.log(16, 2)
    math.sin(math.pi / 2)

Welche Aussagen sind korrekt?

* Das Ergebnis des Logarithmus ist `2`
* Die Funktion `sin()` arbeitet mit Winkeln im Bogenmaß
* Das
* Die math-Bibliothek enthält auch eine Funktion `sqrt()` zum Wurzeln ziehen.

### Import

Python kennt jede Menge Bibliotheken (Module), mit denen sich zusätzliche Funktionen einbinden lassen. Die `import`-Anweisung bindet eine Bibliothek ein, so dass Du sie verwenden kannst.

Jede Bibliothek muß nur einmal importiert werden. Danach ist sie so lange aktiv, bis Du Python neu startest.

### Das Modul `math`

Die Bibliothek `math` ist eine Sammlung häufig benutzter Funktionen wie trigonometrische Funktionen, Logarithmen, Wurzeln und viele mehr. Sie enthält auch einige Konstanten wie `pi` und die Eulersche Zahl `e`.

Eine Übersicht zum Modul `math` findest Du auf [docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

----

## Typumwandlungen

### Aufgabe 10

Welche `print`-Anweisungen sind korrekt?

* `print("9" + "9")`
* `print "neun"`
* `print(str(9) + "neun")`
* `print(9 + 9)`
* `print(neun)`
