
# Machine Learning mit Python

*Data Science has been called "The sexiest job of the 21st century" - probably by someone who has never visited a fire station.* (**Joel Grus**)

## Was ist Machine Learning?

**Beim Machine Learning werden mathematische und statistische Modelle computergestützt entwickelt.** Dies ist eine sehr breite Definition. Da ich nicht vorhabe, das Thema hier erschöpfend zu behandeln, reichen hier einige Anwendungsbeispiele:

* Spamfilter
* Erkennung von Postleitzahlen auf Briefen
* Empfehlung von Büchern auf Amazon
* Fotos auf Snapchat mit Katzenohren zu versehen
* automatische Übersetzung
* AlphaGo
* Roboterfußball

## Wie geht Machine Learning?

Um beim Machine Learning gut zu sein, sind drei Fähigkeiten nötig:

![Venn Diagram of Data Science](images/venn_diagram.png)

*Bildquelle: [Data Science Venn Diagram von Drew Conway, CC-BY-NC](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)*

## Was für Verfahren gibt es?

Das Feld entwickelt sich seit einigen Jahren rasant. Schneller als ich irgend etwas darüber schreiben kann. Einige Verfahren sind jedoch seit vielen Jahren Dauerbrenner. Hier ist ein grober Überblick.

# Grundbegriffe

## Modellparameter

Die Parameter, die ein Modell beim Lernen automatisch einstellt.

## Hyperparameter

Die Parameter, die Du selbst auswählen musst.

## Overfitting

Overfitting bedeutet, dass das Modell die Daten zu detailliert beschreibt (d.h. es lernt die Daten auswendig). Ein Overfitting lässt sich daran erkennen, dass für unabhängige *Testdaten* die Vorhersage schlechter ist als für die Trainingsdaten. Overfitting lässt sich vermeiden, indem man **die Komplexität des Modells reduziert** oder **die Datenmenge erhöht**.

## Underfitting

Underfitting bedeutet, dass das Modell nicht alle Informationen in den Daten verwendet. Es vereinfacht zu stark. Du erkennst Underfitting daran, dass die *Trainingsdaten* nicht gut vorhergesagt werden. Underfitting kann vermieden werden, indem man **die Komplexität des Modells vergrößert**.

## Trainings- und Testdatensätze
Ein Standardansatz ist die Unterteilung der Daten in Trainings- und Testdaten (in der Regel 80% zum Trainieren). Die Testdaten werden nicht für den Aufbau des Modells verwendet, so dass Sie anschließend mit unabhängigen Daten analysieren können, wie gut das Modell wirklich ist.

**Die Testdaten sind erst ganz am Ende und einmalig zu verwenden, damit keine Rückkopplung auf das Modell stattfindet!**

## Testen mehrerer Modelle oder Hyperparameter
Wenn Du mehr als ein Modell evaluierst, ist es unbedingt zu empfehlen, zusätzliche **Validierungsdaten** zu verwenden, um eine Rückkopplung der Testdaten auf das Modell zu vermeiden.

## Kreuzvalidierung

Bei der N-fachen Kreuzvalidierung wird der Datensatz in N Untermengen gleicher Größe aufgeteilt. Bei jedem weiteren Lauf wird eine dieser Portionen als Testdaten verwendet, die restlichen als Trainingsdaten.
So können Sie die Robustheit Ihrer Daten überprüfen.

Es gibt mehrere Varianten dieser Idee (z.B. *Shuffle Split* und *Bootstrapping*).

## Bias

Eine systematische Abweichung (Verzerrung), die das Modell vornimmt.

## Gleichgewicht zwischen Bias und Varianz

In vielen Modellen stehst Du vor der Wahl, die **Varianz** Ihrer Vorhersagen zu senken, aber dafür ein höheres **Bias** in Kauf zu nehmen. Oder umgekehrt. Die Aufgabe eines Data Scientist ist, das für eine konkrete Anwendung optimale Gleichgewicht zu finden.

## Fluch der Dimensionalität

Der **Kurs der Dimensionalität** bezieht sich auf eine Eigenschaft hochdimensionaler Vektoren. Je mehr Dimensionen die Daten haben, desto spärlicher ist der mehrdimensionale Raum belegt. Geometrisch gesehen sind in einem hochdimensionalen Datensatz alle Punkte gleich weit voneinander entfernt.

