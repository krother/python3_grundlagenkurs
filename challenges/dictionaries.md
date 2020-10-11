
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

    :::python3
    d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
    print(d['fish'])

----

### Aufgabe 3

Was haben folgende Anweisungen zum Ergebnis?

    :::python3
    d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
    print('Hund' in d)

----

### Aufgabe 4

Was haben folgende Anweisungen zum Ergebnis?

    :::python3
    d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
    print(list(d.keys()))

----

### Aufgabe 5

Was haben folgende Anweisungen zum Ergebnis?

    :::python3
    d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
    print(d.get('Katze', 'unknown'))

----

### Aufgabe 6

Was haben folgende Anweisungen zum Ergebnis?

    :::python3
    d = {'cat':'Katze', 'dog':'Hund', 'fish':'Fisch'}
    d.setdefault('cat', 'Stubentiger')
    print(d['cat'])
