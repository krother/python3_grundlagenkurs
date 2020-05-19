# Dein erstes Programm

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Ein *"Hallo, Welt"*-Programm schreiben |
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

Es ist Zeit, ein erstes Programm zu schreiben:

Öffne **Spyder** und erstelle eine neue Datei mit `Strg-N`. Schreibe hinein:

    name = input("Wie heißt Du? ")
    print("Hallo", name)

Speichere die Datei anschließend unter dem Namen `hallo.py` ab.

Nun kannst Du das Programm ausführen.
In **Spyder** drückst Du dazu den *"Play"*-Knopf oder `F5`.

Was tut das Programm?

----

## Neue Befehle und Begriffe

| Begriff | Kurzbeschreibung |
|---------|------------------|
| `input` | eine Funktion, die Text von der Tastatur einliest |
| `name` | eine Variable, die Text zwischenspeichert |
| `print` | eine Funktion, die Text auf den Bildschirm ausgibt |
| `"Hallo"` | ein String (Text), der direkt ausgegeben wird |

### Funktionen

Eine **Funktion** ist ein vordefiniertes Unterprogramm. Funktionen rufst Du auf, indem Du den Namen der Funktion eingibst, gefolgt von runden Klammern. Manche Funktionen erfordern **Parameter** in den Klammern wie `print('Hallo')`, andere nicht. In diesem Übungsbuch lernst Du die 25 wichtigsten Python-Funktionen  kennen. Du lernst auch, Deine eigenen Funktionen zu schreiben.

### Variablen

**Variablen** sind Speicherplätze für Daten. Jede Variable hat einen Namen, über den Du die Daten später wiederfindest. In Python erstellst Du Variablen mit dem Gleichheitszeichen `=`. Dabei steht der Name der Variablen links, und rechts das, was in der Variablen gespeichert wird.

### String

**String** (kurz `str`) ist ein **Datentyp**. Strings erlauben Dir, Text in Python-Programmen zu verwenden, in Variablen zu speichern, auszugeben usw. Strings erkennst Du an einfachen `'abc'` oder doppelten  `"abc"` Anführungszeichen.

----

## Mache das Programm kaputt!

Beim Programmieren ist es unvermeidlich, dass Du Fehler machst. Fehler können einfache Vertipper sein oder komplizierte logische Denkfehler. Eine der wichtigsten Fähigkeiten beim Programmieren ist, in einem fehlerhaften Programm die Ursache zu finden und zu beheben. Das kannst Du üben, indem Du das Programm absichtlich kaputt machst und schaust, was passiert.

### Aufgabe 2

Probiere folgende Programme mit Fehlern aus und versuche, die Fehlermeldung zu verstehen:

    name = input("Wie heißt Du? ")
    pront("Hallo", name)

    name = input("Wie heißt Du? "
    print("Hallo", name)

    name = input("Wie heißt Du? )
    print("Hallo", name)

    name = input("Wie heit Du? ")
    print("Hallo", name)

----

### 🐞 Syntax Error

Die Fehlermeldung `SyntaxError` bedeutet, dass Python einen Befehl überhaupt nicht versteht, weil er grammatisch falsch geschrieben ist. Es wird kein Code ausgeführt. Die Fehlermeldung gibt uns manchmal Hinweise darauf, was das Problem ist, aber oft nicht. Der wichtigste Hinweis ist die **Zeilennummer** in der Fehlermeldung, weil der Fehler immer in dieser Zeile oder darüber zu finden ist.

Ein guter Editor zeigt Dir Syntaxfehler an. In Spyder erscheinen diese nach wenigen Sekunden in der Leiste links neben dem Code.

----

### Aufgabe 3

Welche `input`-Befehle funktionieren?

* `name input("gib Deinen Namen ein: ")`
* `name = input("gib eine Zahl ein: ")`
* `name = input(gib Deinen Namen ein)`
* `name = input()`

### Aufgabe 4

Welche `print`-Befehle funktionieren?

* `print "Hallo"`
* `print("Hallo", name, name)`
* `print("Hallo" + name)`
* `print("Hallo name")`
* `print(name)`

### Aufgabe 5

Schreibe 3 Möglichkeiten auf, eine Fehlermeldung zu erzeugen.

### Aufgabe 6

Schreibe ein Programm, das nach Deinem Vor- und Nachnamen fragt und beides ausgibt.

----

## Wie schreibt man Programme?

Du hast in diesem Kapitel bereits mehrere Programmiertechniken kennen gelernt:

* Befehle eintippen
* Befehle verändern
* nach Programmfehlern suchen
* das Programm ausführen und schauen was passiert

Du kannst diese Techniken zu einem einfachen Schema kombinieren:

    1. Editiere das Programm
    2. Führe das Programm aus
    3. Wenn es noch nicht funktioniert, zurück zu 1.

Wahrscheinlich bist Du schon von alleine darau gekommen. Diese Methode, der **Code-Debug-Zyklus**, ist für kleine Programme gut geeignet. Ich schreibe diese Methode trotzdem auf, damit Du sie später von anderen Programmiertechniken unterscheiden kannst.
