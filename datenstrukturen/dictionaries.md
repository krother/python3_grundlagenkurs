
# Grundlagen: Dictionaries

In diesem Kapitel lernst Du einen neuen Datentyp kennen: das **Dictionary**.
Dictionaries eignen sich gut zum Suchen und Nachschlagen.

----

### Aufgabe 1

Finde heraus, was jeder der Ausdrücke mit dem Dictionary in der Mitte anstellt.

![dict exercise](images/dicts.png)

----

### Aufgabe 2

Was haben folgende Anweisungen zum Ergebnis?

```python
d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
print(d['fish'])
```

----

### Aufgabe 3

Was haben folgende Anweisungen zum Ergebnis?

```python
d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
print('Hund' in d)
```

----

### Aufgabe 4

Was haben folgende Anweisungen zum Ergebnis?

```python
d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
print(list(d.keys()))
```

----

### Aufgabe 5

Was haben folgende Anweisungen zum Ergebnis?

```python
d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
print(d.get('Katze', 'unknown'))
```

----

### Aufgabe 6

Was haben folgende Anweisungen zum Ergebnis?

```python
d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
d.setdefault('cat', 'Stubentiger')
print(d['cat'])
```

----

### Aufgabe 7:

Im folgenden Programm kannst Du von Stadt zu Stadt reisen.
Leider enthält es 3 Fehler. Finde und repariere sie.

```python
staedte = {
    "New York": ["Tokyo", "Paris", "London"],
    "Poznan": ["London", "Berlin"],
    "London": ["New York", "Poznan"]
    "Berlin": ["Tokyo", "Poznan"],
    "Tokyo": ["New York", "Berlin"],
    "Paris": ["Katmandu"]
    }

standort = "Paris"

print "\nDeine Aufgabe: fliege nach Katmandu\n"

while standort not in staedte or standort == 'Katmandu':
    print(f"Du bist in {standort}")

print("Es gibt Flüge nach ", staedte[standort])
standort = input("Wohin möchtest du fliegen?")

print("Du hast dein Ziel erreicht")
```

