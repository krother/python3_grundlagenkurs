
# Dekoratoren als Funktionen verwenden

**Dies ist eine aufgabe für fortgeschrittene Python-Nutzer.**

## Aufgabe

Gegeben ist folgender Code:

    @add_two
    def double(a):
        return a * 2

    print(double(20))
    print(add_two(40))

Implementiere den Dekorator `add_two`, so dass die Ausgabe ist:

    42
    42

Verändere den obigen Code nicht!

## Beschreibung

In dieser Aufgabe kannst Du folgende Konzepte üben:

* Dekorator-Funktionen
* Dekorator-Klassen
* Metaklassen

Eine **Dekorator-Klasse** und eine **Funktion** sind unterschiedliche Dinge, oder?
In Python ist dies nicht unbedingt der Fall! An sich kann jedes Python-Objekt sich wie jedes andere verhalten.

Fans stark typisierter Sprachen werden sich bei dieser Übung vor Schmerzen winden. Allerdings das Implementieren eines Dekorators, der sich wie eine Funktion verhält, eine gute Möglichkeit, die tiefer liegende Maschinerie der Namensräume und der dynamischen Typen in Python genauer zu verstehen.

## Optionales Ziel 1

Wenn die Übung für Dich zu leicht war, implementiere den Dekorator als Klasse. Dazu mußt Du Dich mit dem Begriff `metaclass` auseinandersetzen.

## Optionales Ziel 2

Der Dekorator soll immer noch funktionieren, wenn er mehrmals aufeinander gestapelt wird:

    @add_two
    @add_two
    def double(a):
        return a * 2

    double(19)

ergibt `42`.
