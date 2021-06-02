
# Schere-Stein-Papier

**🎯 Schreibe ein Schere-Stein-Papier-Spiel.**

![](../images/Rock-paper-scissors_de.svg)

[Bild von Enzoklop, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=27958795)

----

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Ein *"Schere-Stein-Papier"*-Spiel schreiben |
| ⚙ | Verzweigungen mit `if` schreiben |
| ⚙ | Vergleichsoperatoren verwenden |
| 💡 | Den Datentyp `bool` verwenden |
| 🔀 | Zustandsvariablen verwenden |
| 🐞 | Einrückungsfehler erkennen |

----

Ein wichtiges Strukturelement in Programmen ist das *Treffen von Entscheidungen*.

In Python gibt es für Entscheidungen (Verzweigungen) die `if`-Anweisung. Darum geht es in diesem Kapitel.

----

### Aufgabe 1: Entscheidung

Mit der `if`-Anweisung kannst Du im Programm Entscheidungen treffen.

Teste das folgende Programm mit unterschiedlichen Eingaben:

```python
spieler = input("Bitte gib S, T oder P (für [S]chere, S[T]ein und [P]apier ein ")
computer = "P"

if spieler == computer:
    print("Unentschieden")
```

----

### Aufgabe 2: Alternative Entscheidungen

Setze die Begriffe `elif`, `else` und `if` in das folgende Programm ein, so dass es läuft:

```python
import random

spieler = input("Bitte gib S, T oder P (für [S]chere, S[T]ein und [P]apier ein ")
computer = random.choice('STP')

____ spieler == 'S' and computer == 'P':
    print("Computer gewinnt")
____ spieler == 'S' and computer == 'T':
    print("Spieler gewinnt")
____:
    print("Unentschieden")
```

----

### Aufgabe 3: Papier

Erweitere das Programmm so, dass es auch funktioniert, wenn der Spieler *Papier* wählt.

----

### Aufgabe 4: Debugging

Repariere je einen Fehler in folgenden if-Anweisungen:

```python
elif spieler.upper() not in 'STP':
    print('Ungültige Eingabe. Bitte wähle S,T oder P.')

elif spieler == computer
    print('Du hast das gleiche wie ich gewählt')

if spieler = 'S':
    print('Du hast "Schere" gewählt')

else:
print('Du hast etwas anderes als "Schere" gewählt')
```

----

### Aufgabe 5: Ausdrücke

Welche Vergleichsausdrücke in diesen if-Anweisungen ergeben `wahr`:

```python
a = 3
b = 4
c = 7

if a + b < c:
    print("wahr")

if a + b == 5 + 2:
    print("wahr")

if a * b == 12 and b * c == 28:
    print("wahr")

if a + b * c >= 28:
    print("wahr")

if a + b == "7":
    print("wahr")
```

----

### Aufgabe 6: Zustandsvariablen

Das folgende Programm speichert einen Vergleichsausdruck in einer Variablen vom Typ `bool`.
Vervollständige den Code:

```python
spieler_gewinnt = (spieler == "S" and computer == "P") \
               or (spieler == "P" and ...) \
               or (...)

if spieler_gewinnt:
    print('Du hast gewonnen')
```

----

### Aufgabe 7: Verschachtelte if-Anweisungen

Ergänze das folgende Programm, so dass es alle Fälle abdeckt:

```python
gewinnt = 'unentschieden'

if spieler == "S":
    if computer == "P":
        gewinnt = "Spieler"
    elif computer == "T":
        gewinnt = "Computer"

elif spieler == "P":
    ...

print("Der Gewinner ist:", gewinnt)
```

----

### Aufgabe 8: Schere-Stein-Papier

Vollende das Schere-Stein-Papier-Spiel.

#### Optionale Ziele:

* berücksichtige Unentschieden als Möglichkeit
* sowohl Gross- als auch Kleinbuchstaben sind als Eingabe möglich
* verwende einen einzigen `if..elif..else` Block
* erweitere das Spiel durch [Eidechse und Spock](https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons)
* verwende Zustandsvariablen, so dass nur eine einzige `if`-Anweisung (ohne `elif` oder `else`) übrig bleibt