Siehe [From Regression to Sparsity](http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html#linear-model-from-regression-to-sparsity)

# Klassifikation

Bei der **Klassifikation** werden Datenpunkte einer fest vorgegeben Auswahl von **Kategorien** zugeordnet. Man unterscheidet **binäre Klassifikation** (*"Ist die Email Spam oder nicht?"*) und **Klassifikation mit mehreren Kategorien** (*"Welches Tier ist auf dem Bild zu sehen?"*).

Es gibt eine Unmenge an Klassifikationsverfahren, die alle ihre Vor- und Nachteile haben. Hier sind die wichtigsten kurz vorgestellt.

## Logistische Regression

Bei der **logistischen Regression** verwenden wir die logistische Funktion ($y = 1 / (1 + e^x)$), um Grenzen zwischen Klassen zu ziehen.

Im Gegensatz zur linearen Regression funktioniert die Methode der kleinsten Quadrate hier nicht. Stattdessen werden die Parameter durch Maximierung der **logarithmierten Wahrscheinlichkeit** (logit) der Funktion gefunden.

Siehe auch [Logistic Regression auf Scikit-Learn](http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)

## Support Vector Machines

Bei einer **Support Vector Machine (SVM)**, suchen wir eine **Hyperebene**, die die Daten am besten einteilt. Um nicht lineare Grenzen zu ermöglichen, werden die daten mit einem *Kernel* in einen höher dimensionalen Raum transformiert.

Siehe auch [SVM auf Scikit-Learn](http://scikit-learn.org/stable/modules/svm.html)

## Naive Bayes

In einem Naive Bayes-Klassifikator werden die bedingten Wahrscheinlichkeiten $P(X_i|Y)$ geschätzt, indem man einfach das gemeinsame Auftreten von Merkmal $X_i$ und dem Label $Y$ in den Trainingsdaten zählt. Die Wahrscheinlichkeiten für die Vorhersage werden als Produkt aller Wahrscheinlichkeiten $P_1... P_n$ berechnet.

Naive Bayes basiert auf der Annahme, dass alle Merkmale $X_i$ unabhängig voneinander auftreten. Dies ist eine schreckliche Vermutung! Dennoch funktioniert Naive Bayes im wirklichen Leben erstaunlich gut. Die Methode hat eine lange Erfolgsgeschichte beim Ausfiltern von Spam.


## k-Nächste-Nachbarn

Bei k-Nächste-Nachbarn wird ein Distanzkriterium verwendet, um *k* Datenpunkte in den Trainingsdaten zu finden, die dem zu klassifizierenden am nächsten liegen. Die häufigste Kategorie in diesen *k* Punkten (oder eine gewichtete Mehrheit) wird als Vorhersage verwendet.

## Entscheidungsbäume

Ein Entscheidungsbaum konstruiert einen Binärbaum, in dem jeder Knoten den Trainingsdatensatz anhand einer Frage in zwei Teilmengen teilt. Bei jeder dieser wird jeweils eine weitere Frage zur Unterscheidung gesucht usw. Entscheidungsbäume können gut mit einer Mischung aus numerischen und kategorischen Daten arbeiten. Sie sind leicht zu interpretieren und können die Daten sehr detailliert modellieren.

Wegen der letztgenanten Eigenschaft sind **Entscheidungsbäume sehr anfällig für Overfitting**.

### Random Forests

**Random Forests**, eine Ensemblemethode, lösen das Problem bei Entscheidungsbäumen etwas. Es werden mehrere Entscheidungsbäume erstellt, die sich zufallsbasiert leicht unterscheiden (zufällig ausgewählte Trainingsdaten und Merkmale). Die Vorhersage ist eine Mehrheitsentscheidung der beteiligten Bäume im Ensemble.


## Qualitätsmaße

### Konfusionsmatrix

Eine Matrix mit vier Quadranten, **Richtig Positiven (RP)**, **Richtig Negativen (RP)**, **Falsch Positiven (FP)** und **Falsch Negativen (FN)**.


### Genauigkeit

Die **Genauigkeit (Accuracy)** ist der Anteil korrekter Vorhersagen an den Vorhersagen insgesamt.

    accuracy = (RP + RN) / (RP + FP + FN + RN)

**Achtung:** Wenn der Datensatz *nicht balanciert* ist, ist die Genauigkeit kein besonders gutes Qualitätsmaß!

### Relevanz

Der Anteil Richtig Positiver an allen positiven Vorhersagen.

    relevanz = RP / (RP + FP)

### Sensitivität

Der Anteil Richtig Positiver an allen positiven Vorhersagen.

    sensitivität = RP / (RP + FN)

# Regression

## Lineare Regression

In der einfachsten Form passt die lineare Regression eine Gerade an x/y-Daten an. Dies geschieht durch Minimierung der quadratischen Abweichung von den y-Werten (**Least-Squares-Methode**). In der Praxis geschieht dies meistens durch ein **Gradientenverfahren**.

## Polynomielle Regression

Statt einer geraden Linie wird ein Polynom höherer Ordnung verwendet.

## Multiple Regression

Bei der multiplen Regression sind die x-Werte ein *Vektor*.
Ein Zweck der multiplen Regression ist es, **zu erklären**, welcher Faktor (oder eine Kombination von mehreren) am stärksten zu den y-Werten beiträgt.

Eine allgemeine Annahme einer multiplen Regression ist, dass die Merkmale im x-Vektor *linear unabhängig* sind. Trifft diese Annahme nicht zu, gibt es keine für das Modell keine Lösung.


## Regularisierung

Ein häufiges Problem bei linearen Modellen ist, dass die Anzahl der Parameter oft sehr groß wird. Die Ergebnisse sind daher schwer zu interpretieren und das Risiko für Overfitting wächts. Bei **Regularisierung** wird ein Strafterm addiert, um große Koeffizienten zu begrenzen.

In `scikit-learn` stehen zwei Varianten zur Verfügung: [Ridge Regression](http://scikit-learn.org/stable/modules/linear_model.html#ridge-regression) und [Lasso Regression](http://scikit-learn.org/stable/modules/linear_model.html#lasso).

## Lineare Solver

Das Python-Paket **Pulp** löst linearen Gleichungssysteme. Dazu definierst Du die Parameter des Modells, die zu optimierende lineare Kostenfunktion und eine beliebige Menge von Constraints.

Siehe das Beispiel [Sudoku lösen](http://pythonhosted.org/PuLP/CaseStudies/a_sudoku_problem.html).

## Weitere Regressionsverfahren

Eine weitere Methode zur Regression sind **Regressionsbäume**. Schaue Die dazu den *RandomForestRegressor* näher an.

## Achtung!

Die **logistische Regression** ist ein Klassifikationsverfahren!
# Unüberwachtes Lernen

Beim **unüberwachten Lernen** gibt es keine Trainingsdaten. Die richtigen Antworten sind nicht im Voraus bekannt. Es geht meist darum die Daten zu *clustern*, *die Anzahl der Dimensionen zu reduzieren* oder *Ausreißer zu finden*.

## k-means Clustering

Beim **k-means Clustering** werden die Daten in exakt *k* Cluster eingeteilt. Der Mittelpunkt jedes Clusters wird so gewählt, dass die Entfernung jedes Datenpunktes zum Clustermittelpunkt minimal wird.

Das k-means Clustering ist eine robuste Method, deren Hauptnachteil darin besteht, dass Sie den richtigen Wert für *k* selbst finden müssen.

## Hauptkomponentenzerlegung

Die **Hauptkomponentenzerlegung (PCA)** transformiert die Daten so, dass deren wichtigste Eigenschaft durch eine Koordinate ausgedrückt wird, die zweitwichtigste Eigenschaft durch eine weitere Koordinate usw. Diese Eigenschaften nennt man **Hauptkomponenten**.

**Beispiel:** Bei Schiffen lassen sich viele Eigenschaften wie Länge, Breite, Tiefgang Bruttoregistertonnen usw. durch eine Eigenschaft, die Größe ausdrücken. Die nächstwichtige Eigenschaft könnte sein, ob das Schiff eher bauchig oder länglich ist.

Die Hauptkomponentenzerlegung hat den Vorteil, dass sich die Hauptkomponenten schnell und automatisch berechnen lassen. Mit wenigen Hauptkomponenten läßt sich oft einfacher weiter arbeiten (z.B. mit einem überwachten Verfahren).

Der Nachteil ist, dass sich die Hauptkomponenten meist nicht leicht interpretieren lassen (anders als im Beispiel mit den Schiffen).


## Weitere Verfahren

Andere beliebte unüberwachte Lernverfahren sind andere **Clusterverfahren**, **Gaussian Mixture Models** und **unsupervised Neural Networks**. Siehe [Models for unsupervised learning on the skikit-learn page](http://scikit-learn.org/stable/unsupervised_learning.html#unsupervised-learning)
