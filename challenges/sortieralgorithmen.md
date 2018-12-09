
# Sortieralgorithmen

Sortieralgorithmen gehören zu den wichtigsten Algorithmen überhaupt. In dieser Übung kannst Du Dir ein Grundverständnis einiger Verfahren erarbeiten.

**Für diese Übung brauchst Du keine Computer**

## Material

* einen Stapel mit etwa 20 Spielkarten
* einen Ausdruck mit dem Pseudocode der 4 Algorithmen
* eine Stoppuhr
* einen Zettel, um die Zeit aufzuschreiben

(bei mehr Leuten benötigst Du eine Ausfertigung pro zwei Teilnehmer)

## Anweisungen

* lies Dir den Algorithmus genau durch
* mische den Kartenstapel
* starte die Stoppuhr
* führe einen der Algorithmen aus
* stoppe die Uhr, sobald alle Karten sortiert sind

### Selection Sort

1. Lege die Karten in einer Reihe vor Dir aus
2. Nimm die Karte mit der kleinsten Zahl und tue sie auf den Zielstapel
3. Wiederhole Schritt 2, bis alle Karten sortiert sind

### Insertion Sort

1. Nimm eine Karte vom Stapel und lege sie vor Dir aus
2. Liegen dort bereits Karten, füge die neue Karte an der richtigen Stelle ein
3. Wiederhole Schritte 1 und 2, bis alle Karten sortiert sind

### Bubblesort

1. Lege alle Karten in einer Reiche vor Dir aus
2. Gehe die Karten von links nach rechts durch
3. Wenn eine kleinere Karte rechts von einer größeren liegt, vertausche beide
4. Wiederhole Schritte 2 und 3, bis sich in einem Durchgang nichts ändert

### Mergesort

1. Teile den Kartenstapel in zwei gleich große Stapel
2. Sortiere jeden der Stapel nach dem Mergesort-Verfahren
3. Drehe beide Stapel um, so dass die jeweils kleinste Karte sichtbar ist
4. Lege die kleinere der beiden Karten auf den Zielstapel
5. Wiederhole Schritt 4, bis alle Karten sortiert sind


## Optionale Ziele

* wiederhole die Übung mit einem kleinen (10) und einem grossen Kartenstapel (20)
* implementiere einen der Algorithmen
* messe das Laufzeitverhalten mit `%timeit`
