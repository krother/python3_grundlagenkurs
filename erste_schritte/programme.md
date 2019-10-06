
# Schildkrötengrafik

### Aufgabe 1

Führe das folgende Programm aus:

    import turtle

    turtle.forward(100)
    turtle.left(50)
    turtle.forward(100)


### Aufgabe 2

Erkläre das folgende Programm:

    import turtle

    strecke = 100
    turtle.forward(strecke)
    turtle.left(90)
    strecke = strecke - 50
    print(strecke)
    turtle.forward(strecke)


### Aufgabe 3

Zeichne ein Quadrat:

![](../images/square.svg)


### Aufgabe 4

Zeichne ein Dreieck:

![](../images/triangle.svg)


### Aufgabe 5

Zeichne das Haus vom Nikolaus. Eine Wurzel kannst Du mit dem Modul `math` berechnen:

    import math

    vier = math.sqrt(16)

![](../images/nikohaus.svg)

### Aufgabe 6

Schreibe ein Programm, bei dem der Nutzer die Größe des gezeichneten Quadrats einstellen kann. Du kannst eine Zahl mit folgendem Befehl einlesen:

    zahl = int(input("Gib eine Zahl ein: "))
    print(zahl)

----

## Wiederholung: for-Schleifen

### Aufgabe 7

Zeichne vier Quadrate:

![](../images/four_squares.svg)


### Aufgabe 8

Zeichne konzentrische Quadrate. Du kannst mit `turtle.up()` und `turtle.down()` das Zeichnen aus- und anschalten.

![](../images/concentric.svg)

### Aufgabe 9

Zeichne eine Spirale.

![](../images/square_spiral.svg)
