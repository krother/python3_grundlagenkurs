# Dein erstes Programm

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Ein *"Hallo, Welt"*-Programm schreiben |
| ⚙ | Text in einer Variablen speichern |
| 💡 | Den Datentyp *String* verwenden |
| 💡 | Die Funktionen `print()` und `input()` aufrufen |
| 🔧 | Python-Befehle verändern |
| 🐞 | Syntaxfehler erkennen |

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

----

## Wie schreibt man Programme?

Du hast in diesem Kapitel bereits mehrere wichtige Programmiertechniken kennen gelernt:

* Befehle eintippen
* Programmfehler ansehen und reparieren
* Code verändern und schauen was passiert

Du kannst mit diesen Techniken Programme nach der folgenden Methode, dem **Code-Debug-Zyklus**, entwickeln:

    1. Editiere den Programmcode
    2. Führe das Programm aus
    3. Wenn noch nicht alles funktioniert, zurück zu 1.


Als Anfänger kannst Du mit dem Code-Debug-Zyklus bereits erfolgreich ganz kleine Programme schreiben.

### Wenn die Methode versagt

Ganz oft wird der Code-Debug-Zyklus aber versagen. Dieser Fall ist viel interessanter. Folgendes kann passsieren:

* Du probierst viele Möglichkeiten aus. Nichts davon funktioniert. Du wiederholst den Zyklus viele Male, ohne nennenswerte Fortschritte zu erzielen.
* Du quälst Dir einzelne Programmzeilen mühsam aus den Fingern. Eine Runde im Zyklus dauert sehr lange.
* Du grübelst ewig über Deinen Code nach. Du gelangst zu keinem klaren Ergebnis. Der Zyklus kommt zum Stillstand.

Was kannst Du in diesem Falle tun?

### Was machen erfahrene Programmierer?

Auch erfahrene Programmierer verwenden den Code-Debug-Zyklus, und bringen mitunter Erstaunliches zustande. Aber erfahrene Programmierer kennen mehr als eine Methode, Programme zu schreiben. Wenn eine nicht funktioniert, schalten sie zu einer anderen Methode um.

Der **Code-Debug-Zyklus** ist eine *Improvisationstechnik*. Diese Methode funktioniert nur bei Programmieraufgaben, bei denen Du die Grundlagen halbwegs sicher beherrschst. Es ist eine gute Methode zum Üben, Wiederholen und Festigen von Grundlagen, aber eine schlechte zum Lösen von wirklich schwierigen Aufgaben (was immer das von Deinem Standpunkt aus ist).


### Aufgabe 6

Schreibe ein Programm, das nach Deinem Vor- und Nachnamen fragt und beides ausgibt.

### Aufgabe 7

Baue kleine Fehler in das Programm ein und versuche, nacheinander folgende Fehlermeldungen zu erzeugen:

    SyntaxError
    NameError
    ValueError
    TypeError

## Syntaxfehler erkennen

syntax highlighting
