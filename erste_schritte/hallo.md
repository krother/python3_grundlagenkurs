# Dein erstes Programm

In diesem Kapitel lernst Du:

* Ein Programm mit **Spyder** auszuführen
* Text in einer String-Variablen zu speichern
* Strings mit `input()` einzulesen
* Strings mit `print()` auszugeben
* Python-Befehle zu verändern
* Tippfehler zu suchen

----

## Was ist ein Programm?

Wir müssen dem Computer irgendwie erklären, was er tun soll. Die Programmiersprache Python kann **Befehle** oder **Anweisungen** aus einer Textdatei lesen, verstehen und ausführen. Diese Textdatei nennen wir ein Programm.

Kleine Programme bestehen aus einer einzigen Datei, in der die Befehle einer nach dem anderen ausgeführt werden. Große Programme können aus Hunderten Dateien bestehen, und Python springt beim Ausführen zwischen diesen wild umher. In Kapitel 1-9 beschäftigen wir uns aber erst einmal mit ganz einfachen Programmen.

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

**String** (kurz `str`) ist ein **Datentyp**. Strings erlauben uns, Text in Python-Programmen zu verwenden, in Variablen zu speichern, auszugeben usw. Strings erkennst Du an einfachen `'abc'` oder doppelten  `"abc"` Anführungszeichen.

----

## Wir machen das Programm kaputt!

Beim Programmieren ist es unvermeidlich, dass Du Fehler machst. Fehler können logische Denkfehler sein, oder einfache Vertipper. Eine der wichtigsten Fähigkeiten beim Programmieren ist, in einem fehlerhaften Programm die Ursache zu finden und zu beheben. Das werden wir üben, indem wir das Programm absichtlich kaputt machen und schauen, was passiert.

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

### Syntax Error

Die Fehlermeldung `SyntaxError` bedeutet, dass Python einen Befehl überhaupt nicht versteht, weil er grammatisch falsch geschrieben ist. Es wird kein Code ausgeführt. Die Fehlermeldung gibt uns manchmal Hinweise darauf, was das Problem ist, aber oft nicht. Der wichtigste Hinweis ist die **Zeilennummer** in der Fehlermeldung, weil der Fehler immer in dieser Zeile oder darüber zu finden ist.

### Aufgabe 3

Schreibe 5 Möglichkeiten auf, einen `SyntaxError` zu erzeugen.

----

## Übungen

### Aufgabe 4

Welche `input`-Befehle funktionieren?

* `name input("gib Deinen Namen ein: ")`
* `name = input("gib eine Zahl ein: ")`
* `name = input(gib Deinen Namen ein)`
* `name = input()`

### Aufgabe 5

Welche `print`-Befehle funktionieren?

* `print "Hallo"`
* `print("Hallo", name, name)`
* `print("Hallo" + name)`
* `print("Hallo name")`
* `print(name)`

### Aufgabe 6

Schreibe ein Programm, das nach Deinem Vor- und Nachnamen fragt und beides ausgibt.

### Aufgabe 7

Verändere das Programm selbst und untersuche was passiert. Deckt sich das Ergebnis mit Deinen Erwartungen?

### Aufgabe 8

Nicht alle Fehler erzeugen einen `SyntaxError`. Welche anderen Fehlermeldungen hast Du erhalten?
