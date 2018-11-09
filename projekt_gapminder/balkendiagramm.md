
# Balkendiagramme plotten

### Schritt 1

Lade die Datei `gapminder_total_fertility.csv` in pandas.

    import pandas as pd

    df = pd.read_csv('gapminder_total_fertility.csv', index_col=0)

### Schritt 2

Wähle 3 Jahrgänge aus den Spalten des `DataFrame` aus, z.B.:

    df = df[['1950', '1955', '2000']]

### Schritt 3

Wähle 4 Länder aus dem Index des `DataFrame`aus, z.B.:

    df = df.loc[['Germany', 'India', 'Bulgaria', 'Kenya']]

### Schritt 4

Zeichne ein Balkendiagramm mit den Jahren als Balkengruppen:

    from matplotlib import pyplot as plt

    df.plot.bar()
    plt.savefig('balken.png')

### Schritt 5

Ändere die Größe des Diagramms, indem Du zum Aufruf von `plot.bar` den Parameter `figsize=(5,7)` hinzufügst.
