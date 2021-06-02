
# Babynamen auszählen

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Komma-separierte Daten parsen |
| 🔀 | Daten aggregieren |
| 💡 | Methoden von Strings |
| 💡 | Die Funktionen `sum()`, `max()`  und `min()` |
| 🔧 | Rohdaten im Texteditor inspizieren |
| 🐞 | Zwischenergebnisse überprüfen |

----

## Babynamen in den USA

![Babynamen](../images/baby.png)

Die US-Meldebehörden haben die Namen aller seit 1880 geborenen US-Staatsbürger registriert. Der Datensatz ist öffentlich unter [http://www.ssa.gov/oact/babynames/limits.html
](http://www.ssa.gov/oact/babynames/limits.html) zugänglich. Aus Datenschutzgründen sind nur Namen, die mindestens 5 Mal verwendet wurden, im Datensatz aufgeführt.

In diesem Kapitel werden wir einen größeren String auseinandernehmen. Dies kommt beim Analysieren von Daten immer wieder vor. Zum Üben verwenden wir folgenden mehrzeiligen String (die Daten sind ein Auszug aus dem US-Geburtenregister):

```python
bigbang = """Emily,F,12562
Amy,F,2178
Penny,F,342
Bernadette,F,129
Leonard,M,384
Howard,M,208
Sheldon,M,164
Stuart,M,82
Raj,M,41"""
```

Wir werden ausrechnen, wie viele Babys die Tabelle insgesamt enthält.

### Aufgabe 1

Wenn alle Zahlen in einer Liste wären, wäre es einfach:

```python
bigbang_zahlen = [
    12562, 2178, 342, 129,
    384, 208, 164, 82, 41
]
```

Schreibe ein Programm, das diese Zahlen aufsummiert.

----

### Aufgabe 2

Mit welcher der Methoden kannst du einen String wie die Variable `bigbang` in einzelne Zeilen zerlegen?

* `bigbang.replace("\n", " ")`
* `bigbang.split("\n")`
* `bigbang.strip()`
* `bigbang.count("\n")`

Speichere den zerlegten String in einer Variablen.

----

### Aufgabe 3

Wie viele unterschiedliche Jungennamen mit `'S'` gibt es im bigbang-Datensatz?

**Sortiere** die folgenden Programmzeilen und **rücke sie korrekt ein**:

```python
jungs = 0

print(jungs)

if ",M," in zeile and zeile[0] == 'S':

for zeile in bigbang.split():

jungs += 1
```

----

### Aufgabe 4

Um an die Anzahl heranzukommen, müssen wir die Zeilen an den Kommata aufteilen. Verwende dazu widerum die Funktion `split()`. Diesmal mußt Du als Argument in den Klammern aber ein Komma angeben, damit eine Zeile in Spalten geteilt wird.

Schreibe ein Programm, das alle Anzahlen aus dem String `bigbang` ausgibt.

----

### Aufgabe 5

Schreibe ein Programm, das die Anzahl Babys in der Variable `bigbang` zusammenzählt und die Summe ausgibt.
