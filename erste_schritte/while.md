
# While-Schleifen

In diesem Kapitel lernst Du eine neue Möglichkeit, den *Ablauf* eines Programms (den **Kontrolfluß**) zu steuern: Die bedingte Schleife mit `while`.

### Aufgabe 1

Ordne die Ausdrücke so zu, daß die gezeigten `while`-Schleifen die angegebene Anzahl von Durchläufen vollführen.

![while exercise](../images/while.png)

----

### Aufgabe 2

Welche dieser `while`-Anweisungen sind korrekt?

```python
while a = 1:

while b == 1

while a + 7:

while len(c) > 10:

while a and (b-2 == c):

while s.find('c') >= 0:
```

----

### Aufgabe 3

Welche Aussagen sind korrekt?

* `while` wird auch eine *bedingte Schleife* genannt.
* Der Ausdruck nach `while` darf Funktionsaufrufe enthalten.
* Es ist möglich, endlose `while`-Schleifen zu schreiben.
* Das Semikolon am Ende der Zeile mit `while` ist optional.
* Der Code-Block nach einer `while`-Anweisung wird mindestens ein Mal ausgeführt.

----

### Aufgabe 4

Die folgende `for`-Schleife sucht in den Daten nach dem Wert `33`. Ersetze sie durch eine `while`-Schleife.

```python
data = [5, 7, 33, 12, 4, 3, 18]

gefunden = False
for n in data:
    if n == 33:
        gefunden = True

print("Der Wert 33 wurde gefunden: {}".format(gefunden))
```

----

### Aufgabe 5

Die folgende `while`-Schleife zählt Werte größer 10. Ersetze sie durch eine `for`-Schleife.

```python
data = [4, 7, 11, 1, 3,  15]

i, j = 0,0
while i < len(data):
    if data[i] > 10:
        j += 1
    i += 1

print("Anzahl Werte größer 10: {}".format(j))
```

----

### Aufgabe 6

Welche der folgenden `while`-Schleifen enden von alleine?

#### Aufgabe 6.1

```python
count = 0
while count > 0:
    print count
    count += 1
```

#### Aufgabe 6.2

```python
text = "a"
while "z" not in text:
    text += "a"
```

#### Aufgabe 6.3

```python
a = 7
b = 135
while a != b:
    a += (a - b) / 10.0
    b -= (a - b) / 10.0
```

#### Aufgabe 6.4

```python
n = 0
while n * 5 != n ** 2:
    n += 2
```

#### Aufgabe 6.5

```python
data = [1, 2, 7, 8]
while data[-1] > 2:
    data.pop()
```

#### Aufgabe 6.6

```python
data = [2, 3, 15]
while data[0] < 100:
    data = data[1:]
```

