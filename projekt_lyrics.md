

# Songtexte

![Eminem](../images/eminem_word_cloud.jpg)

*häufige Wörter in Songtexten von Eminem*

## Ziel

In diesem Kapitel werden wir **aus Songtexten die Interpreten vorhersagen**.

Unser Programm soll lernen, aus Sätzen wie

* *"we will dance and have a good time"*
* *"I want you to know, yeah, that I still love you so"*
* *"the little bags of dope, there was a pile of coke"*

einen möglichen Interpreten zu nennen.

Das Projekt besteht aus drei Teilen:

| Teil | Aufgabe      | Technologien |
|------|--------------|--------------|
|  1.  | Songs aus dem Internet herunterladen | web scraping, requests |
|  2.  | Texte aus HTML-Code extrahieren | Reguläre Ausdrücke |
|  3.  | Klassifikation von Texten | maschinelles Lernen, Naive Bayes |

## Links

[Are Pop Lyrics getting more repetitive?](https://pudding.cool/2017/05/song-repetition/index.html)

----

# Teil 1: Songliste herunterladen

## Aufgabe 1.1

Besuche im Browser die Seite [azlyrics.com](http://www.azlyrics.com). Suche Dir einen beliebigen Interpreten aus (außer **Madonna**, **Eminem** und **Beatles**, die habe ich schon).

Notiere Dir die URL.

## Aufgabe 1.2

Erstelle eine Python-Datei `download.py`.

## Aufgabe 1.3

Verwende das Modul `requests`, um die Seite mit der Songliste des gewählten Interpreten herunterzuladen.

Damit das funktioniert, müssen wir so tun als wäre Python ein Browser. Das geht mit:

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    seite = requests.get(url, headers=headers)

## Aufgabe 1.4

Speichere die heruntergeladene Seite in einer HTML-Datei.

#### Hinweis:

Wenn in der Seite bestimmte Sonderzeichen vorkommen, mußt Du die Datei zum Schreiben öffnen mit:

    f = open(dateiname, 'w', encoding='utf-8')

# Teil 2: Songs auslesen

## Aufgabe 2.1

Erstelle eine neue Python-Datei `songs_auslesen.py`.

## Aufgabe 2.2

Lies die in Aufgabe 1.4 gespeicherte HTML-Datei ein.

## Aufgabe 2.3

Betrachte die HTML-Datei in einem Texteditor. Finde heraus, wo in der Datei die Songtitel und Links in der Seite sind und woran das Programm diese Stellen erkennen kann.

## Aufgabe 2.4

Schreibe ein Programm, das alle Links zu songs aus der Seite ausliest und in einer Liste sammelt, z.B.:

    [
     'madonna/frozen.html',
     'madonna/burningup.html',
     ..
    ]

Mögliche Ansätze:

* `string.find`
* `string.split`
* Position im String (falls sie immer die gleiche ist)
* Reguläre Ausdrücke

#### Hinweis:

Wenn in der Seite bestimmte Sonderzeichen vorkommen, mußt Du die Datei öffnen mit:

    f = open(dateiname, 'r', encoding='utf-8')

## Aufgabe 2.5

Gib alle Links auf dem Bildschirm aus und prüfe nach, ob das Programm korrekt arbeitet.

## Aufgabe 2.6

Verpacke den bisher geschriebenen Code in eine Funktion:

    def titel_auslesen(dateiname):
        # Dein Code kommt hierhin
        return songtitel

Rufe die Funktion im Programm aus und stelle sicher, daß es immer noch funktioniert.


# Teil 3: Songtexte herunterladen

## Aufgabe 3.1

Erstelle Dir ein Verzeichnis, in dem Du die Songtexte speichern möchtest.

## Aufgabe 3.2

Lösche sämtliche Leer- und Sonderzeichen aus dem Songtitel, um einen Dateinamen zu erhalten.

Füge dem Dateinamen als Endung `.html` hinzu.

## Aufgabe 3.3

Nimm **nur den ersten Song der Liste**. Erstelle aus dem Link zu diesem Song eine vollständige URL.


## Aufgabe 3.4

Lade einen *einzelnen* Song herunter und speichere diesen in einer Textdatei.

## Aufgabe 3.5

Verpacke das Herunterladen eines Songs in einer Funktion:

    def song_herunterladen(titel, link):
        # Dein Code hierhin

Verwende wie in Aufgabe 1 die `headers`, um einen Browser zu simulieren.

## Aufgabe 3.6

Verwende das Modul `time`, um nach dem Herunterladen und Speichern eines Songs 120 Sekunden zu warten:

    import time
    time.sleep(120)

**DIES IST DER WICHTIGSTE SCHRITT IN DER HEUTIGEN AUFGABE. WENN EINER VON UNS DIESEN VERGISST, KANN ES GANZ LEICHT PASSIEREN, DASS DER SERVER DIE GANZE KLASSE AUSSPERRT.**

## Aufgabe 3.7

Verwende die Funktion `song_herunterladen`, um **die ersten 20 Songs** herunterzuladen.

## Aufgabe 3.8

Prüfe vor dem Herunterladen, ob eine Datei schon existiert:

    import os
    if os.path.exists()

Lade nur Dateien herunter, die es noch nicht gibt.

# Teil 4: Songs einlesen

*Diesen Teil kannst Du bequem bearbeiten, wenn das andere Proramm noch im Hintergrund mit Herunterladen beschäftigt ist.*

## Aufgabe 4.1

Erstelle ein neues Programm `songs_einlesen.py`

## Aufgabe 4.2

Gib die Namen aller Songdateien aus. Verwende das Modul `os`:

    import os
    for dateiname in os.listdir(PFAD):
        print(dateiname)

## Aufgabe 4.3

Betrachte eine Songdatei im Texteditor. Finde heraus, wo der eigentliche Text beginnt und endet.

## Aufgabe 4.4

Lies eine Songdatei als einzelnen String ein. Verwende dazu `read()`:

    text = open(dateiname).read()



# Reguläre Ausdrücke

### Aufgabe 1

Finde Wörter mit `F` im Text. Führe dazu folgendes Beispiel aus:

    import re

    text = "Es war einmal ein Ferkel, das hatte eine Flöte"
    found = re.findall('(F\w+)[^\w]', text, re.IGNORECASE)
    print(found)


### Aufgabe 2

Was haben diese vier Bilder gemeinsam?

![King Kong Flip Flop Hip Hop Ping Pong](../images/regex.jpg)


Führe folgendes Codebeispiel aus:

    import re
    text = input("Was ist auf einem der Bilder zu sehen? ")
    if re.search(r"^(\w+)i(\w+)[- ]\1o\2", text):
        print("stimmt!")

### Aufgabe 3

Besuche die Seite [www.regexone.com](http://www.regexone.com) und führe einige der Übungen aus.

### Aufgabe 4

Schreibe ein Programm, das E-Mail-Adressen in Text erkennt.

Verwende die Funktion `re.findall` und erstelle ein entsprechendes Suchmuster.

Auf [Regex101](https://regex101.com/) kannst Du den regulären Ausdruck testen.

Schneide den Songtext aus. Dies geht recht gut mit Hilfe von `text.find()`.

## Aufgabe 4.5

Verpacke das Einlesen eines Songs in eine Funktion, die den Text als String zurückgibt.

## Aufgabe 4.6

Lies alle Songs in eine Liste von Strings ein. Verpacke auch diesen Code in eine Funktion:

    def songtexte_auslesen(verzeichnis):
        # Dein Code
        return textliste


### Bildquellen (links oben nach rechts unten):

* *[By Source (WP:NFCC#4), Fair use](https://en.wikipedia.org/w/index.php?curid=48711736)*
* *[Die Autorenschaft wurde nicht in einer maschinell lesbaren Form angegeben. Es wird Swarve~commonswiki als Autor angenommen, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=336076)*
* *[Gaël Marziou from Grenoble, France - IMG_6266_DXO, CC BY 2.0](https://commons.wikimedia.org/w/index.php?curid=47416377)*
* *Derfu, CC BY-SA 3.0*

# Teil 5: Vorhersage

Hier werden wir ein Standard-Kochrezept nachbauen (siehe [http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)).

## Aufgabe 5.1

Erstelle ein neues Modul `vorhersage.py`.

Importiere die Funktion zum Einlesen aus dem Modul `songs_einlesen.py` ein:

    from songs_einlesen import songtexte_auslesen

## Aufgabe 5.2

Bereite die Daten zur Vorhersage vor, indem Du in `X` die Liste mit Songtexten sammelst, in `y` die Namen der Interpreten. Zum Beispiel:

    X = madonna + eminem
    y = ['madonna'] * len(madonna) + ['eminem'] * len(eminem)

Stelle sicher, daß X und y gleich lang sind.

## Aufgabe 5.3

Importiere ein paar Sachen aus `scikit-learn`:

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import Pipeline
    from sklearn import model_selection

## Aufgabe 5.4

Zerlege den Datensatz in Trainings- und Testdaten. Setze für `ANTEIL_TESTDATEN` eine Zahl zwischen 0 und 1 ein:

Xtrain, Xtest, ytrain, ytest = \
    model_selection.train_test_split(X, y, test_size=ANTEIL_TESTDATEN)

## Aufgabe 5.5

Baue das Modell:

    model = Pipeline([
        ('vectorizer', CountVectorizer(min_df=3, ngram_range=(1, 1))),
        ('tfidf_transformer', TfidfTransformer()),
        ('bayes_model', MultinomialNB(alpha=1.0)),
    ])
    model.fit(Xtrain, ytrain)

## Aufgabe 5.6

Gib die Anzahl vektorisierter Wörter aus:

    vect = model.named_steps['vectorizer']
    print(len(vect.vocabulary_))

## Aufgabe 5.7

Werte das Modell aus:

    print("Genauigkeit: ", model.score(Xtest, ytest))

Werte das Modell auch für den Testdatensatz aus. Wie bewertest Du das Ergebnis?

## Aufgabe 5.8

Verändere den Parameter `alpha`. Wie verändert sich die Vorhersage?

## Aufgabe 5.9

Führe eine 10-fache Kreuzvalidierung durch:

    print(model_selection.cross_val_score(model, X, y, 
    cv=10, scoring='accuracy'))


## Aufgabe 5.10

Führe eine Vorhersage durch:

    model.predict(["take the 8mile road in detroit"])

## Aufgabe 5.11

Gib typische Wörter für die verglichenen Künstler aus:

    import numpy as np
    names = np.array(model.named_steps['vectorizer'].get_feature_names())

    coef = model.named_steps['bayes_model'].coef_
    coef = coef.reshape((len(names),))

    # Top-Wörter für 1. Interpreten
    indices = (-coef).argsort()[:20].tolist()
    print(names[indices])

    # Top-Wörter für 2. Interpreten
    indices = (coef).argsort()[:20].tolist()
    print(names[indices])

## Aufgabe 5.11

Probiere unterschiedliche Optionen aus:

* variiere den Anteil der Testdaten
* variiere `min_df` beim `CountVectorizer`
* gib beim `CountVectorizer` die Option `stop_words='english'`
* variiere `ngram_range` beim `CountVectorizer`
