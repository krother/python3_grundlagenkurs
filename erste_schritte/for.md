
# Quadratzahlen

**🎯 Berechne eine Serie von Quadratzahlen.**

![](../images/quadrate.jpg)

*[Foto von travelnow.or.crylater auf Unsplash](https://unsplash.com/@travelnow_or_crylater?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

----

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| ⚙ | `for`-Schleifen verwenden |
| ⚙ | Anweisungen einrücken |
| 💡 | Die Funktion `range()` |
| 💡 | Das Modul `time` |
| 🐞 | Laufzeitfehler erkennen |

----

### Aufgabe 1

Führe das folgende Programm aus. Was passiert?

```python
import time

for i in range(5):
    print("Du kannst schon super programmieren!")
    time.sleep(5)
```

----

### Aufgabe 2

Was tut das folgende Programm?

```python
for zahl in range(1, 7):
    print(zahl)
```

----

### Aufgabe 3

Erkläre, warum die `for`-Anweisung besser als der folgende Ansatz ist:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
```

----

### Aufgabe 4

Erkläre den Unterschied zwischen folgenden zwei Programmen:

```python
x = 1
for i in range(10):
    x = x * 2
    print(x)
```

und

```python
x = 1
for i in range(10):
    x = x * 2
print(x)

```

----

### Aufgabe 5

Schreibe eine Schleife mit `for`, welche folgende Ausgabe produziert:

```bash
1
4
9
16
25
36
49
```

----

### Aufgabe 6

Probiere folgende Schleifen aus.
Erkläre was passiert.

```python
for buchstabe in "ABCD":
    print(buchstabe)

for i in range(10):
    print(i)

for zahl in [4, 9, 16, 25]:
    print(zahl)

for x, y in [(1,2), (3,4), (5,6)]:
    print(x, y)

kaninchen = 10
for i in range(9):
     kaninchen = kaninchen + kaninchen // 5
     print(kaninchen)
```

