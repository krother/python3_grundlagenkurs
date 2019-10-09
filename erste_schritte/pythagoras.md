
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

## Codebeispiel

    a = float(input("length of edge a: "))
    b = float(input("length of edge b: "))
    c = float(input("length of edge c: "))

    if a ** 2 + b ** 2  == c ** 2:
        print("This is a straight-edged triangle.")
    else:
        print("This is not a straight-edged triangle.")
