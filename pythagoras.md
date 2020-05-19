
# Pythagoras

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Mathematische Berechnungen durchführen |
| 🔀 | Ein Programm in Eingabe, Verarbeitung und Ausgabe strukturieren |
| ⚙ | Ein Modul importieren |
| 💡 | Die Funktionen `abs()` und `round()` aufrufen |
| 🔧 | Funktionen in der Dokumentation nachschlagen |
| 🐞 | Fehlermeldungen lesen |

----

### Aufgabe 1: Mathematische Berechnungen

Mit Den Funktionen `input()`, `print()` und `int()` kannst Du ein interaktives Rechenprogramm schreiben. Das folgende Beispielprogramm enthält noch 3 Fehler. Behebe sie:

    a = input("Gib die erste Zahl ein: ")
    b = input("Gib die zweite Zahl ein: ')

    summe = a + b

    print(f'Die Summe der Zahlen lautet: summe')


### Aufgabe 2: Eingabe-Verarbeitung-Ausgabe

![Eingabe-Verarbeitung-Ausgabe](../images/IPO.png)

Jedes Programm besteht aus drei Teilen: **Eingabe, Vearbeitung und Ausgabe**. Um sinnvoll Programme zu schreiben, mußt Du Dir mindestens über diese drei Teile im Klaren sein. Es hilft oft, sich aufzuschreiben, worin die Eingabe, Verarbeitung und Ausgabe genau besteht. Im obigen Beispiel sind die drei Teile als Absätze gut erkennbar:

| Programmteil | Beschreibung |
|--------------|--------------|
| Eingabe      | liest zwei Zahlen von der Tastatur ein |
| Verarbeitung | addiert beide Zahlen |
| Ausgabe      | gibt die Summe auf dem Bildschirm aus |

Sammle weitere Geräte/Möglichkeiten, die ein Programm für die Ein- und Ausgabe verwenden könnte (auch wenn Du sie noch nicht in Python ansprechen kannst).

### Aufgabe 3: Absolute Zahlen

Ändere den Verarbeitungsteil, so dass die positive Differenz beider Zahlen berechnet wird. Verwende dazu die Funktion `abs()`:

    :::python
    print(abs(-1.23))

### Aufgabe 4: Das Modul math

Nun werden wir anspruchsvollere Berechnungen durchführen.
Dazu brauchst Du das modul `math`. Es enthält nützliche *Konstanten* und *Funktionen*.
Hier ist als Beispiel eine Kreisberechnung:

    import math

    radius = 5.0
    inhalt = math.pi * math.pi(radius)
    print("Flächeninhalt: ", inhalt)

Finde über die [Dokumentation des math Moduls](https://docs.python.org/3/library/math.html) heraus, was es für Funktionen gibt. Probiere mindestens eine davon aus.

----

### Aufgabe 5: Runden

Verwende die Funktion `round()`, um das Ergebnis aus Ausgabe 4 auf zwei Nachkommastellen zu runden.

**Hinweis:** Die Funktion `round()` ist nicht Bestandteil der `math`-Bibliothek.

----

### Aufgabe 6: Pythagoras

Schreibe ein Programm, das die Hypotenuse eines rechtwinkligen Dreiecks berechnet.

Teile das Programm in Eingabe, Verarbeitung und Ausgabe auf:

* Lies im Eingabeteil die Länge der zwei Katheten ein
* Verwende zur Berechnung die Funktion `math.sqrt()`
* Gib das Ergebnis auf den Bildschirm aus
