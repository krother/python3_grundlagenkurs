
# Die Suche nach dem Drachenei

**🎯 Programmiere ein einfaches Textadventure.**

----

## Die Story

![](../images/drachenei.png)

Weit, weit, hinter unzugänglichen Landschaften verborgen, liegt ein geheimnisvolles Drachenei. Schaffst du es, das Drachenei zum Leben zu erwecken?

* das Drachenei liegt auf einer einsamen Lichtung
* um das Ei zu erwecken benötigst du einen Zauberspruch
* den Zauberspruch gibt es beim Magier
* der Magier lebt hinter dem Wald in einem Turm
* im Wald lebt ein Bär, der niemanden durchlässt
* der Bär mag Honig, den es beim Imker gibt

Wenn dir eine bessere Handlung einfällt, programmiere sie!

----

## Anforderungen

Schreibe ein Spiel, in dem du dich zwischen abgegrenzten Räumen hin- und herbewegen kannst.

* Die Spielwelt besteht aus mindestens vier 'Räumen'
* Zu jedem Raum wird eine Beschreibung ausgegeben.
* Du gibst über die Tastatur ein, in welchen Raum du gehen möchtest.
* Das Ziel ist es, den Ausgang zu finden.
* Wird der Ausgang erreicht, endet das Spiel mit einer Erfolgsmeldung.

Das Spiel ist vollständig textbasiert.

----

## Beispielausgabe

```text
Finde das Drachenei
===================

Du befindest Dich in Deiner Heimatstadt.
Ein kleine Handelsstadt am Rande der Wüste.

Wege führen zu: Wüste, Wald

Wohin möchtest Du gehen? Wüste


Du befindest Dich in der Wüste. Die Sonne brennt unbarmherzig.

Wege führen zu: Heimatstadt, Lichtung, Wald

Wohin möchtest Du gehen? Lichtung


Auf einer verborgenen Lichtung entdeckst Du das Drachenei.

Deine Suche war erfolgreich!
```

----

## Schritt für Schritt

### Schritt 1: Lege ein neues Projekt an

* Erstelle einen Ordner für das Projekt
* Erstelle eine Python-Datei `abenteuer.py`
* Öffne die Datei in einem Editor

----

### Schritt 2: Das Grundgerüst

Schreibe in das Programm eine Willkommensnachricht.
Hierfür eignet sich eine mehrzeilige Ausgabe:

```python
print("""
Finde das Drachenei
===================

Du begibst dich auf die Suche.
""")
```

Gib am Ende eine Erfolgsmeldung aus:

```python
print("""
Auf einer verborgenen Lichtung entdeckst Du das Drachenei.

Deine Suche war erfolgreich!
""")
```

Weiteren Code wirst Du später zwischen diesen beiden Anweisungen einsetzen.

**Führe das Programm aus und stelle sicher, dass es läuft.**

----

### Schritt 3: Die Hauptschleife

Das wichtigste Strukturelement bei den meisten Spielen ist die Hauptschleife.
In jedem Schleifendurchlauf kannst du einen Befehl eingeben.
Das Spiel soll enden, sobald der Zielort erreicht ist.

Es steht allerdings nicht im Voraus fest, wie viele Befehle lang das Spiel dauert.
Also ist die Anzahl Schleifendurchläufe unbekannt.
Für eine unbekannte Anzahl Wiederholungen eignet sich die `while`-Schleife.

Definiere zuerst eine Zustandsvariable, die den aktuellen Raum enthält.
In Python verwenden wir den Namen des Raumes direkt:

```python
raum = "Heimatstadt"
```

Sobald du den Raum *"Drachenei"* erreichtst, endet das Spiel.
Du kannst dies direkt in der `while`-Schleife umsetzen:

```python
while raum != "Lichtung":
    print(f"Du befindest dich in {raum}")
    raum = input("Wohin möchtest Du gehen? ")
```

Die `input()`-Anweisung ist ein Platzhalter, damit das Programm nicht in einer Endlosschleife hängen bleibt.

**Führe das Programm aus und stelle sicher, dass du das Spiel beenden kannst.**

----

### Schritt 4: Räume

Im Spiel gibt es noch keine Räume.
Du siehst also nicht, wo du dich befindest.

Gib stimmungsvolle Beschreibungstexte zu einigen Räumen aus.
Füge `if`-Anweisungen wie folgende zur Hauptschleife hinzu:

```python
if raum == "Heimatstadt":
    print("""
    Du befindest Dich in Deiner Heimatstadt.
    Ein kleine Handelsstadt am Rande der Wüste.
    """)
```

Diese `if`-Blöcke ersetzen die `print()`-Anweisung aus dem vorigen Schritt.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

----

### Schritt 5: Eine Datenstruktur

Jeden Raum mit `if` einzeln abzufragen, mag bei 4 Räumen ja noch angehen
Stelle dir vor, das Spiel hätte stattdessen 100 Räume.
Das Programm würde schnell unübersichtlich.

