
# Postkarte

**🎯 Schreibe ein Programm, das eine Postkarte aus Deiner Lieblingsstadt zusammensetzt.**

![Willkommen in Poznan](images/poznan.png)

## Schritt 1: Bildmaterial

Beschaffe 2-4 Bilder, die Du zu einer Postkarte zusammensetzen möchtest.

----

## Schritt 2: Installiere Pillow

    :::bash
    pip install pillow

(mit Anaconda ist Pillow bereits installiert)

----

## Schritt 3: Lerne Pillow kennen

Führe folgendes Programm aus:

    :::python3
    from PIL import Image

    im = Image.open('bild1.png')
    small = im.resize((320, 240))
    result = small.rotate(180)
    result.save('bild2.png')

Ändere die Zahlen so, dass Du ein quadratisches Bild erzeugst.

----

## Schritt 4: Formen zeichnen

Was tut folgender Code?

    :::python3
    from PIL import Image, ImageDraw

    white = Image.new('RGB', (320, 240), 'white')

    d = ImageDraw.Draw(white)
    d.rectangle((10, 10, 80, 40), 'orange')
    d.ellipse((100,100,180,140), 'red')
    d.polygon((50,200, 90, 200, 70, 170), 'yellow')

    white.save('shapes.png')

----

## Schritt 5: Text zeichnen

Füge etwas Text hinzu:

    :::python3
    from PIL import ImageFont

    font =  ImageFont.load_default()
    d.text((150, 150), 'Poznan', fill=('purple'), font=arial)

Wenn Du TTF-Schriftarten auf Deinem System findest, wird es wesentlich hübscher.

    :::python3
    font = ImageFont.truetype('arial.ttf', 40)

----

## Schritt 6: Das Bild zusammenfügen

Du kannst Bilder mit Pillow einfügen:

    :::python3
    bild1.paste(bild2, (0, 0))
    bild1.save('postkarte.png')

* Setze die kleineren Bilder zu einem großen zusammen.
* Füge einen breiten Streifen als Texthintergrund hinzu.
* Schreibe Text auf den Streifen.
