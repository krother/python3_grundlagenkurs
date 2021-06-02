
# Python als Taschenrechner

**🎯 Verwende Python für einfache Berechnungen.**

![](../images/taschenrechner.png)

*[Foto von Charles Deluvio auf Unsplash](https://unsplash.com/@charlesdeluvio)*

----

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Mit Zahlen rechnen |
| 💡 | Den Datentyp *Integer* verwenden |
| ⚙ | Arithmetische Operatoren verwenden |
| ⚙ | Zahlen in Variablen speichern  |
| ⚙ | Variablen verändern |
| 🔧 | den Variablen-Explorer verwenden |

----

## Arithmetik

In diesem Kapitel werden wir die Python-Kommandozeile als Taschenrechner verwenden.
Du solltest folgende Eingabeaufforderung sehen (im Konsolenfenster rechts unten):

```python
In [1]:
```

Falls dort statt der 1 schon eine andere Zahl steht, macht das nichts.

----

### Aufgabe 1: Grundrechenarten

Führe einige Berechnungen in Python durch.
Setze die fehlenden Zeichen in die Lücken ein:

```python
In [1]: 1 + ___
Out[1]: 3

In [2]: 12 ___ 8
Out[2]: 4

In [3]: ___ * 5
Out[3]: 20

In [4]: 21 / 7
Out[4]: ___

In [5]: ___ ** 2
Out[5]: 81
```

Gib die Befehle in die Konsole ein ein und beobachte was passiert.

Den ersten Teil (`In [1]` etc.) solltest Du **nicht** eingeben, der erscheint automatisch.

----

### Aufgabe 2: Divisionen

Was ist der Unterschied zwischen folgenden Anweisungen?

```python
10 / 4
10.0 / 4
10.0 / 4.0
10 // 4
10 * 0.25
```

Gib sie in der Konsole ein und untersuche das Ergebnis.

----

### Aufgabe 3: Weitere Operatoren

Welche Operationen ergeben 8?

```python
0 + 8
4 - -4
65 // 8
17 % 9
2 * 4
64 ** 0.5
```

Gib die Anweisungen ein und untersuche das Ergebnis.

----

### Aufgabe 4: Variablen

Um Zahlen und Rechenergebnisse für spätere Berechnungen aufzuheben, kannst Du sie in **Variablen** speichern.

Ergänze die Lücken:

```python
In [1]: aepfel = 25
In [2]: bananen = 7
In [3]: kirschen = 5
In [4]: aepfel
Out[4]: ______
In [5]: bananen + 1
Out[5]: ______
In [6]: 3 * kirschen
Out[6]: ______
```

----

### Aufgabe 5: Variablen verändern

Die erste Anwisung verändert den Inhalt einer Variablen aus Aufgabe 4.
Setze Werte und Variablen ein, so dass das Ergebnis stimmt:

```python
In [7]: aepfel = aepfel + 1
In [8]: aepfel
Out[8]: _____

In [9]: obst = _____ + _____ + _____
In [10]: obst
Out[10]: 38
```

Du kannst im **Variablen-Explorer** in Spyder (rechts oben) den Inhalt der Variablen direkt sehen.

----

### Aufgabe 6: Zuweisungen

Welche Zuweisungen an Variablen sind korrekt?

```python
a = 1 * 2
2 = 1 + 1
5 + 6 = y
sieben = 3 * 4
```

----

### Aufgabe 7: Kaninchen

Im April hast Du 10 Kaninchen:

```python
kaninchen = 10
```

Die Kaninchen vermehren sich ständig.
Jeden Monat kommen 20% neue Kaninchen dazu, so dass Du im Mai schon 12 hast.

**Wie viele Kaninchen sind es im Dezember?**

Es sterben keine Kaninchen, und es gibt auch keine halben Kaninchen.
Verwende Python um die Aufgabe zu lösen.

----

### Aufgabe 8: Operatoren

:::quiz operator_quiz.json