Eine bessere Alternative ist, die **Daten zu strukturieren**. Dazu verwenden wir ein **Dictionary**, das die Beschreibungen aller Räume enthält:

```python
beschreibungen = {
    "Heimatstadt": """Du befindest Dich in Deiner Heimatstadt...""",
    "Eiswüste": """...""",
}
```

Definiere dieses Dictionary am Anfang des Programms.
Nun kannst du alle `if`-Anweisungen durch einen einzigen Zugriff auf das Dictionary ersetzen.
Als Schlüssel dient die Variable `raum`.
Schreibe innerhalb der `while`-Schleife:

```python
print(beschreibungen[raum])
```

Und wirf die `if`-Anweisungen aus Schritt 4 weg.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

----

### Schritt 6: Plausibilitätskontrolle

Bisher prüft das Programm nicht, ob es einen Raum auch tatsächlich gibt.
Wenn Du also einen falschen Raum eingibst (oder Dich vertippst), bricht das Programm mit einer Fehlermeldung ab.
Führe eine Kontrolle der Eingabe durch, um das zu unterbinden.
Verwende folgenden Code, der die Eingabe mit den Schlüsseln des Beschreibungs-Dictionaries vergleicht:

```python
ziel = input("Wohin möchtest Du gehen? ")
if ziel in beschreibungen:
    raum = ziel
else:
    print("Stop! Dorthin führt kein Weg.")
```

Finde heraus, an welcher Stelle des Programms diese Zeile eingesetzt werden muss.

**Führe das Programm aus und stelle sicher, dass es funktioniert.**

----

### Schritt 7: Pfade

Im Moment kannst du dich von jedem Raum zu jedem anderen teleportieren.
Das ist etwas witzlos. Erstens nicht klar ist welche Räume es überhaupt gibt.
Zweitens kannst du *"Lichtung"* eingeben und beendest das Spiel sofort.

Etwas spannender wird es, wenn du bestimmte Räume miteinander verbindest.
Dazu brauchen wir eine zweite Datenstruktur, auch diesmal ein Dictionary.
Jeder Eintrag zeigt von einem Startraum zu einem oder mehreren Zielräumen:

```python
pfade = {
    "Heimatstadt": ["Wüste", "Wald"],
    "Wald": ["Heimatstadt", "Eiswüste"],
    ...
}
```

Damit ein Weg in beide Richtungen begehbar ist, benötigst du auch zwei Einträge.
Lässt du einen weg, kannst du auch *Einbahnstrassen* erstellen.

Die Pfade für den aktuellen Raum kannst du mit folgender Zeile anzeigen:

```python
print(pfade[raum])
```

oder etwas eleganter mit:

```python
print(", ".join(pfade[raum]))
```

Möchtest du auch die Plausibilitätskontrolle erweitern, so dass nur die aktuellen Pfade begehbar sind, benötigst du folgende Zeile:

```python
if ziel in pfade[raum]:
    ...
```

**Compiliere das Programm und stelle sicher, dass es läuft.**

----

### Schritt 8: Zustände

Ein spannedes Adventure sollte einige Puzzles enthalten.
Ein Puzzle könnte so aussehen:

```text
Wohin möchtest Du gehen? Wald

Im Wald ist ein Bär!!! Hier kannst Du nicht hin.

...

Wohin möchtest Du gehen? Imkerei

Beim Imker kaufst Du einen Topf Honig.

...

Wohin möchtest Du gehen? Wald

Du gibst dem Bären den Honig und er zieht zufrieden schleckend davon.
```

Wie kannst du ein Puzzle programmieren?

Erstens brauchst du eine **Zustandsvariable**, die du **vor der Hauptschleife** definierst, z.B.:

```python
honig = False
```

Zweitens musst du **in der Hauptschleife** abfragen, ob sich der Zustand ändert, z.B.:

```python
if raum == "Imkerei" and not honig:
    print("Beim Imker kaufst Du einen Topf Honig.")
    honig = True
```

Drittens musst du den Zustand **in der Hauptschleife** auswerten, um Aktionen zu ermöglichen oder zu blocken:

```python
if ziel == "Wald":
    if honig:
        print("Du gibst dem Bären den Honig und er zieht zufrieden schleckend davon.")
        honig = False  # kann nur 1x verwendet werden
    else:
        print("Im Wald ist ein Bär!!! Hier kannst Du nicht hin.")
        ziel = raum   # Spieler bleibt am gleichen Ort
```

----

### Schlussbemerkung

Alle diese Anweisungen in der richtigen Reihenfolge einzusetzen ist nicht ganz einfach.
Am besten probierst du das Programm nach jeder Änderung aus und schaust was passiert.

Bestimmt hast du noch viele Ideen, was in deinem Abenteuer passieren kann.
