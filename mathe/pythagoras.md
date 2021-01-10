
# Pythagoras

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Mathematische Berechnungen durchführen |
| 🔀 | Ein Programm in Eingabe, Verarbeitung und Ausgabe strukturieren |
| ⚙ | Ein Modul importieren |
| 💡 | Die Funktion `abs()` und `round()` aufrufen |
| 🔧 | Funktionen in der Dokumentation nachschlagen |

----

### Aufgabe 1: Mathematische Berechnungen

Mit Den Funktionen `input()`, `print()` und `int()` kannst Du ein interaktives Rechenprogramm schreiben. Das folgende Beispielprogramm enthält noch 3 Fehler. Behebe sie:

    :::python3
    a = input("Gib die erste Zahl ein: ")
    b = input("Gib die zweite Zahl ein: ")

    summe = a + b

    print(f'Die Summe der Zahlen lautet: summe')

----

### Aufgabe 2: Absolute Zahlen

Ändere den Verarbeitungsteil, so dass die positive Differenz beider Zahlen berechnet wird. Verwende dazu die Funktion `abs()`:

    :::python3
    print(abs(-1.23))

### Aufgabe 3: Das Modul math

Nun werden wir anspruchsvollere Berechnungen durchführen.
Dazu brauchst Du das Modul `math`. Es enthält nützliche *Konstanten* und *Funktionen*.
Hier ist als Beispiel eine Kreisberechnung:

    :::python3
    import math

    radius = 5.0
    inhalt = math.pi * math.pi(radius)
    print("Flächeninhalt: ", inhalt)

Finde über die [Dokumentation des math Moduls](https://docs.python.org/3/library/math.html) heraus, was es für Funktionen gibt. Probiere mindestens eine davon aus.

----

### Aufgabe 4: Runden

Verwende die Funktion `round()`, um das Ergebnis aus Aufgabe 3 auf zwei Nachkommastellen zu runden.

Beispiel:

    :::python3
    print(round(1.234, 2))


----

### Aufgabe 5: Pythagoras

Schreibe ein Programm, das die Hypotenuse eines rechtwinkligen Dreiecks berechnet.

Teile das Programm in Eingabe, Verarbeitung und Ausgabe auf:

* Lies im Eingabeteil die Länge der zwei Katheten ein
* Verwende zur Berechnung die Funktion `math.sqrt()`
* Gib das Ergebnis auf den Bildschirm aus
