
# Diashow

**🎯 Programmiere eine kleine Diashow.**

![Beispielausgabe](../images/diashow.png)

*Beispielausgabe des fertigen Programms*

----

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Bilder anzeigen |
| 💡 | Die Bibliothek Pillow verwenden |
| 💡 | Bilder mit Pillow verändern |
| ⚙ | Module importieren |
| ⚙ | Dateinamen und -pfade schreiben |
| ⚙ | Über Listen iterieren |
| ⚙ | Listen indizieren |
| 🔀 | Zählvariablen verwenden |

----

### Aufgabe 1: Ein Bild anzeigen

Verwende die Bibliothek **Pillow**, um Bilder in Spyder anzuzeigen.

* Lade zuerst diese [10 Bilder als Zip-Datei](/static/content/python_basics_DE/10bilder.zip) herunter.
* Entpacke die Zip-Datei
* Kopiere das Bild `"rainbow.jpg"` in Deinen Ordner für Python-Programme.

Erstelle eine neue Programmdatei mit folgenden Anweisungen:

```python
from PIL import Image
from IPython.display import display

bild = Image.open('rainbow.jpg')
display(bild)
```

Speichere das Programm und führe es dann aus.
Du solltest das Bild rechts unten in der **Ausgabekonsole** sehen.

Falls Du eine Fehlermeldung siehst, liegt das Bild wahrscheinlich woanders (es muss dort liegen, wo Du das Programm gerade gespeichert hast).

Falls Du überhaupt nichts siehst (z.B. weil Du einen anderen Editor verwendest), kannst Du statt `display()` auch diesen Befehl ausprobieren:

```python
bild.show()
```

----

### Aufgabe 2: Pfade

Jetzt werden wir ein Bild aus einem anderen Ordner einlesen.

Verschiebe den ganzen Ordner `bilder` dorthin, wo Du Deine Python-Programme speicherst.

Definiere eine Variable mit dem Namen des Ordners (im Fachjargon *"Pfad"*):

```python
from PIL import Image
from IPython.display import display

pfad = 'bilder/'
bild = Image.open(pfad + 'flower.jpg')
display(bild)
```

Der Schrägstrich (*forward slash*) ist sehr wichtig, um Namen von Verzeichnissen und Dateien zu trennen. Python ist sehr pingelig beim Unterscheiden von Schrägstrichen (`/`) und Backslashes (`\`).

Falls Du eine Fehlermeldung siehst, liegen die Bilder wahrscheinlich woanders (der Ordner `bilder` und dein Programm liegen in unterschiedlichen Ordnern).

----

### Aufgabe 3: Mehrere Bilder

Erstelle eine Liste mit Namen von Bildern:

```python
bilder = ['rainbow.jpg', 'flower.jpg', 'pebbles.jpg']
for dateiname in bilder:
    bild = Image.open(pfad + dateiname)
    display(bild)
```

Füge dem Programm folgende Anweisung hinzu:

```python
input('drücke <Enter> für das nächste Bild')
```

Wo musst Du den Befehl einfügen, damit Du jedes Mal drücken musst, um das nächste Bild zu sehen?

----

### Aufgabe 4: Bilder nummerieren

Jedes Bild soll eine Nummer bekommen.
Dazu verwenden wir eine **Zählvariable**.
Die Zählvariable soll sich bei jedem Schleifendurchlauf um 1 erhöhen, so dass sie stets die Nummer des aktuellen Bildes enthält.

Sortiere die folgenden Befehle in das Programm aus dem letzten Schritt ein:

```python
print(titel)
i = i + 1
i = 0
titel = f"Bild Nr. {i}"
```

Wenn alles funktioniert, solltest Du unter jedem Bild eine Unterschrift mit der richtigen Nummer sehen, z.B.:

```text
Bild Nr. 1
```

----

### Aufgabe 5: Bildunterschriften

Bereite eine Liste mit Bildunterschriften vor, z.B.:

beschriftung =  [
        'bunte Ölschlieren von Daniel Olah',
        'weiße Blume von Annie Spratt',
        'Kieselsteine von John Salzarulo'
        ]

Wir möchten immer eine Bildunterschrift auf einmal ausgeben.
Dazu verwenden wir **Indizierung**.
Probiere aus, was Du mit folgenden Befehlen erhälst:

    print(beschriftung[0])

    print(beschriftung[2])

Setze die Variable `i` aus der vorigen Aufgabe in die eckige Klammer ein, um zu jedem Bild den passenden Text auszugeben, z.B.:

```text
Bild Nr. 1
bunte Ölschlieren von Daniel Olah
```

----

### Aufgabe 6: Bildmanipulation

Die Bibliothek **Pillow** kann noch viel mehr.
Probiere nacheinander die folgenden Anweisungen aus. Finde heraus was sie tun:

```python
x, y = bild.size
print(x, y)

b = bild.resize((500, 500))
display(b)

b = bild.rotate(45)
display(b)

b = bild.crop((100, 100, 300, 300))
display(b)

bild.save('neues_bild.png')
```

Du findest eine sehr, sehr ausführliche Dokumentation von Pillow auf [pillow.readthedocs.io ](https://pillow.readthedocs.io).

----

### Aufgabe 7: Eigene Bilder

Verwende Deine eigenen Bilder und beschrifte sie.

Um die letze Eingabe zu unterdrücken, kannst Du den `input()`-Befehl abwandeln:

```python
if i < len(bilder):
    input('nächstes Bild')
```

Führe die fertige Diashow vor.

**Tip:** *Wenn Du größere Bilder zeigen möchtest, kannst Du den Ausgabebereich in Spyder vergrößern, indem Du mit dem  Mauspfeil den Rand nach links ziehst.*

----

## Bildquellen

Folgende Bilder von [unsplash.com](https://unsplash.com) wurden verwendet:

* Bubbles by Marko Blažević on Unsplash
* Coffee by Nathan Dumlao on Unsplash
* Ivy by asoggetti on Unsplash
* Orange by Vino Li on Unsplash
* Rainbow paint by Daniel Olah on Unsplash
* Pebbles by John Salzarulo on Unsplash
* Waterfall by Ben Guerin on Unsplash
* Clouds by Zbynek Burival on Unsplash
* White flower by Annie Spratt on Unsplash
* Puddle by Erik Mclean on Unsplash
