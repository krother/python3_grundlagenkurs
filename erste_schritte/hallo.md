# Hallo Welt

**🎯 Schreibe ein "Hallo, Welt"-Programm**

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💡 | Den Datentyp *String* verwenden |
| 💡 | Die Funktionen `print()` und `input()` aufrufen |
| ⚙ | Text in einer Variablen speichern |
| 🔧 | Befehle eingeben |
| 🔧 | Befehle verändern |
| 🐞 | Syntaxfehler erkennen |

----

### Aufgabe 1:  Dein erstes Programm

Schreibe Dein erstes Programm.

Erstelle eine neue Datei im **Editorfenster** und tippe folgende Anweisungen ein:

    :::python3
    name = input("Wie heißt Du? ")
    print("Hallo", name)

Führe das Programm aus über die Schaltfläche **"Ausführen"** oder **F5** aus.

Was passiert?

----

### Aufgabe 2: Mache das Programm kaputt!

Beim Programmieren ist es unvermeidlich, dass Du Fehler machst. Fehler können einfache Vertipper sein oder komplizierte logische Denkfehler. Eine der wichtigsten Fähigkeiten beim Programmieren ist, in einem fehlerhaften Programm die Ursache zu finden und zu beheben. Das kannst Du üben, indem Du das Programm absichtlich kaputt machst und schaust, was passiert.

Probiere nacheinander folgende Programme mit Fehlern aus und versuche, die Fehlermeldung zu verstehen:

    name = input("Wie heißt Du? ")
    pront("Hallo", name)

    name = input("Wie heißt Du? "
    print("Hallo", name)

    name = input("Wie heißt Du? ")
    print(Hallo , name)

    x = input("Wie heißt Du? ")
    print("Hallo", x)

Was hilft Dir, den Fehler zu erkennen?

----

### Aufgabe 3: input

Welche der folgenden `input`-Befehle funktionieren?
Probiere sie aus.

* `name input("gib Deinen Namen ein: ")`
* `name = input("gib eine Zahl ein: ")`
* `name = input(gib Deinen Namen ein)`
* `name = input()`

----

### Aufgabe 4: print

Welche der folgenden `print`-Befehle funktionieren?
Probiere sie aus.

* `print "Hallo"`
* `print("Hallo", name, name)`
* `print("Hallo" + name)`
* `print("Hallo name")`
* `print(name)`

----

### Aufgabe 5: Variablennamen

Probiere aus, welche der folgenden Variablennamen in Python erlaubt sind:

    :::python3
    YODA = 'jedi'
    darth vader = 'sith'
    luke99 = 'jedi' = 'sith'
    2000imperator = 'sith'
    obi_wan_kenobi = 'jedi'
    darth.maul = 'sith'

----

### Aufgabe 6: Debugging

Das folgende Programm soll ein Lied von Bob Marley ausgeben.
Es enthält drei Fehler.

Finde und repariere sie.

    :::python3
    teil1 = "Don't worry about a thing"
    teil2 = "Cause every little thing"
    teil3 = gonna be all right

    text = "teil1 + teil2 + teil3"
    print(text

----

### Aufgabe 7

Schreibe ein Programm, das nach Deinem Vor- und Nachnamen fragt und beides ausgibt.

----

## Neue Befehle und Begriffe

| Begriff | Kurzbeschreibung |
|---------|------------------|
| `input` | eine Funktion, die Text von der Tastatur einliest |
| `name` | eine Variable, die Text zwischenspeichert |
| `print` | eine Funktion, die Text auf den Bildschirm ausgibt |
| `"Hallo"` | ein String (Text), der direkt ausgegeben wird |
