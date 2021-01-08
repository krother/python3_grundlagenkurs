
# Ada Lovelace

**🎯 Berechne das Alter von Ada Lovelace, der ersten Programmiererin.**

![](../images/ada.jpg)

[Ada Lovelace, Bild von Alfred Edward Chalon - Biography.com, Gemeinfrei](https://commons.wikimedia.org/w/index.php?curid=25519820)

----

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| ⚙ | Datentypen unterscheiden |
| 💡 | Den Datentyp `float` verwenden |
| 💡 | Datentypen ineinander umwandeln |
| 🐞 | Laufzeitfehler erkennen |

----

Python enthält viele Funktionen zur **Umwandlung von Datentypen**.

Mit den Funktionen `int()`, `float()` und `str()` lassen sich Zahlen und Strings ineinander umwandeln.

----

### Aufgabe 1: Ada Lovelace

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

### Aufgabe 2: Neun und neun

Ergänze die folgenden Anweisungen durch `int()` oder `str()`, so daß sie alle funktionieren.

    :::python3
    9 + 9
    9 + '9'
    '9' + '9'
    9 * '9'

----

### Aufgabe 3: Ausgabe

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

Das folgende Programm soll das Alter von Ada in einem einzugebenden Jahr berechnen.
Es enthält drei Fehler.
Finde und behebe sie.

    :::python3
    geburtsjahr = 1815
    jahr = input('Welches Jahr schreiben wir? ')
    alter = geburtsjahr - jahr

    print("Ada Lovelace wäre heute " + alter + "  Jahre alt.")    
