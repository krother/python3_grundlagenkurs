
# Animierter Scatterplot

In dieser Übung werden wir den Zusammenhang von Lebenserwartung und Fruchtbarkeit untersuchen.
Dazu werden wir die berühmte Animation von **Hans Rosling** nachstellen (siehe [https://www.youtube.com/watch?v=jbkSRLYSojo](https://www.youtube.com/watch?v=jbkSRLYSojo)).


### Schritt 1

Lade die Datei `gapminder_fertility.csv` in pandas.

```python
import pandas as pd

fert = pd.read_csv('gapminder_total_fertility.csv', index_col=0)
```

### Schritt 2

Verfahre genauso mit der Datei `gapminder_lifeexpectancy.xlsx`. Speichere es in einem `DataFrame` mit dem Namen `life`.

**Du benötigst dazu die Funktion `pd.read_excel`.**

Prüfe die Größe der beiden Tabellen mit:

```python
print(life.shape)
```

**Wenn sie nicht die gleiche Größe haben, ist das nicht schlimm.**

### Schritt 3

Betrachte die Spalten der beiden Tabellen:

```python
fert.columns
```

und

```python
life.columns
```

Die eine Tabelle hat Strings als Spalten, die andere Integer-Zahlen. Um die Tabellen sinnvoll zusammenführen zu können, sollten beide das gleiche Format haben. Dazu erzeugen wir uns eine Liste mit den Jahrgängen als Integers.

```python
ncol = [int(x) for x in fert.columns]
```

und setzen diese Liste als neue Spaltennamen ein:

```python
fert.set_axis(axis=1, labels=ncol, inplace=True)
```

Prüfe mit `fert.columns`, ob die Umwandlung erfolgreich war.

## Langes und breites Tabellenformat

![](../images/long_vs_wide.png)

### Schritt 3

Um schönere Spaltennamen zu erhalten, kannst Du Dir einen **hierarchischen Index** basteln. Dazu wandeln wir beide Tabellen in ein *langes Tabellenformat* um:

```python
sfert = fert.stack()
slife = life.stack()
```

Die beiden Variablen `sfert` und `slife` sind nun vom Type `pd.Series`. Mehrere Series lassen sich über ein Dictionary in ein `pd.DataFrame` umwandeln:

```python
d = {'fertility': sfert, 'lifeexp': slife}
df2 = pd.DataFrame(data=d)
```

Diese riesige Tabelle lässt sich leichter in ein beliebiges Format bringen, wenn wir zunächst alle Indizes (Zeilen und Spalten) als Zeilenindizes aufstapeln:

```python
df3 = df2.stack()
```

Zum Schluß können wir aus der *langen* wieder eine *breite* Tabelle machen. Dazu erzeugen wir aus der ersten und dritten Ebene des Index (den Ländernamen und den Eigenschaften) neue Spalten:

    :::python3
   df4 = df3.unstack((0,2))

Die Null steht für das jeweils erste Element des Index, mit 1 würden die Jahreszahlen in die Spalten rutschen.

Nun sollte `df4` eine Tabelle sein, in der links die Jahreszahlen stehen und oben die Lebenserwartung und Fruchtbarkeit für alle Länder.

### Schritt 4

Nun kannst Du gezielt Spalten auswählen und plotten:

```python
import pylab as plt
df4[['Germany', 'France', 'Sweden']].plot()
```

### Schritt 5

Um ein Streudiagramm zu erzeugen, ziehen wir die zu plottenden Spalten aus `df3`:

```python
df5 = df3.unstack(2)
df5.plot.scatter('fertility', 'lifeexp', s=0.1)
```

### Schritt 6

Wir können durch die Operationen `stack` und `unstack` auch einen Jahrgang auswählen. So wird die Graphik etwas übersichtlicher:

```python
df6 = df3.unstack(1)  # Jahre als Spalten
df6 = df6[1950]       # nur ein Jahrgang
df6 = df6.unstack(1)  # Eigenschaften als Spalten
df6.plot.scatter('fertility', 'lifeexp', s=0.1)
```

### Schritt 7

Das Ganze bietet noch etwas Raum für Verschönerungen. Beispielsweise kannst Du jedem Land eine andere Farbe geben:

```python
cmap = plt.get_cmap('tab20').colors
df6.plot.scatter('fertility', 'lifeexp', s=0.1, c=cmap)
```

Oder Dir eine Funktion schreiben, die einzelnen Ländern bestimmte Farben zuweist:

```python
def farben_ermitteln(laendernamen):
    farben = []
    for land in laendernamen:
        ...
    return farben

farben = farben_ermitteln(df6.index)
```

### Schritt 8

Für die Größen der Punkte kannst Du die Spalte mit der Bevölkerung verwenden. Verändere die Anweisungen, so dass Du eine sinnvolle Größe für die Punkte erhälst:

```python
groessen = df6['population']
df6.plot.scatter('fertility', 'lifeexp', s=groessen)

```

## Animierter Scatterplot

Abschließend erstellen wir eine Serie von Bildern, die wir zu einem animierten GIF verbinden.

### Schritt 9

Erstelle einen Scatterplot für die Korrelation zwischen Lebenserwartung und Fruchtbarkeit für *jedes* Jahr zwischen 1960 und 2015 (davor sind die Daten sehr lückenhaft).

### Schritt 10

Lege mit `plt.axis()` die Achsenbegrenzungen in x- und y-Richtung fest, damit die Animation nicht herumwackelt.

### Schritt 11

Bringe die Jahreszahl mit `plt.title()` oder `plt.text()` im Diagramm unter.

### Schritt 12

Speichere jeden Scatterplot als eigene Datei mit der Jahreszahl im Dateinamen ab, z.B. `lifeexp_..` .


### Schritt 13

Installiere das Python-Modul `imageio`, indem Du auf der Kommandozeile eingibst:

```python
pip install imageio
```

### Schritt 14

Passe das folgende Skript an und führe es aus:

```python
import imageio

images = []

for i in range(0, 100):
    filename = 'lifeexp_{}.png'.format(i)
    images.append(imageio.imread(filename))

imageio.mimsave('output.gif', images, fps=20)
```

