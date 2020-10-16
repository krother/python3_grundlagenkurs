
# Typumwandlungen

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| ⚙ | Datentypen unterscheiden |
| 💡 | Die Datentypen `int` und `float` verwenden |
| 💡 | Datentypen ineinander umwandeln |
| 🐞 | Laufzeitfehler erkennen |

----

Python enthält viele Funktionen zur **Umwandlung von Datentypen**.

Hier lernst Du einige davon kennen.


### Aufgabe 1

Setze die folgenden Teile in den Code ein, so dass alle Befehle korrekt ausgeführt werden: `alter`, `int(alter)`, `name`, `str(geboren)`, `1815`

    :::python3
    name = "Ada Lovelace"
    geboren = _____
    ____ = "37"

    text = ____ + " kam im Jahr " + _____ + " zur Welt."
    jahr = geboren + _____
    print(text)
    print(jahr)

----

### Aufgabe 2

Ergänze die folgenden Anweisungen durch `int()` oder `str()`, so daß sie alle funktionieren.

    :::python3
    9 + 9
    9 + '9'
    '9' + '9'
    9 * '9'

----

### Aufgabe 3

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

### Aufgabe 4: Debugging

Das folgende Programm soll den Umfang eines Kreises berechnen.
Es enthält zwei Fehler.
Finde und behebe sie.

    :::python3
    pi = 3.14159
    radius = input('Gib den Radius ein: ')
    umfang = 2 * pi * r

    print("Der Umfang des Kreises ist " + umfang)    
