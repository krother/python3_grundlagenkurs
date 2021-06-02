
# Funktionen plotten

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Funktionen plotten |
| 🔀 | Eine Liste transformieren |
| 💡 | Listen erstellen |
| 💡 | Die Funktionen `range()` und `len()` verwenden |
| 💡 | Achsen definieren und beschriften |
| 🐞 | Die Länge von Listen prüfen |

----

![](../images/plot.png)

In diesem Kapitel verwenden wir die Bibliothek `matplotlib`, um  einfache Diagramme zu erzeugen und Funktionen zu plotten.

----

### Aufgabe 1

Führe folgendes Programm aus:

```python
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, -3, 9]

plt.plot(x, y)
```

----

### Aufgabe 2

Ersetze `plot` nacheinander durch folgende Funktionen:

* `bar(x, y)`
* `scatter(x, y)`
* `pie(x)`

----

### Aufgabe 3

Folgendes Programm enthält einen Fehler. Finde und behebe ihn.

```python
from matplotlib import pyplot as plt

plt.scatter([4, 2, 4], [4, 4, 2, 2])
```

----

### Aufgabe 4

Fülle die Lücken im Programm, um eine *Parabel* zu zeichnen:

```python
from ____ ____ pyplot as ____

x = ____
y = []

for i in ____(-10, 10):
    x.append(i)
    y.append(____)

plt.____(x, y)
```

----

### Aufgabe 5

Schreibe ein Programm, das eine Sinusfunktion zeichnet. Verwende die Funktion:

```python
import math

rad = 3.14159
math.sin(rad)
```

#### Hinweis:

Um eine hohe Auflösung zu erhalten, kannst Du `range` bis 100 oder mehr laufen lassen und bei der Berechnung des Winkels durch 10 oder mehr teilen.
