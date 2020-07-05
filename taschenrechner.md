
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

    :::python3
    In [1]:

### Aufgabe 1: Grundrechenarten

Führe einige Berechnungen in Python durch, indem Du die fehlenden Zeichen in die Lücken einsetzt:

    :::python3
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

----

### Aufgabe 2: Divisionen

Was ist der Unterschied zwischen folgenden Anweisungen?

    :::python3
    10 / 4
    10.0 / 4
    10.0 / 4.0
    10 // 4
    10 * 0.25

----

### Aufgabe 3: Weitere Operatoren

Welche Operationen ergeben 8?

    :::python3
    0 + 8
    4 - -4
    65 // 8
    17 % 9
    2 * 4
    64 ** 0.5    

----

### Aufgabe 4: Variablen

Um Zahlen und Rechenergebnisse für spätere Berechnungen aufzuheben, kannst Du sie in **Variablen** speichern.

Ergänze die Lücken:

    :::python3
    In [1]: aepfel = 25
    In [2]: bananen = 7
    In [3]: kirschen = 5
    In [4]: aepfel
    Out[4]: ______
    In [5]: bananen + 1
    Out[5]: ______
    In [6]: 3 * kirschen
    Out[6]: ______

----

### Aufgabe 5

Ändere den Inhalt der Variablen aus Aufgabe 4, so dass das Ergebnis stimmt:

    :::python3
    In [7]: aepfel = aepfel + 1
    In [8]: aepfel
    Out[8]: _____

    In [9]: obst = _____ + _____ + _____
    In [10]: obst
    Out[10]: 38

Setze die korrekten Werte und Variablennamen ein.

----

### Aufgabe 6: Zuweisungen

Welche Zuweisungen an Variablen sind korrekt?

    :::python3
    a = 1 * 2
    2 = 1 + 1
    5 + 6 = y
    sieben = 3 * 4

----

### Aufgabe 7: Typumwandlungen

Welche `print`-Anweisungen funktionieren?

    :::python3
    print("9" + "9")
    print "neun"
    print(str(9) + "neun")
    print(9 + 9)
    print(9 + int("9"))
    print(neun)
    print(float("9") + int(9.0))

----

### Aufgabe 8: Debugging

Das folgende Programm soll den Umfang eines Kreises berechnen.
Es enthält drei Fehler.
Finde und behebe sie.

    :::python3
    pi = 3.14159
    radius = float(input('Gib den Radius ein: '))
    umfang = 2 * pi * r

    print('Der Umfang des Kreises ist ' + umfang)    
    ergebnis = 7
    print(ergebnis)    

----

## Neue Befehle und Begriffe

### Datentypen in Python

Es gibt zwei Datentypen für Zahlen in Python:

* **integer** – ganze Zahlen mit beliebiger Länge
* **float** – Fließkommazahlen mit einer Genauigkeit von 16 Ziffern

Auch **string** ist ein Datentyp.

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

### Typumwandlungen

Die Funktionen `int()`, `float()` und `str()` wandeln Datentypen ineinander um.
Eine Umwandlung in einen String ist immer möglich, die Umwandlung in eine Zahl nur wenn der String auch eine Zahl enthält.

### Laufzeitfehler

* where does the error occur?
* what type of error is it?
* --> why does it occur
* challenge: produce 3 main types from the code example: indexerror, value error, name error
