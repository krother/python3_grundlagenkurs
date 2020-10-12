# Dein erstes Programm

| 💼 | Ein *"Hallo, Welt"*-Programm schreiben |
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

## Was ist ein Programm?

Wir müssen dem Computer irgendwie erklären, was er tun soll. Die Programmiersprache Python kann **Befehle** oder **Anweisungen** aus einer Textdatei lesen, verstehen und ausführen. Diese Textdatei nennen wir ein Programm.

Kleine Programme bestehen aus einer einzigen Datei, in der die Befehle einer nach dem anderen ausgeführt werden.

### Aufgabe 1

Schreibe Dein erstes Programm.
Dazu brauchst Du eine **Programmierumgebung** (IDLE, Spyder, VSCode, Jupyter oder eine andere).

Erstelle eine neue Datei mit folgendem Inhalt:

    :::python3
    name = input("Wie heißt Du? ")
    print("Hallo", name)

Führe das Programm aus.
Was passiert?

----

### Aufgabe 2: Mache das Programm kaputt!

Beim Programmieren ist es unvermeidlich, dass Du Fehler machst. Fehler können einfache Vertipper sein oder komplizierte logische Denkfehler. Eine der wichtigsten Fähigkeiten beim Programmieren ist, in einem fehlerhaften Programm die Ursache zu finden und zu beheben. Das kannst Du üben, indem Du das Programm absichtlich kaputt machst und schaust, was passiert.

Probiere folgende Programme mit Fehlern aus und versuche, die Fehlermeldung zu verstehen:

    name = input("Wie heißt Du? ")
    pront("Hallo", name)

    name = input("Wie heißt Du? "
    print("Hallo", name)

    name = input("Wie heißt Du? ")
    print(Hallo , name)

    x = input("Wie heißt Du? ")
    print("Hallo", x)

----

### 🐞 Syntax Error

Die Fehlermeldung `SyntaxError` bedeutet, dass Python einen Befehl überhaupt nicht versteht, weil er grammatisch falsch geschrieben ist. Es wird kein Code ausgeführt. Die Fehlermeldung gibt uns manchmal Hinweise darauf, was das Problem ist, aber oft nicht. Der wichtigste Hinweis ist die **Zeilennummer** in der Fehlermeldung, weil der Fehler immer in dieser Zeile oder darüber zu finden ist.

Ein guter Editor zeigt Dir Syntaxfehler an. In Spyder erscheinen diese nach wenigen Sekunden in der Leiste links neben dem Code.

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

### Funktionen

Eine **Funktion** ist ein vordefiniertes Unterprogramm. Funktionen rufst Du auf, indem Du den Namen der Funktion eingibst, gefolgt von runden Klammern. Manche Funktionen erfordern **Parameter** in den Klammern wie `print('Hallo')`, andere nicht.
Am Ende dieses Einsteigerkurses solltest Du die 25 wichtigsten Python-Funktionen kennen.
Du lernst hier auch, Deine eigenen Funktionen zu schreiben.

### Variablen

**Variablen** sind Speicherplätze für Daten. Jede Variable hat einen Namen, über den Du die Daten später wiederfindest. In Python erstellst Du Variablen mit dem Gleichheitszeichen `=`. Dabei steht der Name der Variablen links, und rechts das, was in der Variablen gespeichert wird.

### String

**String** (kurz `str`) ist ein **Datentyp**. Strings erlauben Dir, Text in Python-Programmen zu verwenden, in Variablen zu speichern, auszugeben usw. Strings erkennst Du an einfachen `'abc'` oder doppelten  `"abc"` Anführungszeichen.

### Wie schreibt man Programme?

Du hast in diesem Kapitel bereits mehrere Programmiertechniken kennen gelernt:

* Befehle eintippen
* Befehle verändern
* nach Programmfehlern suchen
* ein Programm ausführen und schauen was passiert

Du kannst diese Techniken zu einem einfachen Schema kombinieren:

    :::bash
    1. Editiere das Programm
    2. Führe das Programm aus
    3. Wenn es noch nicht funktioniert, zurück zu 1.

Wahrscheinlich bist Du schon von alleine darauf gekommen.

Diese Methode, der **Code-Debug-Zyklus**, ist für kleine Programme gut geeignet.
Ich erwähne diese Methode, damit Du sie später von anderen Programmiertechniken unterscheiden kannst.
