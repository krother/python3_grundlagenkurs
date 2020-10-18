
# Wer überlebt auf der Titanic?

**🎯 Sage anhand der Angaben über einen Passagier auf der Titanic vorher, ob dieser das Unglück überlebt.**

![](../images/titanic.png)

----

### Aufgabe 1: Hypothesen

Sammle Ideen, was für *Merkmale von Passagieren* die Überlebenschancen auf der Titanic steigern und welche nicht, bevor du das Modell baust.

----

### Aufgabe 2: Vorbereitung

Importiere einige Bibliotheken:

    :::python3
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

----

###  Aufgabe 3: Daten laden

Verwende `pandas`, um die Datei [`train.csv`](/static/content/python_basics_DE/titanic/train.csv) zu laden.

Du findest eine Dokumentation der Daten auf [www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic).

----

### Aufgabe 4: Histogramm

Erstelle ein Histogramm nach dem Alter und nach Überleben gruppiert:

    :::python3
    df.groupby('Survived')['Age'].hist(alpha=0.5)

----

### Aufgabe 5: Balkendiagramm

Erstelle ein Balkendiagramm mit den Häufigkeiten gruppiert nach Passagierklasse nach Überleben:

    :::python3
    g = df.groupby(['Survived', 'Pclass'])
    g = g['Name'].count()
    g = g.unstack()
    g.plot().bar()

**Wozu dient der Befehl `unstack`?**

----

### Aufgabe 6: Noch ein Balkendiagramm

Gruppiere als drittes Kriterium zusätzlich nach Geschlecht.

----

### Aufgabe 7: Paarplot

Jetzt plotten wir alles gegen alles!

    :::python3
    pd.scatter_matrix(df, figsize=(15,15))

**Anmerkung:** Da die meisten der Daten *kategorisch* sind, kann man im Diagramm nicht so viel sehen. Die Darstellung ist aber oft so praktisch, daß ich sie hier nicht vorenthalten wollte.

----

### Aufgabe 8: Einfärben

Färbe die Überlebenden blau ein und die Ertrunkenen rot. Schreibe dazu eine Funktion `make_col(x)`, die je nach x einen anderen Farbcode `(R, G, B)` zurück liefert.

Damit können wir eine Spalte mit Farbangaben erstellen:

    :::python3
    col = df['Survived'].apply(make_color)

Und diese als zusätzlichen Parameter `c=col` in der Funktion `scatter_matrix` angeben.

----

### Aufgabe 9: Auswählen von Spalten

Wähle alle Spalten außer `"Survived"` für den Paarplot aus.

----

### Aufgabe 10: Datenaufbereitung

Lösche die Spalten `"Name"` und `"Cabin"` aus dem Datensatz.

    :::python3
    del df['Name']
    ...

Fülle die fehlenden Werte in der Spalte `"Age"` mit

    :::python3
    df.fillna(df['Age'].median(), inplace=True)

----

### Aufgabe 11: Unabhängige und abhängige Variablen

* Speichere die *unabhängigen Variablen*, die Spalten `"Pclass"` und `"Age"`, in einem DataFrame `X`.
* Speichere die *abhängige Variable*, die Spalte `"Survived"`, in einer Variable `y`.

----

### Aufgabe 12: Trainings- und Testdaten

Teile den Datensatz in Trainings- und Testdaten auf:

    :::python3
    from sklearn.model_selection import train_test_split

    Xtrain, ytrain, Xtest, ytest = train_test_split(X, y, random_state=0)

**Überlege, warum diese Aufteilung wichtig ist.**

----

### Aufgabe 13: Ein Modell trainieren

Nun erstelle eines der einfachsten möglichen maschinellen Lernmodelle nach dem k-nächste-Nachbarn-Verfahren:

    :::python3
    from sklearn.neighbors import KNeighborsClassifier

    m = KNeighborsClassifier(n_neighbors=1)

und trainiere das Modell mit den Trainingsdaten:

    :::python3
    m.fit(Xtrain, ytrain)

----

### Aufgabe 14: Das Modell auswerten

Berechne die Genauigkeit des Modells für die Trainingsdaten:

    :::python3
    print(m.score(Xtrain, ytrain))

Berechne die Genauigkeit auch für die Testdaten. Vergleiche die Zahlen und erkläre die Unterschiede.

**Ist dies ein gutes Modell?**

----

### Aufgabe 15: Vorhersage

Erstelle Datensätze für weitere Passagiere:

    :::python3
    import numpy as np

    leo = np.array([[22, 3]])
    kate = np.array([[25, 1]])

und erstelle eine Vorhersage für diese:

    :::python3
    print(m.predict(leo))
    print(m.predict(kate))

----

### Aufgabe 16: Mehr Daten

Wiederhole den Modellbau, indem Du mehr Daten berücksichtigst. Nimm 2-3 zusätzliche Spalten auf. Verbessert sich an der Qualität der Vorhersage etwas?

----

### Aufgabe 17: Dummy-Variablen

Um die *kategorischen* Merkmale `"Sex"` oder `"Embarked"` mit aufzunehmen, benötigst Du folgende Funktion:

    :::python3
    dummies = pd.get_dummies(df['Sex'])

baue eine der Dummy-Variablen in Deinen Datensatz ein, bevor Du ihn in Trainings- und Testdaten aufteilst:

    df['female'] = dummies['female']

Wie verändert sich die Genauigkeit des Modells?

----

### Aufgabe 18: Weitere Modelle

Verschaffe Dir einen Überblick über die Funktionsweise eines der folgenden Modelle zur Klassifikation:

| Modell | Klasse in scikit-learn |
|--------|------------------------|
| logistische Regression | sklearn.linear_model.LogisticRegression |
| Random Forest | sklearn.ensemble.RandomForestClassifier |
| Support Vector Machine | sklearn.svm.SVC |

Als Quelle dienen Wikipedia und [scikit-learn.org](http://scikit-learn.org)

Wende eines dieser Modelle auf den Datensatz an, indem Du die Klasse
`KNeighborsClassifier` durch die aus der Tabelle ersetzt. Gib keine Parameter an, sondern verwende die Standardeinstellungen.

Welche Genauigkeit erreichst du?

----

### Aufgabee 19: Koeffizienten bei der logistischen Regression

Schaue Dir die berechneten Koeffizienten von `LogisticRegression` an:

    :::python3
    for label, coef in zip(X.columns, m.coef_):
        print("{:10s}\t{:8.3f}".format(lab, coef))

----

### Aufgabe 20: Skaliere

Skaliere die Eingabedaten der logistischen Regression:

    :::python3
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaler.fit(Xtrain)
    Xtrain = scaler.transform(Xtrain)
    Xtest = scaler.transform(Xtest)

Trainiere das Modell mit dem skalierten `Xtrain`.

----

### Aufgabe 21: Maximale Tiefe beim Random Forest

Vergleiche die Parameter `max_depth=2`, `max_depth=3` und `max_depth=10` beim Random-Forest-Modell. Wie wirken sich die Einstellungen auf die Vorhersagequalität aus?


----

### Aufgabe 22: Die Vorhersage einschicken

Sende eine Vorhersage auf [kaggle.com](http://www.kaggle.com) ein und schaue wie erfolgreich Dein Modell ist.
