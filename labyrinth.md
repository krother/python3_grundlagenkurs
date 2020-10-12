
# Flucht aus dem Labyrinth

**🎯 Schreibe ein einfaches Labyrinth-Spiel.**

![arcade](../images/labyrinth.png)

----

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Ein Spiel mit Grafik programmieren |
| 🔀 | Callback-Funktionen verwenden |
| ⚙ | Klassen definieren |
| ⚙ | Einen Konstruktor `__init__()` schreiben |
| 💡 | Die Bibliothek `arcade` verwenden |
| 🔧 | Programme über die Kommandozeile ausführen |

----

### Aufgabe 1: arcade

Die Python-Bibliothek [`arcade`](http://arcade.academy/) ist eine Bibliothek zum Programmieren von 2D-Spielen. Arcade kümmert sich um einen Großteil der Grafik und Steuerung, so dass Du Dich auf das Spiel konzentieren kannst.

Zunächst installiere die Bibliothek mit:

    :::bash
    pip install arcade

Auf manchen Systemen sind einige zusätzliche Schritte notwendig. Zur Sicherheit solltest Du das in der [Dokumentation zu `arcade`](http://arcade.academy/) überprüfen.

----

### Aufgabe 2: Ein Fenster erzeugen

Die Grundlage für Spiele ist die Klasse `arcade.Window`. Diese musst Du importieren:

    import arcade

und eine abgeleitete Klasse definieren. Gib der Klasse die Methode `__init__()` mit auf den Weg, in der Du Fenstergröße und -titel definierst:

    :::python3
    class Labyrinth(arcade.Window):

        def __init__(self):
            super().__init__(600, 600, "Labyrinth")

Nun kannst Du ein `Labyrinth`-Objekt erstellen und laufen lassen:

    :::python3
    laby = Labyrinth()
    arcade.run()

Beim Ausführen des Programms solltest Du ein schwarzes Fenster sehen, das bei Programmabbruch verschwindet. Bei einigen Entwicklungsumgebungen (darunter Anaconda Spyder) kann das Fenster im Hintergrund erscheinen. Suche es mit `Alt+Tab`.

----

### Aufgabe 3: Grafiken laden

Nun müssen wir Grafikelemente laden und anzeigen. Du findest einige in der Datei `tiles.png`:

![`arcade`](../images/tiles.png).

Lade einzelne Grafikelemente mit `arcade.load_texture()`. Als Parameter sind der Dateiname, die Position und Größe des Grafikelements nötig. Alle Elemente haben die Größe `32 x 32` Pixel:

    :::python3
    wand = load_texture("tiles.png", 0, 0, 32, 32)
    boden = load_texture("tiles.png", 0, 32, 32, 32)
    pac = load_texture("tiles.png", 0, 64, 32, 32)

Plaziere diese Befehle *vor* der Klassendefinition.

Wenn Du möchtest, kannst Du die Grafiken auch in einer intelligenteren Datenstruktur (z.B. einem Dictionary ablegen).

----

### Aufgabe 4: Grafiken anzeigen

Nun fügen wir der Klasse `Labyrinth` eine Methode `on_draw()` hinzu, die Grafik zeichnet. Diese wird von `arcade` automatisch in regelmäßigen Zeitabständen aufgerufen. Wir müssen nur noch angeben, welches Grafikelement wo auf dem Bildschirm erscheinen soll:

    :::python3
    def on_draw(self):
        arcade.start_render()
        pac.draw(300, 300, 32, 32)

Achte darauf, die Methode so einzurücken, dass sie sich *innerhalb* der Klasse befindet (auf gleicher Höhe mit `__init__()`). Die Funktion `start_render()` sorgt dafür, dass die Grafik nicht flimmert oder ruckelt.

Die Koordinaten werden von links nach rechts und von unten nach oben gezählt.

Wenn Du das Programm nun startest, solltest Du die Spielfigur auf dem Bildschirm sehen.

----

### Aufgabe 5: Die Spielfigur

Als nächstes wirst Du die Position der Spielfigur speichern und auf Tastendruck verändern.

Speichere zunächst die x/y-Position der Spielfigur als **Zustandsvariable** oder **Attribut** in der Klasse. Die Startposition läßt sich am Besten in der `__init__()`-Methode festlegen, da diese als Erstes aufgerufen wird:

    :::python3
    self.xpos = 300
    self.ypos = 300

Wir benötigen den Parameter `self`, um auf den Zustand der Klasse zuzugreifen. Andernfalls vergisst Python die Variable, sobald die Funktion beendet ist (man sagt auch, ihr *Gültigkeitsbereich (scope)* endet).

----

### Aufgabe 6: Den Punktefresser bewegen

Ändere die Methode `on_draw()` so, dass statt der voreingestellten `300` die Werte `self.xpos` und `self.ypos` verwendet werden.

----

### Aufgabe 7: Tastatursteuerung

Für die Tastaturabfrage benötigst Du die Pfeiltasten:

    :::python3
    from arcade.key import MOTION_UP, MOTION_DOWN, \
                           MOTION_LEFT, MOTION_RIGHT

Die Methode `on_key_press()` wird ebenfalls automatisch aufgerufen, wenn eine Taste gedrückt wird. Je nach Taste kannst Du die Position der Spielfigur verändern:

    :::python3
    def on_key_press(self, taste, mod):
        if taste == MOTION_RIGHT:
            self.xpos += 32

Nun sollte sich die Figur nach rechts bewegen!

Die anderen Bewegungsrichtungen bekommst Du selbst hin!

----

### Aufgabe 8: Das Programm verlassen

Importiere `ESCAPE` aus dem Modul `arcade.key`. Füge eine zusätzliche Bedingung dazu, die bei Drücken der Escape-Taste folgende Funktion aufruft:

    :::python3
    arcade.window_commands.close_window()

Damit sollte das Schließen des Fensters deutlich bequemer werden.

----

### Aufgabe 9: Das Spielfeld

Damit auf dem Bildschirm etwas mehr los ist, brauchen wir ein Spielfeld. Dieses soll aus Wänden und Boden bestehen.

Das Spielfeld lässt sich am Besten als String definieren. So lässt es sich leicht editieren. Ein `#` steht für eine Wand, ein `.` für Boden:

    :::python3
    LABYRINTH = """
    ##########
    #........#
    #.#.####.#
    #.#......#
    #.#....#.#
    #.#....#.#
    #......#.#
    #.####.#.#
    #........#
    ##########"""

Wandle das Spielfeld in eine Liste von Listen um. So kannst Du einfacher auf eine bestimmte Zeile und Spalte zugreifen:

    :::python3
    LEVEL = []
    for zeile in LABYRINTH.strip().split():
        LEVEL.append(list(zeile))

Füge diesen Code **vor** der Klassendefinition ein.

----

### Aufgabe 10: Das Spielfeld zeichnen

Um das Spielfeld zu zeichnen musst Du alle Kacheln aus `LEVEL` an der richtigen Stelle zeichnen. Schreibe dazu eine doppelte `for`-Schleife:

    :::python3
    for y, zeile in enumerate(LEVEL):
        for x, char in enumerate(zeile):
            if char == '#':
                wand.draw(x * 32, y * 32, 32, 32)

Setze diesen Code in die `on_draw()`-Methode ein.

Du solltest jetzt das Labyrinth angezeigt bekommen, wenn auch an der falschen Stelle.

----

### Aufgabe 11: Die Karte positionieren

Noch sind weder die Karte noch die  Spielfigur an der richtigen Stelle.

Zentriere das Spielfeld, indem Du zu den Koordinaten der Wände einen festen Betrag addierst:

    :::python3
    wand.draw(x * 32 + ____, y * 32 + ____, 32, 32)

Setze Zahlen ein, die aus Deiner Sicht gut aussehen.

----

### Aufgabe 12: Die Spielfigur positionieren

Für den letzten Schliff setze die Spielfigur auf die Gitterkoordinaten des Spielfeldes. Stelle dazu in `__init__()` die Position auf Gitterkoordinaten um:

    :::python3
    self.xpos = 5
    self.ypos = 5

Verwende zum Zeichnen der Spielfigur die gleiche Formel wie für das Spielfeld:

    :::python3
    pac.draw(self.xpos * 32 + ____, self.ypos * 32 + ____, 32, 32)

Achte darauf, beim Bewegen in `on_key_press()` die Koordinaten nicht mehr um `32`, sondern nur noch um `1` zu verändern:

    :::python3
    if taste == MOTION_RIGHT:
        self.xpos += 1

Dieser Trick macht es übrigens **viel** einfacher, Interaktionen mit der Umgebung zu programmieren.

----

## Fragen

### Wie kann ich prüfen, welches Grafikelement an der Position der Spielfigur liegt?

    :::python3
    LEVEL[self.ypos][self.xpos]

----

### Wie kann ich verhindern, dass die Spielfigur durch Wände läuft?

Prüfe in `on_key_press()` das jeweils nächste Feld, bevor Du `xpos` oder `ypos` veränderst. Beispielsweise bei einer Bewegung nach rechts:

    :::python3
   xneu = self.xpos + 1
   if LEVEL[self.ypos][xneu] != '#':
       self.xpos = xneu

Bei den anderen Richtungen ist der Code ähnlich.

----

### Wie kann ich etwas auf der Karte platzieren?

    :::python3
    LEVEL[self.ypos][self.xpos] = '#'

----

### Kann ich Text schreiben?

Ja. Schaue bitte in der Dokumentation von `arcade` nach wie es geht.

----

### Ich möchte einen Geist programmieren, der sich von selbst bewegt. Wie?

Wie bei der Spielfigur, kannst Du Koordinaten in `__init__()` definieren. Da die Bewegung aber auch erfolgen soll, wenn der Spieler grade nichts macht, verwende die Methode `update()`, die ebenfalls automatisch von `arcade` aufgerufen wird:

    :::python3
    def update(self, delta):
        # hier Geist bewegen
        ...

----

### Ich möchte Grafik mit vielen beweglichen Elementen programmieren. Wie?

Schaue Dir die Klassen `Sprite` und `SpriteList` an, mit denen sich viele bewegliche Elemente bequemer verwalten und sehr schnell zeichnen lassen.

----

## Links

* [Arcade Dokumentation](http://arcade.academy/)
* [OpenGameArt](https://opengameart.org/) – frei nutzbare Grafiken für eigene Spiele
